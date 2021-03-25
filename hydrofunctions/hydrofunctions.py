"""
hydrofunctions.hydrofunctions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module contains the main functions used in an interactive session.

-----
"""
from __future__ import absolute_import, print_function, division, unicode_literals
import requests
import numpy as np
import pandas as pd
import json
import gzip
import pyarrow as pa
import pyarrow.parquet as pq
from pandas.tseries.frequencies import to_offset
import logging

# Change to relative import: from . import exceptions
# https://axialcorps.com/2013/08/29/5-simple-rules-for-building-great-python-packages/
from . import exceptions
import warnings
from . import typing
from . import helpers

logging.basicConfig(
    filename="hydrofunctions_testing.log",
    level=logging.ERROR,
    format="%(asctime)s:%(levelname)s:%(message)s",
)


def select_data(nwis_df):
    """Create a boolean array of columns that contain data.

    Args:
        nwis_df:
            A pandas dataframe created by ``extract_nwis_df``.

    Returns:
        an array of Boolean values corresponding to the columns in the
        original dataframe.

    Example:

        >>> my_dataframe[:, select_data(my_dataframe)]

        returns a dataframe with only the data columns; the qualifier columns
        do not show.
    """
    data_regex = r"[0-9]$"
    return nwis_df.columns.str.contains(data_regex)


def calc_freq(index):
    # Method 0: calc_freq() was called, but we haven't done anything yet.
    method = 0
    if isinstance(index, pd.DataFrame):
        index = index.index
    try:
        # Method 1: Try the direct approach first. Maybe freq has already been set.
        freq = index.freq
        method = 1
    except AttributeError:
        # index.freq does not exist, so let's keep trying.
        freq = None

    if freq is None:
        # Method 2: Use the built-in pd.infer_freq(). It raises ValueError
        #    when it fails, so catch ValueErrors and keep trying.
        try:
            freq = to_offset(pd.infer_freq(index))
            method = 2
        except ValueError:
            pass

    if freq is None:
        # Method 3: divide the length of time by the number of observations.
        freq = (index.max() - index.min()) / len(index)
        if pd.Timedelta("13 minutes") < freq < pd.Timedelta("17 minutes"):
            freq = to_offset("15min")
        elif pd.Timedelta("27 minutes") < freq < pd.Timedelta("33 minutes"):
            freq = to_offset("30min")
        elif pd.Timedelta("55 minutes") < freq < pd.Timedelta("65 minutes"):
            freq = to_offset("60min")
        else:
            freq = None
        method = 3

    if freq is None:
        # Method 4: Subtract two adjacent values and use the difference!
        if len(index) > 3:
            freq = to_offset(abs(index[2] - index[3]))
            method = 4
            logging.debug(
                "calc_freq4:"
                + str(freq)
                + "= index[2]:"
                + str(index[3])
                + "- index [3]:"
                + str(index[2])
            )

    if freq is None:
        # Method 5: If all else fails, freq is 0 minutes!
        warnings.warn(
            "It is not possible to determine the frequency "
            "for one of the datasets in this request. "
            "This dataset will be set to a frequency of "
            "0 minutes",
            exceptions.HydroUserWarning,
        )

        freq = to_offset("0min")
        method = 5

    debug_msg = "Calc_freq method:" + str(method) + "freq:" + str(freq)
    logging.debug(debug_msg)
    return pd.Timedelta(freq)


