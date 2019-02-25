# -*- coding: utf-8 -*-
"""
hydrofunctions.py

This module contains the main functions used in an interactive session.
"""
from __future__ import absolute_import, print_function, division, unicode_literals
import requests
import numpy as np
import pandas as pd
# Change to relative import: from . import exceptions
# https://axialcorps.com/2013/08/29/5-simple-rules-for-building-great-python-packages/
from . import exceptions
import warnings
from . import typing
from . import helpers


def select_data(nwis_df):
    """Create a boolean array of columns that contain data.

    Args:
        nwis_df:
            A pandas dataframe created by extract_nwis_df.

    Returns:
        an array of Boolean values corresponding to the columns in the
        original dataframe.

    Example:
        >>> my_dataframe[:, select_data(my_dataframe)]

        returns a dataframe with only the data columns; the qualifier columns
        do not show.
    """
    data_regex = r'[0-9]$'
    return nwis_df.columns.str.contains(data_regex)


def calc_freq(index):
    if (isinstance(index, pd.DataFrame)):
        index = index.index
    try:
        # Try the direct approach first.
        freq = index.freq
    except AttributeError:
        freq = None

    if freq is None:
        try:
            # Second attempt using built-in. I've crashed this before, so
            # let's catch exceptions.
            freq = pd.infer_freq(index)
        except ValueError:
            pass

    if freq is None:
        freq = (index.max() - index.min())/len(index)
        if pd.Timedelta('13 minutes') < freq < pd.Timedelta('17minutes'):
            freq = pd.Timedelta('15 minutes')
        else:
            freq = None

    if freq is None:
        freq = index[2] - index[3]

    if freq is None:
        warnings.warn("It is not possible to determine the frequency"
                      "for one of the datasets in this request."
                      "This dataset will be set to a frequency of "
                      "15 minutes", exceptions.HydroUserWarning)
        freq = '15T'

    return freq


