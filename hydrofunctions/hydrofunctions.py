# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import requests
from hydrofunctions import exceptions


def first():
    print("This is the first function.")
    return True


def raiseit():
    raise exceptions.HydroNoDataError


def get_nwis(site, service, start_date, end_date):
    """
    request stream gauge data from the USGS NWIS.

    Parameters
    ----------
    site: string
        a valid site is 01585200
    service: string
        can either be 'iv' or 'dv' for instantaneous or daily data.
    start_date: string
       should take on the form yyyy-mm-dd
    end_date: string
        should take on the form yyyy-mm-dd

    Returns
    -------
    a response object.
        response.url: the url we requested data from.
        response.status_code:
        response.json: the content translated as json
        response.ok: "True" when we get a '200'

    Raises
    ------
    ConnectionError  due to connection problems like refused connection or DNS

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


