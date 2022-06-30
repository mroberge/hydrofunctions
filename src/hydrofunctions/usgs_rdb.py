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
from IPython import display
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
        rdb (str):
            The complete original text of the rdb file.

    **Properties:**
        **header** (str):
            A multi-line string from the header of the rdb file. The header
            often contain important metadata and user warnings.
        **table** (pandas dataframe):
            This is a dataframe made from the rdb file.
        **columns** (str):
            A string from the rdb file that lists the column names.
        **dtypes** (str):
            A string from the rdb file that gives the data type and length of
            each column.
        **rdb** (str):
            The original, unparsed rdb file as returned by the USGS.

        You can also access the header and the dataframe as a named tuple::

            hydroRDB(header=<a multi-line string>, table=<pandas dataframe>)

    Note:
        - The args to create this object are supplied by hf.read_rdb().
        - The hydroRDB object is returned from several functions that request\
        RDB files from a USGS data service, including: peaks(), field_meas(),\
        rating_curve(), stats(), site_file(), and data_catalog().
        - You can read more about the RDB format here: https://pubs.usgs.gov/of/2003/ofr03123/6.4rdb_format.pdf
    """

    def __init__(self, header, table, columns, dtypes, rdb_str):
        self.header = header
        self.table = table
        self.columns = columns
        self.dtypes = dtypes
        self.rdb = rdb_str

    def __iter__(self):
        return iter((self.header, self.table))

    def __repr__(self):
        return f"hydroRDB(header={self.header},\ntable={self.table}"

    def _repr_html_(self):
        html_header = "<p>" + self.header.replace("\n", "<br />") + "</p>"
        # return html_header + self.df._repr_html_()
        return f"<p>hydroRDB(header=<br />{html_header}</p><p>table=<br />{self.table._repr_html_()})</p>"


def get_usgs_RDB_service(url, headers=None, params=None):
    """Request data from a USGS dataservice and handle errors.

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
        This function will raise an exception for any non-200 status code, and\
        in cases where the USGS service returns anything that is not obviously\
        an RDB file. If an exception is raised, then an attempt will be made to\
        display the error page which the USGS sometimes sends back to the user.
    """
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        if response.text[0] == "#":
            # Everything seems good; they apparently returned an RDB file.
            return response
        else:
            print(
                "The USGS has apparently not returned any data. Check the "
                "following message for further information for why this "
                "request failed. One possibility is that your site number "
                "is incorrect."
            )
            display.display(display.HTML(response.text))
            raise exceptions.HydroNoDataError(
                "The USGS did not return a valid RDB file for this request."
            )
    else:
        # response.status_code != 200:
        print(f"The USGS has returned an error code of {response.status_code}")
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
        header (multi-line string):
            Every commented line at the top of the rdb file is marked with a
            '#' symbol. Each of these lines is stored in this output.
        outputDF (pandas.DataFrame):
            A dataframe containing the information in the rdb file. `site_no`
            and `parameter_cd` are interpreted as a string, but every other number
            is interpreted as a float or int; missing values as an np.nan;
            strings for everything else.
        columns (list of strings):
            The column names, taken from the rdb header row.
        dtypes (list of strings):
            The second header row from the rdb file. These mostly tell the
            column width, and typically record everything as string data ('s')
            type. The exception to this are dates, which are listed with a 'd'.
    """
    try:
        headerlines = []
        datalines = []
        count = 0
        for line in text.splitlines():
            if line[0] == "#":
                headerlines.append(line)
            elif count == 0:
                columns = line.split()
                count += 1
            elif count == 1:
                dtypes = line.split()
                count += 1
            else:
                datalines.append(line)
        data = "\n".join(datalines)
        header = "\n".join(headerlines)

        outputDF = pd.read_csv(
            StringIO(data),
            sep="\t",
            comment="#",
            header=None,
            names=columns,
            dtype={"site_no": str, "parameter_cd": str},
            # When converted like this, poorly-formed dates will be saved as strings
            parse_dates=True,
            # If dates are converted like this, then poorly formed dates will stop the process
            # converters={"peak_dt": pd.to_datetime},
        )
        # Another approach would be to convert date columns later, and catch errors
        # try:
        #   outputDF.peak_dt = pd.to_datetime(outputDF.peak_dt)
        # except ValueError as err:
        #   print(f"Unable to parse date. reason: '{str(err)}'.")

    except:
        print(
            "There appears to be an error processing the file that the USGS "
            "returned. This sometimes occurs if you entered the wrong site "
            "number. We were expecting an RDB file, but we received the "
            f"following instead:\n{text}"
        )
        raise
    # outputDF.outputDF.filter(like='_cd').columns
    # TODO: code columns ('*._cd') should be interpreted as strings.
    # TODO: date columns ('*_dt') should be converted to dates.

    return header, outputDF, columns, dtypes


