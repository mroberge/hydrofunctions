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
    compose a data request object for the USGS NWIS,
    send it to make_request(),
    then deal with the returned error or json.

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
    the json response

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
    return response

"""
    data = urllib.parse.urlencode(values)  # data is a string now. don't encode
    url = 'http://waterservices.usgs.gov/nwis/'
    url = url + service + '/?' + data
    req = urllib.request.Request(url, headers=header)

    return req
"""