def get_nwis(
    site,
    service="dv",
    start_date=None,
    end_date=None,
    stateCd=None,
    countyCd=None,
    bBox=None,
    parameterCd="all",
    period=None,
):
    """Request stream gauge data from the USGS NWIS.

    Args:
        site (str or list of strings):
            a valid site is '01585200' or ['01585200', '01646502']. site
            should be `None` if stateCd or countyCd are not `None`.

        service (str):
            can either be 'iv' or 'dv' for instantaneous or daily data.
                - 'dv'(default): daily values. Mean value for an entire day.
                - 'iv': instantaneous value measured at this time. Also known\
                    as 'Real-time data'. Can be measured as often as every\
                    five minutes by the USGS. 15 minutes is more typical.

        start_date (str):
           should take on the form yyyy-mm-dd

        end_date (str):
            should take on the form yyyy-mm-dd

        stateCd (str):
            a valid two-letter state postal abbreviation. Default is `None`.

        countyCd (str or list of strings):
            a valid county abbreviation. Default is `None`.

        bBox (str, list, or tuple):
            a set of coordinates that defines a bounding box.
                * Coordinates are in decimal degrees
                * Longitude values are negative (west of the prime meridian).
                * Latitude values are positive (north of the equator).
                * comma-delimited, no spaces, if provided as a string.
                * The order of the boundaries should be: "West,South,East,North"
                * Example: "-83.000000,36.500000,-81.000000,38.500000"

        parameterCd (str or list of strings):
            NWIS parameter code. Usually a five digit code. Default is 'all'.\
            A valid code can also be given as a list: ``parameterCd=['00060','00065']``
                * if value of 'all' is submitted, then NWIS will return every \
                    parameter collected at this site. (default option)
                * stage: '00065'
                * discharge: '00060'
                * not all sites collect all parameters!
                * See https://nwis.waterdata.usgs.gov/usa/nwis/pmcodes for full list

        period (str):
            NWIS period code. Default is `None`.
                * Format is "PxxD", where xx is the number of days before today.
                * Either use start_date or period, but not both.

    Returns:
        a response object. This function will always return the response,
            even if the NWIS returns a status_code that indicates a problem.

            * response.url: the url we used to request data
            * response.json: the content translated as json
            * response.status_code: the internet status code
                - '200': is a good request
                - non-200 codes will be reported as a warning.
                - '400': is a 'Bad Request'-- the parameters did not make sense
                - see <https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html> for more codes and meaning.
            * response.ok: `True` when we get a '200' status_code

    Raises:
        ConnectionError: due to connection problems like refused connection
            or DNS Error.

        SyntaxWarning: when NWIS returns a response code that is not 200.

    **Example:**

        >>> import hydrofunctions as hf
        >>> response = hf.get_nwis('01585200', 'dv', '2012-06-01', '2012-07-01')

        >>> response
        <response [200]>

        >>> response.json()
        *JSON ensues*

        >>> hf.extract_nwis_df(response)
        *a Pandas dataframe appears*

    Other Valid Ways to Make a Request::

        >>> sites = ['07180500', '03380475', '06926000'] # Request a list of sites.
        >>> service = 'iv'  # Request real-time data
        >>> days = 'P10D'  # Request the last 10 days.
        >>> stage = '00065' # Sites that collect discharge usually collect water depth too.
        >>> response2 = hf.get_nwis(sites, service, period=days, parameterCd=stage)

    Request Data By Location::

        >>> # Request the most recent daily data for every site in Maine
        >>> response3 = hf.get_nwis(None, 'dv', stateCd='ME')
        >>> response3
        <Response [200]>

    The specification for the USGS NWIS IV service is located here:
    http://waterservices.usgs.gov/rest/IV-Service.html
    """

    service = typing.check_NWIS_service(service)

    if parameterCd == "all":
        parameterCd = None

    header = {"Accept-encoding": "gzip", "max-age": "120"}

    values = {
        # specify version of nwis json. Based on WaterML1.1
        # json,1.1 works; json%2C works; json1.1 DOES NOT WORK
        "format": "json,1.1",
        "sites": typing.check_parameter_string(site, "site"),
        "stateCd": stateCd,
        "countyCd": typing.check_parameter_string(countyCd, "county"),
        "bBox": typing.check_NWIS_bBox(bBox),
        "parameterCd": typing.check_parameter_string(parameterCd, "parameterCd"),
        "period": period,
        "startDT": start_date,
        "endDT": end_date,
    }

    # Check that site selection parameters are exclusive!
    total = helpers.count_number_of_truthy([site, stateCd, countyCd, bBox])
    if total == 1:
        pass
    elif total > 1:
        raise ValueError(
            "Select sites using either site, stateCd, "
            "countyCd, or bBox, but not more than one."
        )
    elif total < 1:
        raise ValueError(
            "Select sites using at least one of the following "
            "arguments: site, stateCd, countyCd or bBox."
        )

    # Check that time parameters are not both set.
    # If neither is set, then NWIS will return the most recent observation.
    if start_date and period:
        raise ValueError(
            "Use either start_date or period, or neither, " "but not both."
        )

    if not (start_date or period):
        # User didn't specify time; must be requesting most recent data.
        # See issue #49.
        pass

    url = "https://waterservices.usgs.gov/nwis/"
    url = url + service + "/?"
    response = requests.get(url, params=values, headers=header)
    print("Requested data from", response.url)
    # requests will raise a 'ConnectionError' if the connection is refused
    # or if we are disconnected from the internet.

    # .get_nwis() will always return the response.

    # Higher-level code that calls get_nwis() may decide to handle or
    # report status codes that indicate something went wrong.

    # Issue warnings for bad status codes
    nwis_custom_status_codes(response)
    if not response.text:
        raise exceptions.HydroNoDataError(
            "The NWIS has returned an empty string for this request."
        )

    return response