def get_nwis(site, service='dv', start_date=None, end_date=None, stateCd=None,
             countyCd=None, bBox=None, parameterCd='all', period=None):
    """Request stream gauge data from the USGS NWIS.

    Args:
        site (str or list of strings):
            a valid site is '01585200' or ['01585200', '01646502']. site
            should be None if stateCd or countyCd are not None.

        service (str):
            can either be 'iv' or 'dv' for instantaneous or daily data.
            'dv'(default): daily values. Mean value for an entire day.
            'iv': instantaneous value measured at this time. Also known
            as 'Real-time data'. Can be measured as often as every
            five minutes by the USGS. 15 minutes is more typical.

        start_date (str):
           should take on the form yyyy-mm-dd

        end_date (str):
            should take on the form yyyy-mm-dd

        stateCd (str):
            a valid two-letter state postal abbreviation. Default is None.

        countyCd (str or list of strings):
            a valid county abbreviation. Default is None.

        bBox (str, list, or tuple):
            a set of coordinates that defines a bounding box.
                * Coordinates are in decimal degrees
                * Longitude values are negative (west of the prime meridian).
                * Latitude values are positive (north of the equator).
                * comma-delimited, no spaces, if provided as a string.
                * The order of the boundaries should be: "West,South,East,North"
                * Example: "-83.000000,36.500000,-81.000000,38.500000"

        parameterCd (str or list of strings):
            NWIS parameter code. Usually a five digit code. Default is 'all'.
            A valid code can also be given as a list: parameterCd=['00060','00065']
                * if value of 'all' is submitted, then NWIS will return every \
                parameter collected at this site. (default option)
                * stage: '00065'
                * discharge: '00060'
                * not all sites collect all parameters!
                * See https://nwis.waterdata.usgs.gov/usa/nwis/pmcodes for full list

        period (str):
            NWIS period code. Default is None.
                * Format is "PxxD", where xx is the number of days before \
                today, with a maximum of 999 days accepted.
                * Either use start_date or period, but not both.

    Returns:
        a response object. This function will always return the response,
            even if the NWIS returns a status_code that indicates a problem.

            * response.url: the url we used to request data
            * response.status_code: '200' when okay; see <https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html>
            * response.json: the content translated as json
            * response.status_code: the internet status code
                - '200': is a good request
                - non-200 codes will be reported as a warning.
                - '400': is a 'Bad Request'-- the parameters did not make sense
            * response.ok: "True" when we get a '200' status_code

    Raises:
        ConnectionError: due to connection problems like refused connection
            or DNS Error.

        SyntaxWarning: when NWIS returns a response code that is not 200.

    Example::

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

    if (parameterCd == 'all'):
        parameterCd = None

    header = {
        'Accept-encoding': 'gzip',
        'max-age': '120'
    }

    values = {
        # specify version of nwis json. Based on WaterML1.1
        # json,1.1 works; json%2C works; json1.1 DOES NOT WORK
        'format': 'json,1.1',
        'sites': typing.check_parameter_string(site, 'site'),
        'stateCd': stateCd,
        'countyCd': typing.check_parameter_string(countyCd, 'county'),
        'bBox': typing.check_NWIS_bBox(bBox),
        'parameterCd': typing.check_parameter_string(parameterCd, 'parameterCd'),
        'period': period,
        'startDT': start_date,
        'endDT': end_date
    }

    # Check that site selection parameters are exclusive!
    total = helpers.count_number_of_truthy([site, stateCd, countyCd, bBox])
    if total == 1:
        pass
    elif (total > 1):
        raise ValueError("Select sites using either site, stateCd, "
                         "countyCd, or bBox, but not more than one.")
    elif (total < 1):
        raise ValueError("Select sites using at least one of the following"
                         " arguments: site, stateCd, countyCd or bBox.")

    # Check that time parameters are not both set.
    # If neither is set, then NWIS will return the most recent observation.
    if (start_date and period):
        raise ValueError("Use either start_date or period, or neither, "
                         "but not both.")

    url = 'https://waterservices.usgs.gov/nwis/'
    url = url + service + '/?'
    response = requests.get(url, params=values, headers=header)
    # requests will raise a 'ConnectionError' if the connection is refused
    # or if we are disconnected from the internet.

    # .get_nwis() will always return the response.

    # Higher-level code that calls get_nwis() may decide to handle or
    # report status codes that indicate something went wrong.

    # Issue warnings for bad status codes
    nwis_custom_status_codes(response)

    return response


def get_nwis_property(nwis_dict, key=None, remove_duplicates=False):
    """Returns a list containing property data from an NWIS response object.

    Args:
        nwis_dict (dict):
            the json returned in a response object as produced by get_nwis().json().

        key (str):
            a valid NWIS response property key. Default is None. The index is \
            returned if key is None. Valid keys are:
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
        HydroNoDataError  when the request is valid, but NWIS has no data for
            the parameters provided in the request.

        ValueError when the key is not available in
    """
    #nwis_dict = response_obj.json()

    # strip header and all metadata. ts is the 'timeSeries' element of the
    # response; it is an array of objects that contain time series data.
    ts = nwis_dict['value']['timeSeries']
    msg = 'The NWIS reports that it does not' + \
          ' have any data for this request.'
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
    sourceInfo = ['siteName', 'siteCode', 'timeZoneInfo', 'geoLocation',
                  'siteType', 'siteProperty']
    variable = ['variableCode', 'variableName', 'variableDescription',
                'valueType', 'unit', 'options', 'noDataValue']
    root = ['name']
    vals = []
    try:
        for idx, tts in enumerate(ts):
            d = tts['values'][0]['value']
            # skip stations with no data
            if len(d) < 1:
                continue
            if key in variable:
                v = tts['variable'][key]
            elif key in sourceInfo:
                v = tts['sourceInfo'][key]
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
    """Returns a Pandas dataframe from an NWIS response object.

    Args:
        nwis_dict (obj):
            the json from a response object as returned by get_nwis().json().

    Returns:
        a pandas dataframe.

    Raises:
        HydroNoDataError  when the request is valid, but NWIS has no data for
            the parameters provided in the request.

        HydroUserWarning  when one dataset is at a lower frequency than another
            dataset in the same request.
    """
    if type(nwis_dict) is not dict:
        nwis_dict = nwis_dict.json()

    # strip header and all metadata.
    ts = nwis_dict['value']['timeSeries']
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

        raise exceptions.HydroNoDataError("The NWIS reports that it does not"
                                          " have any data for this request.")

    # create a list of time series;
    # set the index, set the data types, replace NaNs, sort, find the first and last

    collection = []
    starts = []
    ends = []
    freqs = []
    for series in ts:
        series_name = series['name']
        noDataValues = series['variable']['noDataValue']
        data = series['values'][0]['value']
        if data == []:
            # This parameter has no data. Skip to next series.
            continue
        qualifiers = series_name + "_qualifiers"
        DF = pd.DataFrame(data=data)
        DF.index = pd.to_datetime(DF.pop('dateTime'), utc=True)
        DF['value'] = DF['value'].astype(float)
        DF = DF.replace(to_replace=noDataValues, value=np.nan)
        DF['qualifiers'] = DF['qualifiers'].apply(lambda x: ','.join(x))
        DF.rename(columns={'qualifiers': qualifiers, 'value': series_name}, inplace=True)
        DF.sort_index(inplace=True)
        local_start = DF.index.min()
        local_end = DF.index.max()
        starts.append(local_start)
        ends.append(local_end)
        local_freq = calc_freq(DF.index)
        freqs.append(local_freq)
        local_clean_index = pd.date_range(start=local_start, end=local_end, freq=local_freq)

        DF = DF.reindex(index=local_clean_index, copy=True)
        qual_cols = DF.columns.str.contains('_qualifiers')
        # https://stackoverflow.com/questions/21998354/pandas-wont-fillna-inplace
        # Instead, create a temporary dataframe, fillna, then copy back into original.
        DFquals = DF.loc[:, qual_cols].fillna("hf.missing")
        DF.loc[:, qual_cols] = DFquals

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
        raise exceptions.HydroNoDataError("The NWIS does not have any data for"
                                          " the requested combination of sites"
                                          ", parameters, and dates.")
    startmin = min(starts)
    endmax = max(ends)
    freqmin = min(freqs)
    freqmax = max(freqs)
    if (freqmin != freqmax):
        warnings.warn("One or more datasets in this request is going to be "
                      "'upsampled' to " + str(freqmin) + " because the data "
                      "were collected at a lower frequency of " + str(freqmax),
                      exceptions.HydroUserWarning)
    clean_index = pd.date_range(start=startmin, end=endmax, freq=freqmin)
    cleanDF = pd.DataFrame(index=clean_index)
    for dataset in collection:
        cleanDF = pd.concat([cleanDF, dataset], axis=1)
    cleanDF.index.name = 'datetime'
    # Replace lines with missing _qualifier flags with hf.upsampled
    qual_cols = cleanDF.columns.str.contains('_qualifiers')
    cleanDFquals = cleanDF.loc[:, qual_cols].fillna('hf.upsampled')
    cleanDF.loc[:, qual_cols] = cleanDFquals

    if interpolate:
        #TODO: mark interpolated values with 'hf.interp'

        #select data, then replace Nans with interpolated values.
        data_cols = cleanDF.columns.str.contains(r'[0-9]$')
        cleanDFdata = cleanDF.loc[:,data_cols].interpolate()
        cleanDF.loc[:,data_cols] = cleanDFdata

    if (not DF.index.is_unique):
        DF = DF[~DF.index.duplicated(keep='first')]
    if (not DF.index.is_monotonic):
        DF.sort_index(axis=0, inplace=True)

    return cleanDF


def nwis_custom_status_codes(response):
    """
    Raise custom warning messages from the NWIS when it returns a
    status_code that is not 200.

    Args:
        response: a response object as returned by get_nwis().

    Returns:
        None: if response.status_code == 200
        response.status_code: for all other status codes.

    Raises:
        SyntaxWarning: when a non-200 status code is returned.
            https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

    Note:
        To raise an exception, call `response.raise_for_status()`
        This will raise requests.exceptions.HTTPError with a helpful message
        or it will return None for status code 200.
        From: http://docs.python-requests.org/en/master/user/quickstart/#response-status-codes

        NWIS status_code messages come from:
            https://waterservices.usgs.gov/docs/portable_code.html
        Additional status code documentation:
            https://waterservices.usgs.gov/rest/IV-Service.html#Error
    """
    nwis_msg = {
        '200': 'OK',
        '400': "400 Bad Request - "
               "This often occurs if the URL arguments "
               "are inconsistent, for example in the instantaneous values "
               "service using startDT and endDT with the period argument. "
               "An accompanying error should describe why the request was "
               "bad."
               + "\nError message from NWIS: {}".format(response.reason),
        '403': "403 Access Forbidden - "
               "This should only occur if for some reason the USGS has "
               "blocked your Internet Protocol (IP) address from using "
               "the service. This can happen if we believe that your use "
               "of the service is so excessive that it is seriously "
               "impacting others using the service. To get unblocked, "
               "send us the URL you are using along with the IP using "
               "this form. We may require changes to your query and "
               "frequency of use in order to give you access to the "
               "service again.",
        '404': "404 Not Found - "
               "Returned if and only if the query expresses a combination "
               "of elements where data do not exist. For multi-site "
               "queries, if any data are found, it is returned for those "
               "site/parameters/date ranges where there are data.",
        '503': "500 Internal Server Error - "
               "If you see this, it means there is a problem with the web "
               "service itself. It usually means the application server "
               "is down unexpectedly. This could be caused by a host of "
               "conditions but changing your query will not solve this "
               "problem. The application support team has to fix it. Most "
               "of these errors are quickly detected and the support team "
               "is notified if they occur."
    }
    if response.status_code == 200:
        return None
    # All other status codes will raise a warning.
    else:
        # Use the status_code as a key, return None if key not in dict
        msg = "The NWIS returned a code of {}.\n".format(response.status_code) \
              + nwis_msg.get(str(response.status_code)) \
              + "\n\nURL used in this request: {}".format(response.url)

        # Warnings will not beak the flow. They just print a message.
        # However, they are often supressed in some applications.
        warnings.warn(msg, SyntaxWarning)
        return response.status_code
