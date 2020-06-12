"""
hydrofunctions.usgs_rdb
~~~~~~~~~~~~~~~~~~~~~~~

This module is for working with the various USGS dataservices that use the rdb
text format. These include the statistics service, the field measurements
service, the rating curve service, and the peak discharge service.
"""
import pandas as pd
import requests
from io import StringIO
from IPython.core import display
from . import exceptions


class hydroRDB:
    """A class for holding the information from USGS rdb files.

    Args:
        header (str):
            A multi-line string from the header of the rdb file. The header
            often contain important metadata and user warnings.
        table (pandas dataframe):
            This is a dataframe made from the rdb file.
        columns (str):
            A string from the rdb file that lists the column names.
        dtypes (str):
            A string from the rdb file that gives the data type and length of
            each column.


    Note:
        The args to create this object are supplied by hf.read_rdb().
        You can read more about the RDB format here: https://pubs.usgs.gov/of/2003/ofr03123/6.4rdb_format.pdf
    """
    def __init__(self, header, table, columns, dtypes):
        self.header = header
        self.table = table
        self.columns = columns
        self.dtypes = dtypes

    def __iter__(self):
        return iter((self.header, self.table))

    def __repr__(self):
        return f'hydroRDB(header={self.header},\ntable={self.table}'

    def _repr_html_(self):
        html_header = '<p>' + self.header.replace('\n', '<br />') + '</p>'
        #return html_header + self.df._repr_html_()
        return f'<p>hydroRDB(header=<br />{html_header}</p><p>table=<br />{self.table._repr_html_()})</p>'


def get_usgs_RDB_service(url, headers=None, params=None):
    """Request data from a USGS dataservice and handle errors

    Args:
        url (str):
            a string used by Requests as the base URL.
        header (dict):
            a dict of parameters used to request the data.
        params (dict):
            a dict of parameters used to modify the url of a REST service.
    Returns:
        A Requests response object.
    Raises:
        This function will raise an exception for any non-200 status code, and
        in cases where the USGS service returns anything that is not obviously
        an RDB file. If an exception is raised, then an attempt will be made to
        display the error page which the USGS sometimes sends back to the user.
    """
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        if response.text[0] == '#':
            # Everything seems good; they apparently returned an RDB file.
            return response
        else:
            print('The USGS has apparently not returned any data. Check the'
                  'following message for further information for why this'
                  'request failed.')
            display.display(display.HTML(response.text))
            raise exceptions.HydroNoDataError('The USGS did not return a valid RDB file'
                                   'for this request.')
    else:
        #response.status_code != 200:
        print(f'The USGS has returned an error code of {response.status_code}')
        # If this code is being run inside of a notebook, the USGS error page
        # will be displayed.
        display.display(display.HTML(response.text))
        # raise an exception
        response.raise_for_status()
        # or raise some sort of Hydro http error based on requests http error.
    return response


def read_rdb(text):
    """Read strings that are in rdb format.

    Args:
        text (str):
            A long string containing the contents of a rdb file. A common way
            to obtain these would be from the .text property of a requests
            response, as in the example usage below.
    Returns:
        header (list of strings):
            Every commented line at the top of the rdb file is marked with a
            '#' symbol. Each of these lines is stored in this output.
        outputDF (pandas.DataFrame):
            A dataframe containing the information in the rdb file. 'site_no'
            and parameter_cd
            are interpreted as a string, but every other number is interpreted
            as a float or int; missing values as an np.nan; strings for
            everything else.
        columns (list of strings):
            The column names, taken from the rdb header row.
        dtypes (list of strings):
            The second header row from the rdb file. These mostly tell the
            column width, and typically record everything as string data ('s')
            type. The exception to this are dates, which are listed with a 'd'.
    """
    headerlines = []
    datalines = []
    count = 0
    for line in text.splitlines():
        if line[0] == '#':
            headerlines.append(line)
        elif count == 0:
            columns = line.split()
            count = count + 1
        elif count == 1:
            dtypes = line.split()
            count = count + 1
        else:
            datalines.append(line)
    data = "\n".join(datalines)
    header = "\n".join(headerlines)

    outputDF = pd.read_csv(StringIO(data),
                           sep='\t',
                           comment='#',
                           header=None,
                           names=columns,
                           dtype={'site_no': str, 'parameter_cd': str},
                           )

    #outputDF.outputDF.filter(like='_cd').columns
    #TODO: code columns ('*._cd') should be interpreted as strings.

    return header, outputDF, columns, dtypes