def site_file(site, verbose=True):
    """Load USGS site file into a Pandas dataframe.

    Args:
        site (str):
            The gauge ID number for the site.
        verbose (bool):
            If True (default), will print confirmation messages with the url before and
            after the request.

    Returns:
        a hydroRDB object or tuple consisting of the header and a pandas
        dataframe. The dataframe will have one row for every site requested; for each
        site it will provide detailed site characteristics such as watershed area, 
        drainage basin HUC code, site latitude, longitude, altitude, and datum; the date
        the site was established, hole depth for wells, and other information. All of
        the columns are listed in the header; for more information, visit: 
        http://waterservices.usgs.gov/rest/Site-Service.html

        For information on the data collected at this site (including the start and stop
        dates for data collection), use the 'data_catalog' function. 

    **Example:**

        >>> test = site_file('01542500')

        >>> test
        hydroRDB(header=<a multi-line string of the header>,
                 table=<a Pandas dataframe>)

    You can also access the header, dataframe, column names, and data types
    through the associated properties `header`, `table`, `columns`, `dtypes`::

        >>> test.table
        <a Pandas dataframe>

    """
    url = (
        "https://waterservices.usgs.gov/nwis/site/?format=rdb&sites="
        + site
        + "&siteOutput=expanded&siteStatus=all"
    )
    headers = {"Accept-encoding": "gzip"}

    if verbose:
        print(f"Retrieving the site file for site #{site} from {url}", end="\r")
    response = get_usgs_RDB_service(url, headers)
    if verbose:
        print(f"Retrieved the site file for site #{site} from {url}")
    (
        header,
        outputDF,
        columns,
        dtype,
    ) = read_rdb(response.text)

    return hydroRDB(header, outputDF, columns, dtype, response.text)


def data_catalog(site, verbose=True):
    """Load a history of the data collected at a site into a Pandas dataframe.

    Args:
        site (str):
            The gauge ID number for the site.
        verbose (bool):
            If True (default), will print confirmation messages with the url before and
            after the request.

    Returns:
        a hydroRDB object or tuple consisting of the header and a pandas
        dataframe.  The dataframe will have one row for every type of data collected at
        each site requested; for each data parameter it will provide information 
        including: parameter code, date of first observation, date of last observation,
        and total number of observations. A full description of the data catalog is
        given in the header; more information is available at: 
        http://waterservices.usgs.gov/rest/Site-Service.html

        For information about the site itself, including watershed area and HUC code, 
        use the 'site_file' function.

    **Example:**

        >>> test = data_catalog('01542500')
        >>> test
        hydroRDB(header=<a mulit-line string of the header>,
                 table=<a Pandas dataframe>)

    You can also access the header, dataframe, column names, and data types
    through the associated properties `header`, `table`, `columns`, `dtypes`::

        >>> test.table
        <a Pandas dataframe>

    """
    url = (
        "https://waterservices.usgs.gov/nwis/site/?format=rdb&sites="
        + site
        + "&seriesCatalogOutput=true&siteStatus=all"
    )
    headers = {"Accept-encoding": "gzip"}

    if verbose:
        print(f"Retrieving the data catalog for site #{site} from {url}", end="\r")
    response = get_usgs_RDB_service(url, headers)
    if verbose:
        print(f"Retrieved the data catalog for site #{site} from {url}")
    (
        header,
        outputDF,
        columns,
        dtype,
    ) = read_rdb(response.text)
    return hydroRDB(header, outputDF, columns, dtype, response.text)


