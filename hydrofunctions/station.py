"""
hydrofunctions.station
~~~~~~~~~~~~~~~~~~~~~~

This module contains the Station and NWIS classes, which are used for
organizing and managing data for data collection sites.

-----
"""
from __future__ import absolute_import, print_function, division, unicode_literals
import re

import json
import warnings
from . import hydrofunctions as hf
from . import helpers


class Station(object):
    """A class for organizing stream gauge data for a single request.
    """

    station_dict = {}

    def __init__(self, site=None):
        Station.station_dict[site] = self
        self.site = site
        # One option is to make it so that you can pass in a get_data function
        # during the creation of an instance.
        self.get_data = None


class NWIS(Station):
    """A class for working with data from the USGS NWIS service.

    description

    Args:
        site (str or list of strings):
            a valid site is '01585200' or ['01585200', '01646502']. Default is
            None. If site is not specified, you will need to select sites using
            stateCd or countyCd.

        service (str):
            can either be 'iv' or 'dv' for instantaneous or daily data.
            'dv'(default): daily values. Mean value for an entire day.
            'iv': instantaneous value measured at this time. Also known
            as 'Real-time data'. Can be measured as often as every
            five minutes by the USGS. 15 minutes is more typical.

        start_date (str):
           should take on the form 'yyyy-mm-dd'

        end_date (str):
            should take on the form 'yyyy-mm-dd'

        stateCd (str):
            a valid two-letter state postal abbreviation, such as 'MD'. Default
            is None. Selects all stations in this state. Because this type of
            site selection returns a large number of sites, you should limit
            the amount of data requested for each site.

        countyCd (str or list of strings):
            a valid county FIPS code. Default is None. Requests all stations
            within the county or list of counties. See https://en.wikipedia.org/wiki/FIPS_county_code
            for an explanation of FIPS codes.

        bBox (str, list, or tuple):
            a set of coordinates that defines a bounding box.
                * Coordinates are in decimal degrees.
                * Longitude values are negative (west of the prime meridian).
                * Latitude values are positive (north of the equator).
                * comma-delimited, no spaces, if provided as a string.
                * The order of the boundaries should be: "West,South,East,North"
                * Example: "-83.000000,36.500000,-81.000000,38.500000"

        parameterCd (str or list of strings):
            NWIS parameter code. Usually a five digit code. Default is 'all'.
            A valid code can also be given as a list: parameterCd=['00060','00065']
            This will request data for this parameter.

                * if value is 'all', or no value is submitted, then NWIS will \
                return every parameter collected at this site. (default option)
                * stage: '00065'
                * discharge: '00060'
                * not all sites collect all parameters!
                * See https://nwis.waterdata.usgs.gov/usa/nwis/pmcodes for full list

        period (str):
            NWIS period code. Default is None.
                * Format is "PxxD", where xx is the number of days before \
                today, with a maximum of 999 days accepted.
                * Either use start_date or period, but not both.


    """

    def __init__(
        self,
        site=None,
        service="dv",
        start_date=None,
        end_date=None,
        stateCd=None,
        countyCd=None,
        bBox=None,
        parameterCd="all",
        period=None,
        file=None,
    ):

        self.ok = False
        if file is not None:
            try:
                self._dataframe, self.meta = hf.read_parquet(file)
                self.ok = True
                print("Reading data from", file)

            except OSError as err:
                # File does not exist yet, we'll make it later.
                pass

        if self.ok == False:
            self.response = hf.get_nwis(
                site,
                service,
                start_date,
                end_date,
                stateCd=stateCd,
                countyCd=countyCd,
                bBox=bBox,
                parameterCd=parameterCd,
                period=period,
            )
            try:
                self.json = self.response.json()
                self._dataframe, self.meta = hf.extract_nwis_df(self.json)
                self.ok = self.response.ok
                if file is not None:
                    self.save(file)
                    print("Saving data to", file)
            except json.JSONDecodeError as err:
                self.ok = False
                print(f"JSON decoding error. URL: {self.response.url}")
                raise json.JSONDecodeError(err)

        # Can I get rid of this, and only keep metadata in the meta dict?
        if self.ok:
            self.site = site
            self.service = service
            self.start_date = start_date
            self.end_date = end_date
            self.start = self._dataframe.index.min()
            self.end = self._dataframe.index.max()

    def __repr__(self):
        repr_string = ""
        for site_id in sorted(self.meta.keys()):
            repr_string += site_id + ": " + self.meta[site_id]["siteName"] + "\n"
            for param in sorted(self.meta[site_id]["timeSeries"].keys()):
                repr_string += (
                    "    "
                    + param
                    + ": "
                    + self.meta[site_id]["timeSeries"][param]["variableFreq"]
                    + "  "
                    + self.meta[site_id]["timeSeries"][param]["variableDescription"]
                    + "\n"
                )
        repr_string += "Start: " + str(self.start) + "\n" + "End:   " + str(self.end)
        return repr_string

    def df(self, *args):
        """
        Return a subset of columns from the dataframe.

        Args:
            '': If no args are provided, the entire dataframe will be returned.

            str 'all': the entire dataframe will be returned.

            str 'data': all of the parameters will be returned, with no flags.

            str 'flags': Only the _qualifier flags will be returned. Unless the \
            flags arg is provided, only data columns will be returned. Visit \
            https://waterdata.usgs.gov/usa/nwis/uv?codes_help#dv_cd1 to see a \
            more complete listing of possible codes.

            str 'discharge' or 'q': discharge columns ('00060') will be returned.

            str 'stage': Gauge height columns ('00065') will be returned.

            int any five digit number: any matching parameter columns will be returned. '00065' returns stage, for example.

            int any eight to twelve digit number: any matching stations will be returned.
        """
        all_cols = self._dataframe.columns != ""  # all true
        no_cols = ~all_cols  # all false
        data_cols = self._dataframe.columns.str.contains(
            r"[0-9]$"
        )  # Data columns end in a number.
        flag_cols = self._dataframe.columns.str.contains("_qualifiers")
        Q_cols = self._dataframe.columns.str.contains(
            ":00060:"
        )  # This includes data & flags
        stage_cols = self._dataframe.columns.str.contains(":00065:")
        param_re = r"^\d{5}$"  # parameters are a five-digit number.
        station_re = r"\d{8,12}$"  # station ID's are between 8 and 12 digits.

        sites = no_cols
        params = no_cols
        meta = no_cols
        if len(args) == 0:  # If no args are given, return every column.
            sites = all_cols
            params = all_cols
            meta = all_cols
        else:
            for item in args:
                if item == "all":
                    sites = all_cols
                    params = all_cols
                    meta = all_cols
                    break  # If one param is 'all', ignore the other params and deliver everything.
                elif item == "discharge":
                    params = Q_cols | params
                elif item == "q":
                    params = Q_cols | params
                elif item == "stage":
                    params = stage_cols | params
                elif item == "data":
                    meta = data_cols | meta
                elif item == "flags":
                    meta = flag_cols | meta
                elif re.search(param_re, item):
                    param_arg = ":" + item + ":"
                    params = self._dataframe.columns.str.contains(param_arg) | params
                    if not params.any():
                        raise ValueError(
                            "The parameter '{param}' is not contained in this dataset.".format(
                                param=item
                            )
                        )
                elif re.search(station_re, item):
                    station_arg = ":" + item + ":"
                    sites = self._dataframe.columns.str.contains(station_arg) | sites
                    if not sites.any():
                        raise ValueError(
                            "The site '{site}' is not in this dataset.".format(
                                site=item
                            )
                        )
                else:
                    raise ValueError(
                        "The argument '{item}' is not recognized.".format(item=item)
                    )
        if not sites.any():  # If no sites are selected, select them all.
            sites = all_cols
        if not params.any():  # If no params are selected, select them all.
            params = all_cols
        if (
            not meta.any()
        ):  # If neither flags nor data are selected, select data columns.
            meta = data_cols
        selection = sites & params & meta
        requested_df = self._dataframe.loc[:, selection]
        return requested_df

    def get_data(self):
        warnings.warn(
            "It is no longer necessary to call .get_data() to request data.",
            FutureWarning,
        )
        return self

    def save(self, file):
        """
        Save the dataframe and metadata to a parquet file.

        Args:
            file (str):
                the filename to save to.
        """
        hf.save_parquet(file, self._dataframe, self.meta)
        return self

    def read(self, file):
        """
        Read a dataframe and metadata from a parquet file.

        Args:
            file (str):
                the filename to read from.
        """
        self._dataframe, self.meta = hf.read_parquet(file)
        return self