def get_nwis_property(nwis_dict, key=None, remove_duplicates=False):
    """Returns a list containing property data from an NWIS response object.

    Args:
        nwis_dict (dict):
            the json returned in a response object as produced by ``get_nwis().json()``.

        key (str):
            a valid NWIS response property key. Default is `None`. The index is \
            returned if key is `None`. Valid keys are:
                * None
                * name - constructed name "provider:site:parameterCd:statistic"
                * siteName
                * siteCode
                * timeZoneInfo
                * geoLocation
                * siteType
                * siteProperty
                * variableCode
                * variableName
                * variableDescription
                * valueType
                * unit
                * options
                * noDataValue
        remove_duplicates (bool):
            a flag used to remove duplicate values in the returned list.

    Returns:
        a list with the data for the passed key string.

    Raises:
        HydroNoDataError
            when the request is valid, but NWIS has no data for \
            the parameters provided in the request.

        ValueError when the key is not available.
    """
    # nwis_dict = response_obj.json()

    # strip header and all metadata. ts is the 'timeSeries' element of the
    # response; it is an array of objects that contain time series data.
    ts = nwis_dict["value"]["timeSeries"]
    msg = "The NWIS reports that it does not have any data for this request."

    if len(ts) < 1:
        raise exceptions.HydroNoDataError(msg)

    # This predefines what to expect in the response.
    # Would it be better to look in the response for the key?
    # Pseudo code
    # skip stations with no data
    # if key in tts['variable']:
    #    v = etc
    # elif key in tts['sourceInfo']:
    #    v = etc
    # elif key in tts:
    #    v = etc
    # else just return index or raise an error later
    #
    sourceInfo = [
        "siteName",
        "siteCode",
        "timeZoneInfo",
        "geoLocation",
        "siteType",
        "siteProperty",
    ]
    variable = [
        "variableCode",
        "variableName",
        "variableDescription",
        "valueType",
        "unit",
        "options",
        "noDataValue",
    ]
    root = ["name"]
    vals = []
    try:
        for idx, tts in enumerate(ts):
            d = tts["values"][0]["value"]
            # skip stations with no data
            if len(d) < 1:
                continue
            if key in variable:
                v = tts["variable"][key]
            elif key in sourceInfo:
                v = tts["sourceInfo"][key]
            elif key in root:
                v = tts[key]
            else:
                v = idx  # just return index
            if remove_duplicates:
                if v not in vals:
                    vals.append(v)
            else:
                vals.append(v)
    # Why catch this? If we can't find the key, we already return the index.
    except:  # TODO: dangerous to use bare 'except'  clauses.
        msg = 'The selected key "{}" could not be found'.format(key)
        raise ValueError(msg)
    return vals


