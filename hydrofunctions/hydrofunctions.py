# -*- coding: utf-8 -*-
"""
hydrofunctions.py

This module contains the main functions used in an interactive session.
"""
from __future__ import absolute_import, print_function
import requests
import numpy as np
import pandas as pd
# Change to relative import: from . import exceptions
# https://axialcorps.com/2013/08/29/5-simple-rules-for-building-great-python-packages/
from . import exceptions
from . import typing


def get_nwis(site, service, start_date, end_date, stateCd=None, countyCd=None,
             parameterCd='00060'):
    """Request stream gauge data from the USGS NWIS.

    Args:
        site (str or list of strings):
            a valid site is '01585200' or ['01585200', '01646502']. site
            should be None if stateCd or countyCd are not None.

        service (str):
            can either be 'iv' or 'dv' for instantaneous or daily data.

        start_date (str):
           should take on the form yyyy-mm-dd

        end_date (str):
            should take on the form yyyy-mm-dd

        stateCd (str):
            a valid two-letter state postal abbreviation. Default is None.

        countyCd (str or list of strings):
            a valid county abbreviation. Default is None.

        parameterCd (str):
            NWIS parameter code. Default is stream discharge '00060'
                * stage: '00065'
                * discharge: '00060'
                * not all sites collect all parameters!
                * See https://nwis.waterdata.usgs.gov/usa/nwis/pmcodes for \
                full list

    Returns:
        a response object.

            * response.url: the url we requested data from.
            * response.status_code: '200' when okay; see \
            <https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html>
            * response.json: the content translated as json.
            * response.ok: "True" when we get a '200'

    Raises:
        ConnectionError
            due to connection problems like refused connection
            or DNS Error.

        HydroNoDataError
            when NWIS returns a response code that is not 200.

    Example::

        >>> import hydrofunctions as hf
        >>> response = hf.get_nwis('01585200', 'dv', '2012-06-01', '2012-07-01')

        >>> response
        <response [200]>
        >>> response.ok
        True
        >>> response.json()
        *JSON ensues*

    The specification for the USGS NWIS service is located here:
    http://waterservices.usgs.gov/rest/IV-Service.html
    """

    header = {
        'Accept-encoding': 'gzip',
        'max-age': '120'
        }

    values = {
        'format': 'json,1.1',
        # 'sites': sites,
        # default parameterCd represents stream discharge.
        'parameterCd': parameterCd,
        # This is the format for requesting 10 days of data before today.
        # 'period': 'P10D',
        'startDT': start_date,
        'endDT': end_date
        }

    # process sites, stateCd, or countyCd options
    if stateCd is None and countyCd is None:
        sites = typing.check_NWIS_site(site)
        values['sites'] = sites
    elif stateCd is not None:
        values['stateCd'] = stateCd
    elif countyCd is not None:
        countyCd = typing.check_NWIS_site(countyCd)
        values['countyCd'] = countyCd

    url = 'http://waterservices.usgs.gov/nwis/'
    url = url + service + '/?'
    response = requests.get(url, params=values, headers=header)
    # requests will raise a 'ConnectionError' if the connection is refused
    # or if we are disconnected from the internet.
    # I think that is appropriate, so I don't want to handle this error.

    # This function will always return the response. Higher-level code
    # That calls this function may decide how to handle or report 
    # status codes that indicate something went wrong.
    # Error codes are from: https://waterservices.usgs.gov/docs/portable_code.html
    if response.status_code == 200:
        return response
    else:
        print("The NWIS returned a code of {}.".format(response.status_code))
        return response


def extract_nwis_dict(response_obj):
    """Returns a dict object from an NWIS response object.

    Args:
        response_obj (obj):
            a response object as returned by get_nwis().

    Returns:
        a dict formed from the response.json()
    """
    nwis_dict = response_obj.json()

    return nwis_dict