def site_file(site):
    """Load USGS site file into a Pandas dataframe

    Args:
        site (str):
            The gauge ID number for the site.

    Returns:
        a hydroRDB object or tuple consisting of the header and a pandas
        dataframe.

    Example:
        ```
        test = site_file('01542500')
        test

        hydroRDB(header=<a mulit-line string of the header>,
                 table=<a Pandas dataframe>)
        ```
        You can also access the header, dataframe, column names, and data types
        through the associated properties:
        ```
        test.table

        <a Pandas dataframe>
        ```
    """
    url = 'https://waterservices.usgs.gov/nwis/site/?format=rdb&sites=' \
          + site + '&siteOutput=expanded&siteStatus=all'
    headers = {'Accept-encoding': 'gzip'}

    print("Retrieving the site file for site #", site, " from ", url)
    response = get_usgs_RDB_service(url, headers)
    header, outputDF, columns, dtype, = read_rdb(response.text)
    output_obj = hydroRDB(header, outputDF, columns, dtype)

    return output_obj
def field_meas(site):
    """Load USGS field measurements of stream discharge into a Pandas dataframe

    Args:
        site (str):
            The gage ID number for the site.

    Returns:
        a dataframe. Each row represents an observation on a given date of
        river conditions at the gage by USGS personnel. Values are stored in
        columns, and include the measured stream discharge, channel width,
        channel area, depth, and velocity. These data can be used to create a
        rating curve, to estimate the gage height for a discharge of zero, and
        to get readings of water velocity.

    NOTES:
        To plot a rating curve, use:
            `output.plot(x='gage_height_va', y='discharge_va', kind='scatter')`

        Rating curves are typically plotted with the indepedent variable,
        gage_height, plotted on the Y axis.

    Discussion:
        The USGS operates over 8,000 stream gages around the United States and
        territories. Each of these sensors records the depth, or 'stage' of the
        water. In order to translate this stage data into stream discharge, the
        USGS staff creates an empirical relationship called a 'rating curve'
        between the river stage and stream discharge. To construct this curve,
        the USGS personnel visit all of the gage every one to eight weeks, and
        measure the stage and the discharge of the river manually.

        The `field_meas()` function returns all of the field-collected data for
        this site. You can use these data to create your own rating curve or to
        read the notes about local conditions.

        The `rating_curve()` function returns the most recent 'expanded shift-
        adjusted' rating curve constructed for this site.

    """
    url = 'https://waterdata.usgs.gov/nwis/measurements?site_no=' + site + \
          '&agency_cd=USGS&format=rdb_expanded'
    headers = {'Accept-encoding': 'gzip'}

    print("Retrieving field measurements for site #", site, " from ", url)
    response = get_usgs_RDB_service(url, headers)
    # It may be desireable to keep the original na_values, like 'unkn' for many
    # of the columns. However, it is still a good idea to replace for the gage
    # depth and discharge values, since these variables get used in plotting
    # functions.
    header, outputDF, columns, dtype, = read_rdb(response.text)
    outputDF.measurement_dt = pd.to_datetime(outputDF.measurement_dt)

    # An attempt to use the tz_cd column to make measurement_dt timezone aware.
    #outputDF.tz_cd.replace({np.nan: 'UTC'}, inplace=True)
    #def f(x, y):
    #    return x.tz_localize(y)
    #outputDF['datetime'] = outputDF[['measurement_dt', 'tz_cd']].apply(lambda x: f(*x), axis=1)

    outputDF.set_index('measurement_dt', inplace=True)

    output_obj = hydroRDB(header, outputDF, columns, dtype)

    return output_obj