def extract_nwis_df(nwis_dict, interpolate=True):
    """Returns a Pandas dataframe and a metadata dict from the NWIS response
    object or the json dict of the response.

    Args:
        nwis_dict (obj):
            the json from a response object as returned by get_nwis().json().
            Alternatively, you may supply the response object itself.

    Returns:
        a pandas dataframe.

    Raises:
        HydroNoDataError
            when the request is valid, but NWIS has no data for
            the parameters provided in the request.

        HydroUserWarning
            when one dataset is sampled at a lower frequency than
            another dataset in the same request.
    """
    if type(nwis_dict) is not dict:
        nwis_dict = nwis_dict.json()

    # strip header and all metadata.
    ts = nwis_dict["value"]["timeSeries"]
    if ts == []:
        # raise a HydroNoDataError if NWIS returns an empty set.
        #
        # Ideally, an empty set exception would be raised when the request
        # is first returned, but I do it here so that the data doesn't get
        # extracted twice.
        # TODO: raise this exception earlier??
        #
        # ** Interactive sessions should have an error raised.
        #
        # **Automated systems should catch these errors and deal with them.
        # In this case, if NWIS returns an empty set, then the request
        # needs to be reconsidered. The request was valid somehow, but
        # there is no data being collected.

        raise exceptions.HydroNoDataError(
            "The NWIS reports that it does not " "have any data for this request."
        )

    # create a list of time series;
    # set the index, set the data types, replace NaNs, sort, find the first and last

    collection = []
    starts = []
    ends = []
    freqs = []
    meta = {}
    for series in ts:
        full_series_name = series["name"]
        name_list = full_series_name.split(":")
        agency = str(name_list[0])
        site_id = agency + ":" + str(name_list[1])
        parameter_cd = str(name_list[2])
        stat = str(name_list[3])
        siteName = series["sourceInfo"]["siteName"]
        siteLatLongSrs = series["sourceInfo"]["geoLocation"]["geogLocation"]
        noDataValues = series["variable"]["noDataValue"]
        variableDescription = series["variable"]["variableDescription"]
        unit = series["variable"]["unit"]["unitCode"]
        values = series["values"]
        for method in values:
            data = method["value"]
            # This line assumes only one method per parameter. See issue #77.
            # data = series["values"][0]["value"]
            if data == []:
                # This parameter has no data. Skip to next series.
                continue
            if len(data) == 1:
                # This parameter only contains the most recent reading.
                # See Issue #49
                pass
            method_description = method["method"][0]["methodDescription"]
            method_id = str(method["method"][0]["methodID"])
            # use method_mod as a modifier for altering parameter names.
            method_mod = "-" + method_id
            if len(values) == 1:
                # If there is only one method, don't bother recording method #.
                method_mod = ""
            series_name = site_id + ":" + parameter_cd + method_mod + ":" + stat
            qualifiers_name = series_name + "_qualifiers"
            DF = pd.DataFrame(data=data)
            DF.index = pd.to_datetime(DF.pop("dateTime"), utc=True)
            DF["value"] = DF["value"].astype(float)
            DF = DF.replace(to_replace=noDataValues, value=np.nan)
            DF["qualifiers"] = DF["qualifiers"].apply(lambda x: ",".join(x))
            DF.rename(
                columns={"qualifiers": qualifiers_name, "value": series_name},
                inplace=True,
            )
            DF.sort_index(inplace=True)
            local_start = DF.index.min()
            local_end = DF.index.max()
            starts.append(local_start)
            ends.append(local_end)
            local_freq = calc_freq(DF.index)
            freqs.append(local_freq)
            if not DF.index.is_unique:
                print(
                    "Series index for "
                    + series_name
                    + " is not unique. Attempting to drop identical rows."
                )
                DF = DF.drop_duplicates(keep="first")
                if not DF.index.is_unique:
                    print(
                        "Series index for "
                        + series_name
                        + " is STILL not unique. Dropping first rows with duplicated date."
                    )
                    DF = DF[~DF.index.duplicated(keep="first")]
            if local_freq > to_offset("0min"):
                local_clean_index = pd.date_range(
                    start=local_start, end=local_end, freq=local_freq, tz="UTC"
                )
                # if len(local_clean_index) != len(DF):
                # This condition happens quite frequently with missing data.
                # print(str(series_name) + "-- clean index length: "+ str(len(local_clean_index)) + " Series length: " + str(len(DF)))
                DF = DF.reindex(index=local_clean_index, copy=True)
            else:
                # The dataframe DF must contain only the most recent data.
                pass
            qual_cols = DF.columns.str.contains("_qualifiers")
            # https://stackoverflow.com/questions/21998354/pandas-wont-fillna-inplace
            # Instead, create a temporary dataframe, fillna, then copy back into original.
            DFquals = DF.loc[:, qual_cols].fillna("hf.missing")
            DF.loc[:, qual_cols] = DFquals

            if local_freq > pd.Timedelta(to_offset("0min")):
                variableFreq_str = str(to_offset(local_freq))
            else:
                variableFreq_str = str(to_offset("0min"))
            parameter_info = {
                "variableFreq": variableFreq_str,
                "variableUnit": unit,
                "variableDescription": variableDescription,
                "methodID": method_id,
                "methodDescription": method_description,
            }
            site_info = {
                "siteName": siteName,
                "siteLatLongSrs": siteLatLongSrs,
                "timeSeries": {},
            }
            # if site is not in meta keys, add it.
            if site_id not in meta:
                meta[site_id] = site_info
            # Add the variable info to the site dict.
            meta[site_id]["timeSeries"][parameter_cd + method_mod] = parameter_info
            collection.append(DF)

    if len(collection) < 1:
        # It seems like this condition should not occur. The NWIS trims the
        # response and returns an empty nwis_dict['value']['timeSeries']
        # if none of the parameters requested have data.
        # If at least one of the paramters have data,
        # then the empty series will get delivered, but with no data.
        # Compare these requests:
        # empty:               https://nwis.waterservices.usgs.gov/nwis/iv/?format=json&sites=01570500&startDT=2018-06-01&endDT=2018-06-01&parameterCd=00045
        # one empty, one full: https://nwis.waterservices.usgs.gov/nwis/iv/?format=json&sites=01570500&startDT=2018-06-01&endDT=2018-06-01&parameterCd=00045,00060
        raise exceptions.HydroNoDataError(
            "The NWIS does not have any data for"
            " the requested combination of sites"
            ", parameters, and dates."
        )
    startmin = min(starts)
    endmax = max(ends)
    # Remove all frequencies of zero from freqs list.
    zero = to_offset("0min")
    freqs2 = list(filter(lambda x: x > zero, freqs))
    if len(freqs2) > 0:
        freqmin = min(freqs)
        freqmax = max(freqs)
        if freqmin != freqmax:
            warnings.warn(
                "One or more datasets in this request is going to be "
                "'upsampled' to " + str(freqmin) + " because the data "
                "were collected at a lower frequency of " + str(freqmax),
                exceptions.HydroUserWarning,
            )
        clean_index = pd.date_range(start=startmin, end=endmax, freq=freqmin, tz="UTC")
        cleanDF = pd.DataFrame(index=clean_index)
        for dataset in collection:
            cleanDF = pd.concat([cleanDF, dataset], axis=1)
        # Replace lines with missing _qualifier flags with hf.upsampled
        qual_cols = cleanDF.columns.str.contains("_qualifiers")
        cleanDFquals = cleanDF.loc[:, qual_cols].fillna("hf.upsampled")
        cleanDF.loc[:, qual_cols] = cleanDFquals
        if interpolate:
            # TODO: mark interpolated values with 'hf.interp'
            # select data, then replace Nans with interpolated values.
            data_cols = cleanDF.columns.str.contains(r"[0-9]$")
            cleanDFdata = cleanDF.loc[:, data_cols].interpolate()
            cleanDF.loc[:, data_cols] = cleanDFdata
    else:
        # If datasets only contain most recent data, then
        # don't set an index or a freq. Just concat all of the datasets.
        cleanDF = pd.concat(collection, axis=1)

    cleanDF.index.name = "datetimeUTC"

    if not DF.index.is_unique:
        DF = DF[~DF.index.duplicated(keep="first")]
    if not DF.index.is_monotonic:
        DF.sort_index(axis=0, inplace=True)

    return cleanDF, meta


