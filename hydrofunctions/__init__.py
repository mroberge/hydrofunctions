# -*- coding: utf-8 -*-

"""
Hydrofunctions
~~~~~~~~~~~~~~

Hydrofunctions is a suite of convenience functions to help you explore
hydrology data interactively.

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
from __future__ import absolute_import, print_function

__title__ = 'hydrofunctions'
__version__ = '0.1.8dev'
__author__ = 'Martin Roberge'
__email__ = 'mroberge.whois@gmail.com'
__license__ = 'MIT'
__copyright__ = 'Copyright 2016 Martin Roberge and contributors'


from .exceptions import (
        HydroNoDataError,
        HydroUserWarning
        )
from .hydrofunctions import (
        get_nwis,
        select_data,
        extract_nwis_df,
        nwis_custom_status_codes,
        get_nwis_property,
        calc_freq
        )
from .station import Station, NWIS
from .typing import (
        check_parameter_string, check_datestr, check_NWIS_service, check_NWIS_bBox,
        check_period
        )
from .helpers import (
        draw_map,
        count_number_of_truthy
        )
from .charts import (
        flow_duration,
        cycleplot
        )
from .usgs_rdb import (
        read_rdb,
        field_meas,
        rating_curve
        )