def field_meas(site, verbose=True):
    """Load USGS field measurements of stream discharge into a Pandas dataframe.

    Args:
        site (str):
            The gauge ID number for the site.
        verbose (bool):
            If True (default), will print confirmation messages with the url before and
            after the request.

    Returns:
        a hydroRDB object or tuple consisting of the header and a pandas
        dataframe. Each row of the table represents an observation on a given date of
        river conditions at the gauge by USGS personnel. Values are stored in
        columns, and include the measured stream discharge, channel width,
        channel area, depth, and velocity.

    **Example:**

        >>> test = field_meas('01542500')
        >>> test
        hydroRDB(header=<a mulit-line string of the header>,
                 table=<a Pandas dataframe>)

    You can also access the header, dataframe, column names, and data types
    through the associated properties `header`, `table`, `columns`, `dtypes`::

        >>> test.table
        <a Pandas dataframe>

    **Discussion:**
        The USGS operates over 8,000 stream gages around the United States and
        territories. Each of these sensors records the depth, or 'stage' of the
        water. In order to translate this stage data into stream discharge, the
        USGS staff creates an empirical relationship called a 'rating curve'
        between the river stage and stream discharge. To construct this curve,
        the USGS personnel visit all of the gage every one to eight weeks, and
        measure the stage and the discharge of the river manually.

        The ``field_meas()`` function returns all of the field-collected data for
        this site. The USGS uses these data to create the rating curve. You can use
        these data to see how the site has changed over time, or to
        read the notes about local conditions.

        The ``rating_curve()`` function returns the most recent 'expanded shift-
        adjusted' rating curve constructed for this site. This is the current official
        rating curve.

        To plot a rating curve from the field measurements, use::

            >>> header, data = hf.field_meas('01581830')

            >>> data.plot(x='gage_height_va', y='discharge_va', kind='scatter')

        Rating curves are typically plotted with the indepedent variable,
        gage_height, plotted on the Y axis.
    """
    url = (
        "https://waterdata.usgs.gov/nwis/measurements?site_no="
        + site
        + "&agency_cd=USGS&format=rdb_expanded"
    )
    headers = {"Accept-encoding": "gzip"}

    if verbose:
        print(
            f"Retrieving the field measurements for site #{site} from {url}", end="\r"
        )
    response = get_usgs_RDB_service(url, headers)
    if verbose:
        print(f"Retrieved the field measurements for site #{site} from {url}")
    # It may be desireable to keep the original na_values, like 'unkn' for many
    # of the columns. However, it is still a good idea to replace for the gage
    # depth and discharge values, since these variables get used in plotting
    # functions.
    (
        header,
        outputDF,
        columns,
        dtype,
    ) = read_rdb(response.text)

    try:
        outputDF.measurement_dt = pd.to_datetime(outputDF.measurement_dt)
    except ValueError as err:
        print(
            f"Unable to parse the measurement_dt field as a date. reason: '{str(err)}'."
        )

    # An attempt to use the tz_cd column to make measurement_dt timezone aware.
    # outputDF.tz_cd.replace({np.nan: 'UTC'}, inplace=True)
    # def f(x, y):
    #    return x.tz_localize(y)
    # outputDF['datetime'] = outputDF[['measurement_dt', 'tz_cd']].apply(lambda x: f(*x), axis=1)

    outputDF.set_index("measurement_dt", inplace=True)
    return hydroRDB(header, outputDF, columns, dtype, response.text)


def peaks(site, verbose=True):
    """Return a series of annual peak discharges.

    Args:
        site(str):
            The gauge ID number for the site.
        verbose (bool):
            If True (default), will print confirmation messages with the url before and
            after the request.

    Returns:
        a hydroRDB object or tuple consisting of the header and a table. The header
        is a multi-line string of metadata supplied by the USGS with the data series.
        The table is a dataframe containing the annual peak discharge series. You can
        use these data to conduct a flood frequency analysis.

    **Example:**

        >>> test = hf.peaks('01542500')
        >>> test
        hydroRDB(header=<a mulit-line string of the header>,
                 table=<a Pandas dataframe>)

    You can also access the header, dataframe, column names, and data types
    through the associated properties `header`, `table`, `columns`, `dtypes`::

        >>> test.table
        <a Pandas dataframe>

    """
    url = (
        "https://nwis.waterdata.usgs.gov/nwis/peak?site_no="
        + site
        + "&agency_cd=USGS&format=rdb"
    )

    headers = {"Accept-encoding": "gzip"}

    if verbose:
        print(
            f"Retrieving the annual peak discharges for site #{site} from {url}",
            end="\r",
        )
    response = get_usgs_RDB_service(url, headers)
    if verbose:
        print(f"Retrieved the annual peak discharges for site #{site} from {url}")
    header, outputDF, columns, dtype = read_rdb(response.text)
    try:
        outputDF.peak_dt = pd.to_datetime(outputDF.peak_dt)
    except ValueError as err:
        print(f"Unable to parse the peak_dt field as a date. Reason: '{str(err)}'.")

    # peak_date might be a string, or it might be a datetime. Both work as an index
    outputDF.set_index("peak_dt", inplace=True)
    return hydroRDB(header, outputDF, columns, dtype, response.text)