def nwis_custom_status_codes(response):
    """
    Raise custom warning messages from the NWIS when it returns a
    status_code that is not 200.

    Args:
        response: a response object as returned by get_nwis().

    Returns:
        * `None`
            if response.status_code == 200
        * `response.status_code`
            for all other status codes.

    Raises:
        SyntaxWarning: when a non-200 status code is returned.
            https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

    Note:
        To raise an exception, call ``response.raise_for_status()``
        This will raise `requests.exceptions.HTTPError` with a helpful message
        or it will return `None` for status code 200.
        From: http://docs.python-requests.org/en/master/user/quickstart/#response-status-codes

        NWIS status_code messages come from:
            https://waterservices.usgs.gov/docs/portable_code.html
        Additional status code documentation:
            https://waterservices.usgs.gov/rest/IV-Service.html#Error
    """
    nwis_msg = {
        "200": "OK",
        "400": "400 Bad Request - "
        "This often occurs if the URL arguments "
        "are inconsistent. For example, if you submit a request using "
        "a startDT and an endDT with the period argument. "
        "An accompanying error should describe why the request was "
        "bad." + "\nError message from NWIS: {}".format(response.reason),
        "403": "403 Access Forbidden - "
        "This should only occur if for some reason the USGS has "
        "blocked your Internet Protocol (IP) address from using "
        "the service. This can happen if we believe that your use "
        "of the service is so excessive that it is seriously "
        "impacting others using the service. To get unblocked, "
        "send us the URL you are using along with the IP using "
        "this form. We may require changes to your query and "
        "frequency of use in order to give you access to the "
        "service again.",
        "404": "404 Not Found - "
        "Returned if and only if the query expresses a combination "
        "of elements where data do not exist. For multi-site "
        "queries, if any data are found, it is returned for those "
        "site/parameters/date ranges where there are data.",
        "503": "500 Internal Server Error - "
        "If you see this, it means there is a problem with the web "
        "service itself. It usually means the application server "
        "is down unexpectedly. This could be caused by a host of "
        "conditions, but changing your query will not solve this "
        "problem. The NWIS application support team has to fix it. Most "
        "of these errors are quickly detected and the support team "
        "is notified if they occur.",
    }
    if response.status_code == 200:
        return None
    # All other status codes will raise a warning.
    else:
        # Use the status_code as a key, return None if key not in dict
        msg = (
            "The NWIS returned a code of {}.\n".format(response.status_code)
            + nwis_msg.get(str(response.status_code))
            + "\n\nURL used in this request: {}".format(response.url)
        )

        # Warnings will not beak the flow. They just print a message.
        # However, they are often supressed in some applications.
        warnings.warn(msg, SyntaxWarning)
        return response.status_code


