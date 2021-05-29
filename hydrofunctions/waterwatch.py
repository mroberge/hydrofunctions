"""
hydrofunctions.waterwatch
~~~~~~~~~~~~~~~~~~~~~~~~~

This module is for working with the five USGS WaterWatch Data Services.
Description of data services https://waterwatch.usgs.gov/webservices/

Main page: https://waterwatch.usgs.gov

NOTICE (taken from waterwatch.usgs.gov): In January 2020, USGS WaterWatch began 
operating in maintenance-only mode. Existing tools, features, and web data services are 
being fully maintained as before, but new tools and enhancements will no longer be 
developed. Please click here for more information or contact USGS WaterWatch if you have
 any questions.

The WaterWatch program provides five data services with REST APIs:

- Current Conditions Real-Time Streamflow Service
- Flood and High Flow Service
- Average Streamflow for 7, 14, and 28 Days Service
- Hourly Flow Change Service
- Flood Stage Service

Hydrofunctions allows you to access each of these services as either a dictionary
or a dataframe with the station ID as the key/index.
-----
"""
import requests
import pandas as pd

WATERWATCH_URL = "https://waterwatch.usgs.gov/webservices/"


def _get_flood_stages(site_number: str = None):
    """Retrieves flood stages for USGS stations.

    Args:
        param site_number: Optional USGS station number. If not provided flood stages for all stations are retrieved.

    Returns: Dictionary of station numbers and corresponding flood stages
    """
    # response formats: json | xml | csv
    params = {"format": "json"}
    if site_number:
        params["site"] = site_number
    res = requests.get(WATERWATCH_URL + "floodstage", params=params)
    if res.ok:
        stages = res.json()
        return {
            site["site_no"]: {k: v for k, v in site.items() if k != "site_no"}
            for site in stages["sites"]
        }


def filter_flood_stages(all_flood_stages, sites_numbers=None):
    """Filters flood states of specific station numbers"""
    stations_stages = {}
    for site_nb in sites_numbers:
        try:
            stations_stages[site_nb] = all_flood_stages[site_nb]
        except KeyError:
            stations_stages[site_nb] = None
    return stations_stages


def get_flood_stage(site=None, output_format="dict"):
    """Retrieves flood stages for a list of station numbers.

    This function retrieves a dictionary of flood stages for each site. The 'stage' of
    a river is the height of the river surface at a stream gauge, expressed as a height
    above an arbitrary datum. It is similar to water depth, except that datums are
    usually set so that the zero (0) to be well below the lowest elevation of the
    stream bed. This is done so that even if there is erosion over time, the stream bed
    and the river stage will never reach an elevation that is less than zero. Stage is
    usually expressed in feet in this dataset. You can retrieve the stage of the river
    using the parameter '00065', whereas the discharge of the river is '00060'.

    There are several kinds of flood stage reported in these data:

        * action stage: If the water gets above this level, it triggers an action by
            the National Weather Service.
        * flood stage: Water at this level begins to be a hazard to lives, property, or
            commerce. Not necessarily the same as bankfull stage.
        * moderate flood stage: structures and roads begin to be inundated.
        * major flood stage: requires significant evacuations of people or transfer of
            property to higher elevations.

        See https://waterwatch.usgs.gov/webservices/ for more information.

    Args:
        site (str or list of str):
            The USGS site ID number or a list of numbers.

        output_format: Optional output format. Returns dict if 'dict' else returns pd.DataFrame

    Returns: Dictionary or DataFrame of station numbers and their flood stages. If
        there is no flood stage for a station, `None` is returned.

    Example:
        >>> stations = ["07144100", "07144101"]
        >>> res = get_flood_stage(stations, output_format="dict")  # dictionary output
        >>> print(res)
        {'07144100': {'action_stage': '20', 'flood_stage': '22', 'moderate_flood_stage': '25', 'major_flood_stage': '26'},
         '07144101': None}
        >>> print(get_flood_stage(stations))
    """
    all_stages = _get_flood_stages()

    if site:
        if isinstance(site, str):
            site = [site]
        stations_stages = filter_flood_stages(all_stages, site)
    else:
        stations_stages = all_stages

    if output_format == "dict":
        return stations_stages
    else:
        return pd.DataFrame(stations_stages).T
