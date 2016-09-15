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
from hydrofunctions import exceptions


def get_nwis(site, service, start_date, end_date):
    """Request stream gauge data from the USGS NWIS.

    Args:
        site (str):
            a valid site is 01585200
        service (str):
            can either be 'iv' or 'dv' for instantaneous or daily data.
        start_date (str):
           should take on the form yyyy-mm-dd
        end_date (str):
            should take on the form yyyy-mm-dd

    Returns:
        a response object.

            * response.url: the url we requested data from.
            * response.status_code:
            * response.json: the content translated as json
            * response.ok: "True" when we get a '200'

    Raises:
        ConnectionError  due to connection problems like refused connection
        or DNS Error.

    Example::

        >>> from hydrofunctions import hydrofunctions as hf
        >>> response = hf.get_nwis('01585200', 'dv', '2012-06-01', '2012-07-01')

        >>> response
        <respones [200]>
        >>> response.ok
        True
        >>> response.json()
        *JSON ensues*

    The specification for this service is located here:
    http://waterservices.usgs.gov/rest/IV-Service.html
    """

    header = {
        'Accept-encoding': 'gzip',
        'max-age': '120'
        }

    values = {
        'format': 'json,1.1',
        'sites': site,
        'parameterCd': '00060',  # represents stream discharge.
        # 'period': 'P10D' # This is the format for requesting data for a period before today
        'startDT': start_date,
        'endDT': end_date
        }

    url = 'http://waterservices.usgs.gov/nwis/'
    url = url + service + '/?'
    response = requests.get(url, params=values, headers=header)
    # requests will raise a 'ConnectionError' if the connection is refused
    # or if we are disconnected from the internet.
    # I think that is appropriate, so I don't want to handle this error.

    # TODO: where should all unhelpful ('404' etc) responses be handled?
    return response


def extract_nwis_dict(response_obj):
    """Returns a dict object from an NWIS response object.
    """
    nwis_dict = response_obj.json()

    return nwis_dict


def extract_nwis_df(response_obj):
    """Returns a Pandas dataframe from an NWIS response object.

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
        raise exceptions.HydroNoDataError("The NWIS reports that it does not \
                                            have any data for this request.")

    data = nwis_dict['value']['timeSeries'][0]['values'][0]['value']

    DF = pd.DataFrame(data, columns=['dateTime', 'value'])
    DF.index = pd.to_datetime(DF.pop('dateTime'))
    DF.value = DF.value.astype(float)
    # DF.index.name = None
    DF.index.name = 'datetime'
    DF.replace(to_replace='-999999', value=np.nan)

    return DF