def read_parquet(filename):
    """Read a hydrofunctions parquet file.

    This function will read a parquet file that was saved by
    hydrofunctions.save_parquet() and return a dataframe and a metadata dictionary.

    Args:
        filename (str): A string with the filename and extension.

    Returns:
        dataframe (pd.DataFrame): a pandas dataframe.
        meta (dict): a dictionary with the metadata for the NWIS data request, if it
        exists.
    """
    pa_table = pq.read_table(filename)
    dataframe = pa_table.to_pandas()
    dataframe.index.freq = calc_freq(dataframe.index)
    meta_dict = pa_table.schema.metadata
    if b"hydrofunctions_meta" in meta_dict:
        meta_string = meta_dict[b"hydrofunctions_meta"].decode()
        meta = json.loads(meta_string)
    else:
        meta = None
    return dataframe, meta


def save_parquet(filename, dataframe, hf_meta):
    """Save a hydrofunctions parquet file.

    This function will save a dataframe and a dictionary into the parquet format.
    Parquet files are a compact, easy to process format that work well with Pandas and
    large datasets. This function will accompany the dataframe with a dictionary of NWIS
    metadata that is produced by the hydrofunctions.extract_nwis_df() function. This
    file can then be read by the hydrofunctions.read_parquet() function.

    Args:
        filename (str): A string with the filename and extension.
        dataframe (pd.DataFrame): a pandas dataframe.
        hf_meta (dict): a dictionary with the metadata for the NWIS data request, if it
        exists.
    """
    if (len(filename.split('.'))==1):
        filename = filename + '.gz.parquet'

    table = pa.Table.from_pandas(dataframe, preserve_index=True)
    meta_dict = table.schema.metadata
    hf_string = json.dumps(hf_meta).encode()
    meta_dict[b"hydrofunctions_meta"] = hf_string
    table = table.replace_schema_metadata(meta_dict)
    pq.write_table(table, filename, compression="gzip")


def read_json_gzip(filename):
    """Read a gzipped JSON file into a Python dictionary

    Reads JSON files that have been zipped and returns a Python dictionary.
    Usually the files should have an extension *.json.gz
    Hydrofunctions uses this function to store the original JSON format WaterML
    response from the USGS NWIS.

    Args:
        filename (str): A string with the filename and extension.

    Returns:
        a dictionary of the file contents.
    """
    with gzip.open(filename, 'rb') as zip_file:
        zip_dict = json.loads(zip_file.read())
        return zip_dict


def save_json_gzip(filename, json_dict):
    """Save a Python dictionary as a gzipped JSON file.

    This save function is especially designed to compress and save the original
    JSON response from the USGS NWIS. If no file extension is specified, then a
    *.json.gz extension will be provided.

    Args:
        filename (str): A string with the filename and extension.
        json_dict (dict): A dictionary representing the json content.
    """
    if (len(filename.split('.'))==1):
        filename = filename + 'json.gz'

    with gzip.open(filename, 'wt', encoding="ascii") as zip_file:
       json.dump(json_dict, zip_file)