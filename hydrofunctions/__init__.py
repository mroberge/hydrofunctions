# -*- coding: utf-8 -*-

"""
Hydrofunctions
~~~~~~~~~~~~~~

Hydrofunctions is a suite of convenience functions to help you explore
Hydrology data interactively.

Basic Usage::

    >>> import hydrofunctions as hf

    >>> site = '01582500'
    >>> start = '2015-05-10'
    >>> end = '2015-05-15'
    >>> response = hf.get_nwis(site, 'dv', start, end)

Examine the response object::

    >>> response.ok
    True

    >>> response.status_code
    200

    >>> response.text
    '{"name":"ns1:timeSeriesResponseType","declaredType":"org.cuahsi.waterml.TimeSeriesResponseType" .... }

List all of the different attributes and methods with dir()::

    >>> dir(response)

Read more about Hydrofunctions here: https://hydrofunctions.readthedocs.io/

"""

__title__ = 'hydrofunctions'
__version__ = '0.1.5'
__author__ = 'Martin Roberge'
__email__ = 'mroberge.whois@gmail.com'
__license__ = 'MIT'
__copyright__ = 'Copyright 2016 Martin Roberge and contributors'




from .exceptions import HydroNoDataError
from .hydrofunctions import (
        get_nwis, extract_nwis_df, nwis_custom_status_codes
        )
from .station import Station, NWIS
from .typing import (
        check_NWIS_site, check_datestr, check_NWIS_service, check_period
        )
