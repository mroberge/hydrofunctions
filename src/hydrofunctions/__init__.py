# -*- coding: utf-8 -*-

"""
Hydrofunctions
~~~~~~~~~~~~~~

Hydrofunctions is a suite of convenience functions to help you explore
hydrology data interactively.

Basic Usage::

    >>> import hydrofunctions as hf

    >>> site = '01570500'
    >>> harrisburg = hf.NWIS(site, 'iv', period='P10D')
    Requested data from https://waterservices.usgs.gov/nwis/iv/?format=json%2C1.1&sites=01570500&period=P10D

    >>> harrisburg.ok
    True

Examine the dataset::

    >>> harrisburg
    USGS:01570500: Susquehanna River at Harrisburg, PA
        00045: <30 * Minutes> Precipitation, total, inches
        00060: <30 * Minutes> Discharge, cubic feet per second
        00065: <30 * Minutes> Gage height, feet
    Start: 2019-04-06 00:30:00+00:00
    End:   2019-04-15 23:00:00+00:00

The listing reports each of the parameters collected at the site that was
requested, how frequently the data are collected, and the name of the parameter
written out with units. The start and end of the dataset are given in Universal
Time (UTC).

View the first five rows of a dataframe that only contains the discharge data::

    >>> harrisburg.df('discharge').head()
                               USGS:01570500:00060:00000
    datetimeUTC
    2019-04-06 00:30:00+00:00                    44200.0
    2019-04-06 01:00:00+00:00                    44000.0
    2019-04-06 01:30:00+00:00                    44000.0
    2019-04-06 02:00:00+00:00                    43700.0
    2019-04-06 02:30:00+00:00                    43700.0

Because the .df() method returns a dataframe, you have access to all of the
methods associated with Pandas, including .plot(), .describe(), and .info() !

Learn more about hydrofunctions and the NWIS object with help()::

    >>> help(hf)
    >>> help(hf.NWIS)

Read more about Hydrofunctions here: https://hydrofunctions.readthedocs.io/

"""
from __future__ import absolute_import, print_function
import importlib.metadata
__version__ = importlib.metadata.version('hydrofunctions')
__author__ = "Martin Roberge"
__author_email__ = "mroberge@towson.edu"
__url__ = "https://github.com/mroberge/hydrofunctions"

from .exceptions import (
    HydroNoDataError,
    HydroUserWarning,
)
from .hydrofunctions import (
    get_nwis,
    select_data,
    extract_nwis_df,
    nwis_custom_status_codes,
    get_nwis_property,
    calc_freq,
    read_parquet,
    save_parquet,
    read_json_gzip,
    save_json_gzip,
)
from .logging import _start_logging
from .station import Station, NWIS
from .validate import (
    check_parameter_string,
    check_datestr,
    check_NWIS_service,
    check_NWIS_bBox,
    check_period,
)
from .helpers import (
    draw_map,
    count_number_of_truthy,
)
from .charts import (
    flow_duration,
    cycleplot,
)
from .usgs_rdb import (
    get_usgs_RDB_service,
    read_rdb,
    site_file,
    data_catalog,
    field_meas,
    rating_curve,
    peaks,
    stats,
    hydroRDB,
)
from .waterwatch import (
    filter_flood_stages,
    get_flood_stage,
)