def rating_curve(site, verbose=True):
    """Return the most recent USGS expanded-shift-adjusted rating curve for a
    given stream gage into a dataframe.

    Args:
        site (str):
            The gage ID number for the site.
        verbose (bool):
            If True (default), will print confirmation messages with the url before and
            after the request.

    Returns:
        a hydroRDB object or tuple consisting of the header and a table. The header
        is a multi-line string of metadata supplied by the USGS with the data series.
        The table is a dataframe containing the latest official rating curve for the
        site.

    **Example:**

        >>> test = rating_curve('01542500')
        >>> test
        hydroRDB(header=<a mulit-line string of the header>,
                 table=<a Pandas dataframe>)

    You can also access the header, dataframe, column names, and data types
    through the associated properties `header`, `table`, `columns`, `dtypes`::

        >>> test.table
        <a Pandas dataframe>

    **Discussion:**
        The USGS operates over 8,000 stream gauges around the United States and
        territories. Each of these sensors records the depth, or 'stage' of the
        water. In order to translate this stage data into stream discharge, the
        USGS staff creates an empirical relationship called a 'rating curve'
        between the river stage and stream discharge.

        See ``hf.field_meas()`` to access the field data used to construct the
        rating curve.

        **Note:** Rating curves change over time.
    """
    url = (
        "https://waterdata.usgs.gov/nwisweb/data/ratings/exsa/USGS."
        + site
        + ".exsa.rdb"
    )
    headers = {"Accept-encoding": "gzip"}
    if verbose:
        print(f"Retrieving the rating curve for site #{site} from {url}", end="\r")
    response = get_usgs_RDB_service(url, headers)
    if verbose:
        print(f"Retrieved the rating curve for site #{site} from {url}")
    header, outputDF, columns, dtype = read_rdb(response.text)
    outputDF.columns = ["stage", "shift", "discharge", "stor"]
    """
    outputDF = pd.read_csv(StringIO(response.text),
                     sep='\t',
                     comment='#',
                     header=1,
                     names=['stage', 'shift', 'discharge', 'stor'],
                     skiprows=2
                     )
    """
    return hydroRDB(header, outputDF, columns, dtype, response.text)


def stats(site, statReportType="daily", verbose=True, **kwargs):
    """Return statistics from the USGS Stats Service as a dataframe.

    Args:
        site (str):
            The gage ID number for the site, or a series of gage IDs separated
            by commas, like this: '01546500,01548000'.

        statReportType ('daily'|'monthly'|'annual'):
            There are three different types of report that you can request.

            - 'daily' (default): calculate statistics for each of 365 days.
            - 'monthly': calculate statistics for each of the twelve months.
            - 'annual': calculate annual statistics for each year since the start of the record.
        verbose (bool):
            If True (default), will print confirmation messages with the url before and
            after the request.

    Returns:
        a hydroRDB object or tuple consisting of the header and a table. The header
        is a multi-line string of metadata supplied by the USGS with the data series.
        The table is a dataframe containing the latest official statistics for the
        site.

    Raises:
        HTTPError
            when a non-200 http status code is returned.

    **Example:**

        >>> test = stats('01542500', 'monthly')
        >>> test
        hydroRDB(header=<a mulit-line string of the header>,
                 table=<a Pandas dataframe>)

    You can also access the header, dataframe, column names, and data types
    through the associated properties `header`, `table`, `columns`, `dtypes`::

        >>> test.table
        <a Pandas dataframe>

    Note:
        This function is based on the USGS statistics service, described here:
        https://waterservices.usgs.gov/rest/Statistics-Service.html

        The USGS Statistics Service allows you to specify a wide array of
        additional parameters in your request. You can provide these parameters
        as keyword arguments, like in this example::

            >>> hf.stats('01452500', parameterCD='00060')

        This will only request
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
        "Accept-encoding": "gzip",
    }
    # Set default values for parameters that are too obscure to put into call
    # signature.
    params = {
        "statReportType": statReportType,
        "statType": "all",
        "sites": site,
        "format": "rdb",
    }
    # Overwrite defaults if they are specified.
    params.update(kwargs)

    if verbose:
        print(
            f"Retrieving {params['statReportType']} statistics for site #{params['sites']} from {url}",
            end="\r",
        )
    response = get_usgs_RDB_service(url, headers, params)
    if verbose:
        print(
            f"Retrieved {params['statReportType']} statistics for site #{site} from {response.url}"
        )

    header, outputDF, columns, dtype = read_rdb(response.text)

    return hydroRDB(header, outputDF, columns, dtype, response.text)
