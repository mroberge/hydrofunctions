"""
Hydrofunctions
~~~~~~~~~~~~~~

Hydrofunctions is a suite of convenience functions to help you explore
hydrology data interactively.

Basic Usage::

    >>> import hydrofunctions as hf

    >>> site = '01589440'
    >>> jones = hf.NWIS(site, 'iv', period='P10D')
    Requested data from https://waterservices.usgs.gov/nwis/iv/?format=json%2C1.1&sites=01589440&period=P10D

Examine the dataset::

    >>> jones
    USGS:01589440: JONES FALLS AT SORRENTO, MD
        00060: <15 * Minutes> Discharge, cubic feet per second
        00065: <15 * Minutes> Gage height, feet
    Start: 2022-10-27 17:30:00+00:00
    End:   2022-11-06 17:15:00+00:00

The listing reports each of the parameters collected at the site that was
requested, how frequently the data are collected, and the name of the parameter
written out with units. The start and end of the dataset are given in Universal
Time (UTC).

View the first five rows of a dataframe that only contains the discharge data::

    >>> jones.df('discharge').head()
                               USGS:01589440:00060:00000
    datetimeUTC
    2022-10-27 17:30:00+00:00                    14.6
    2022-10-27 17:45:00+00:00                    15.2
    2022-10-27 18:00:00+00:00                    15.2
    2022-10-27 18:15:00+00:00                    15.8
    2022-10-27 18:30:00+00:00                    16.4

Because the .df() method returns a dataframe, you have access to all of the
methods associated with Pandas, including .plot(), .describe(), and .info() !

Learn more about hydrofunctions and the NWIS object with help()::

    >>> help(hf)
    >>> help(hf.NWIS)

Read more about Hydrofunctions here: https://hydrofunctions.readthedocs.io/

"""
__version__ = "0.2.4"
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
