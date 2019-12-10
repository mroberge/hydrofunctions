# -*- coding: utf-8 -*-
"""
hydrofunctions.nldi
~~~~~~~~~~~~~~~~~~~

This module holds functions that use the USGS Hydro Network-Linked Data Index.

The Hydro Network-Linked Data Index (NLDI) is a web service that utilizes the
National Hydrolography Dataset (NHD). The NHD, NHDplus V2, and the NHDplus High
Resolution are all spatial datasets that combine collections of points (stream
gauge locations, watershed outlets), lines (stream channels, canals), and
polygons (ponds, watersheds). The various forms of the NHD are usually
available only in formats for use in desktop GIS programs, like ArcMap. The
NLDI is a web service that makes some of the materials available in the NHD as
an online webservice.

For more information on the NLDI, visit:
    - NLDI blog post: https://owi.usgs.gov/blog/nldi-intro/
    - a second source: https://waterdata.usgs.gov/blog/nldi-intro/
    - a demo page: https://cida.usgs.gov/nldi/swagger-ui.html#!/lookup-controller/getRegisteredFeatureUsingGET

The NLDI can return all of the gauges upstream and downstream from a gauge, a
geojson file of the US & DS channel, and the watershed boundary.

"""
from . import exceptions
import requests
from IPython.core.display import display, HTML
def get_nldi(path='', parameters=None):
    """Request data from the NLDI web service.

    If no path or parameters are supplied, this will return json listing all of
    the data services currently supplied by the NLDI. At this time (2019-12-07)
    these include:
        * NHDPlus comid: access items using their unique ID.
        * HUC 12 Pour Points: sets of points showing the location of the pour
        points for the USGS 12-digit watersheds.
        * EPA point sources: sites that discharge into waterways.
        * NWIS sites: USGS stream gauging stations.
        * Water Quality Portal: data collection sites in the EPA Water Quality
        Portal.

    Args:
        path (str):
            Any additional part of the URL to be added to the base url,
            'https://cida.usgs.gov/nldi/'. Default is an empty string, ''.
        parameters (dict):
            A dictionary of additional parameters to be added to the request.
            These will be added to the end of the URL after a '?'.

    Raises:
        HydroNoDataError:
            This indicates that the NLDI service received a valid request for
            something that it does not have. In this case, the service will
            return an empty string. One reason this might happen is if a site
            number has been written incorrectly.
        requests.exceptions.HTTPError:
            If the NLDI service returns anything other than a 200 level status
            code.

    Returns:
        a Requests response object.
            The underlying json data may be accessed using the response.text
            property, or the json may be converted into a Python dict using the
            response.json() method. See Examples for more.

    Example:
        >>> import hydrofunctions as hf
        >>> my_response = hf.get_nldi()
        Requested data from https://cida.usgs.gov/nldi/

        >>> my_response.json()
        [{'source': 'comid',
          'sourceName': 'NHDPlus comid',
          'features': 'https://cida.usgs.gov/nldi/comid'},
         {'source': 'huc12pp',
          'sourceName': 'HUC12 Pour Points',
          'features': 'https://cida.usgs.gov/nldi/huc12pp'},
         {'source': 'npdes_rad',
          'sourceName': 'EPA Office of Water (OW): Facilities that Discharge to Water NHDPlus Indexed Dataset',
          'features': 'https://cida.usgs.gov/nldi/npdes_rad'},
         {'source': 'nwissite',
          'sourceName': 'NWIS Sites',
          'features': 'https://cida.usgs.gov/nldi/nwissite'},
         {'source': 'wqp',
          'sourceName': 'Water Quality Portal',
          'features': 'https://cida.usgs.gov/nldi/wqp'}]

    Notes:
        1 This function can be used to access the full capability of the NLDI
          web service simply by passing in the appropriate path or parameters.
          Only the most useful endpoints of the NLDI's REST API have been given
          functions. See https://owi.usgs.gov/blog/nldi-intro/ for more info.
        2 This function returns a Request response object instead of geojson.
          This is because some applications will need to use the raw json
          string, such as the GeoPandas.read_file() method. Other applications
          will need to translate the raw json string into a Python dict. The
          response object quickly gives access to both of these formats, so it
          was kept for now. This may change in the near future.
    """

    BASE_URL = 'https://cida.usgs.gov/nldi/'
    url = BASE_URL + path
    header = {
        'Accept-encoding': 'gzip',
    }
    response = requests.get(url, params=parameters, headers=header)
    print("Requested data from", response.url)

    # requests will raise a 'ConnectionError' if the connection is refused
    # or if we are disconnected from the internet.

    # .get_nldi() will always return the response.

    # Higher-level code that calls get_nldi() may decide to handle or
    # report status codes that indicate something went wrong.

    if response.status_code != 200:
        print('There was an error. Status code = ' + str(response.status_code))
        display(HTML(response.text))
        response.raise_for_status()

    if not response.text:
        raise exceptions.HydroNoDataError("The NWIS has returned an empty string for this "
                               "request. This may indicate that you requested "
                               "data for a site that does not exist.")

    return response