def peaks(site):
    """Return a series of annual peak discharges.

    Args:
        site(str):
            The gauge ID number for the site.

    Returns:
        a dataframe with the annual peak discharge series.

        a header of meta-data supplied by the USGS with the data series.
    """
    url = 'https://nwis.waterdata.usgs.gov/nwis/peak?site_no=' + site + \
        '&agency_cd=USGS&format=rdb'

    headers = {'Accept-encoding': 'gzip'}

    print("Retrieving annual peak discharges for site #", site, " from ", url)
    response = get_usgs_RDB_service(url, headers)
    header, outputDF, columns, dtype = read_rdb(response.text)
    outputDF.peak_dt = pd.to_datetime(outputDF.peak_dt)

    outputDF.set_index('peak_dt', inplace=True)

    output_obj = hydroRDB(header, outputDF, columns, dtype)
    return output_obj


def rating_curve(site):
    """Return the most recent USGS expanded-shift-adjusted rating curve for a
    given stream gage into a dataframe.

    Args:
        site (str):
            The gage ID number for the site.

    Returns:
        a dataframe with the most recent rating curve.

    Note:
        Rating curves change over time
    """
    url = "https://waterdata.usgs.gov/nwisweb/data/ratings/exsa/USGS." + \
          site + ".exsa.rdb"
    headers = {'Accept-encoding': 'gzip'}
    print("Retrieving rating curve for site #", site, " from ", url)
    response = get_usgs_RDB_service(url, headers)
    header, outputDF, columns, dtype = read_rdb(response.text)
    outputDF.columns = ['stage', 'shift', 'discharge', 'stor']
    """
    outputDF = pd.read_csv(StringIO(response.text),
                     sep='\t',
                     comment='#',
                     header=1,
                     names=['stage', 'shift', 'discharge', 'stor'],
                     skiprows=2
                     )
    """
    output_obj = hydroRDB(header, outputDF, columns, dtype)
    return output_obj


def stats(site, statReportType='daily', **kwargs):
    """Return statistics from the USGS Stats Service as a dataframe.

    Args:
        site (str):
            The gage ID number for the site, or a series of gage IDs separated
            by commas, like this: '01546500,01548000'.

        statReportType ('annual'|'monthly'|'daily'):
            There are three different types of report that you can request.
            - 'daily' (default): this

    Returns:
        a dataframe with the requested statistics.

    Raises:
        HTTPError when a non-200 http status code is returned.

    Note:
        This function is based on the USGS statistics service, described here:
        https://waterservices.usgs.gov/rest/Statistics-Service.html

        The USGS Statistics Service allows you to specify a wide array of
        additional parameters in your request. You can provide these parameters
        as keyword arguments, like in this example:
        `hf.stats('01452500', parameterCD='00060')`  This will only request
        statistics for discharge, which is specified with the '00060'
        parameter code.

        Additional useful parameters include:

            - `parameterCD='00060,00065'` Limit the request for statistics to
              only one parameter or to a list of parameters. The default behavior
              is to provide statistics for every parameter that has been measured
              at this site. In this example, statistics for discharge ('00060')
              and stage ('00065') are requested.

            - `statYearType='water'` Calculate annual statistics based on the
              water year, which runs from October 1st to September 31st. This
              parameter is only for use with annual reports. If not specified,
              the default behavior will use calendar years for reporting.

            - `missingData='on'`  Calculate statistics even when there are some
              missing values. If not specified, the default behavior is to drop
              years that have fewer than 365 values from annual reports, and to
              drop months that have fewer than 30 values in monthly reports. The
              number of values used to calculate a statistic is reported in the
              'count_nu' column.

            - You can read about other useful parameters here: https://waterservices.usgs.gov/rest/Statistics-Service.html#statistical_Controls

    """
    url = "https://waterservices.usgs.gov/nwis/stat/"

    headers = {
            'Accept-encoding': 'gzip',
            }
    # Set default values for parameters that are too obscure to put into call
    # signature.
    params = {
            'statReportType': statReportType,
            'statType': 'all',
            'sites': site,
            'format': 'rdb',
            }
    # Overwrite defaults if they are specified.
    params.update(kwargs)

    response = get_usgs_RDB_service(url, headers, params)
    print(f"Retrieving {params['statReportType']} statistics for site #{params['sites']} from {response.url}")

    header, outputDF, columns, dtype = read_rdb(response.text)

    output_obj = hydroRDB(header, outputDF, columns, dtype)
    return output_obj