def extract_nwis_df(response_obj):
    """Returns a Pandas dataframe from an NWIS response object.

    Args:
        response_obj (obj):
            a response object as returned by get_nwis().

    Returns:
        a pandas dataframe.

    Raises:
        HydroNoDataError  when the request is valid, but NWIS has no data for
            the parameters provided in the request.
    """
    nwis_dict = response_obj.json()

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

        # TODO: this if clause needs to be tested.
        raise exceptions.HydroNoDataError("The NWIS reports that it does not"
                                          " have any data for this request.")

    # create lists of timeseries keys, names, and noDataValues
    keys = []
    names = []
    noDataValues = []
    for idx, tts in enumerate(ts):
        keys.append(idx)
        tag = tts['name'].split(':')[1]
        tag += ' - '
        try:
            tag += tts['variable']['options']['option'][0]['value']
        # TODO: either list specific exceptions that we can fix, or remove this
        # except clause.
        except:
            pass
        tag += ' ' + tts['variable']['variableDescription']
        names.append(tag)
        ndv = tts['variable']['noDataValue']
        if ndv not in noDataValues:
            noDataValues.append(ndv)

    # determine the NWIS data item with the maximum amount of data so that
    # it can be processed first
    idxmx = 0
    emax = 0
    for idx, key in enumerate(keys):
        data = nwis_dict['value']['timeSeries'][key]['values'][0]['value']
        if len(data) > emax:
            emax = len(data)
            idxmx = idx

    # process data for the first NWIS site
    data = nwis_dict['value']['timeSeries'][idxmx]['values'][0]['value']
    DF = pd.DataFrame(data, columns=['dateTime', 'value'])
    DF.index = pd.to_datetime(DF.pop('dateTime'))
    DF = DF.rename(columns={'value': names[idxmx]})
    DF[names[idxmx]] = DF[names[idxmx]].astype(float)

    # set index name for dataframe
    DF.index.name = 'datetime'

    # process data for the remaining NWIS sites
    for key in keys:
        # skip data processing if key has already been processed
        if key == idxmx:
            continue
        da = nwis_dict['value']['timeSeries'][key]['values'][0]['value']
        dfa = pd.DataFrame(da, columns=['dateTime', 'value'])
        dfa.index = pd.to_datetime(dfa.pop('dateTime'))
        dfa = dfa.rename(columns={'value': names[key]})
        DF = pd.concat([DF, dfa], axis=1)
        DF[names[key]] = DF[names[key]].astype(float)

    # replace missing values in the dataframe
    DF = DF.replace(to_replace=noDataValues, value=np.nan)

    return DF


def handle_status_code(response):
    if response.status_code == 200:
        return response
    # All other status codes will raise an Exception.
    elif response.status_code == 400:
        raise exceptions.HydroNoDataError("The NWIS returned a code "
                                          "of {}. Description: ".format(response.status_code)
                                          + "400 Bad Request - This often occurs if the URL arguments "
                                          "are inconsistent, for example in the instantaneous values "
                                          "service using startDT and endDT with the period argument. An "
                                          "accompanying error should describe why the request was "
                                          "bad."
                                          # Error value will be reported in response.reason
                                          + "NWIS error value: {}".format(response.reason)
                                          )

    elif response.status_code == 403:
        raise exceptions.HydroNoDataError("The NWIS service returned a code "
                                          "of {}. Description: ".format(response.status_code)
                                          + "403 Access Forbidden - This "
                                          "should only occur if for some reason"
                                          "the USGS has blocked your Internet Protocol (IP) address from using the service. This can happen if we believe that your use of the service is so excessive that it is seriously impacting others using the service. To get unblocked, send us the URL you are using along with the IP using this form. We may require changes to your query and frequency of use in order to give you access to the service again.")

    elif response.status_code == 404:
        raise exceptions.HydroNoDataError("The NWIS service returned a code "
                                          "of {}. Description: ".format(response.status_code)
                                          + "404 Not Found - Returned if and only if the query expresses a combination of elements where data do not exist. For multi-site queries, if any data are found, it is returned for those site/parameters/date ranges where there are data.")

    elif response.status_code == 500:
        raise exceptions.HydroNoDataError("The NWIS service returned a code "
                                          "of {}. Description: ".format(response.status_code)
                                          + "500 Internal Server Error - If you see this, it means there is a problem with the web service itself. It usually means the application server is down unexpectedly. This could be caused by a host of conditions but changing your query will not solve this problem. The application support team has to fix it. Most of these errors are quickly detected and the support team is notified if they occur.")
    elif response.status_code == 503:
        raise exceptions.HydroNoDataError("The NWIS service returned a code "
                                          "of {}. Description: ".format(response.status_code)
                                          + "503 Service Unavailable - The application server is working but this application is down at the moment. When something causes this to happen, the support team should be quickly notified. Hopefully the service will be available shortly.")
    else:
        raise exceptions.HydroNoDataError("The NWIS service returned a code "
                                          "of {}. Description: ".format(response.status_code))
