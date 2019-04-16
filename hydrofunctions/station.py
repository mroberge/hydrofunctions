# -*- coding: utf-8 -*-

"""
hydrofunctions.station
~~~~~~~~~~~~~~~~~~~~~~

This module contains the Station and NWIS classes, which are used for
organizing and managing data for data collection sites.

-----
"""
from __future__ import absolute_import, print_function, division, unicode_literals
import re
from . import typing
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

    def __init__(self,
                 site=None,
                 service='dv',
                 start_date=None,
                 end_date=None,
                 stateCd=None,
                 countyCd=None,
                 bBox=None,
                 parameterCd='all',
                 period=None):

        self.response = hf.get_nwis(site,
                                    service,
                                    start_date,
                                    end_date,
                                    stateCd=stateCd,
                                    countyCd=countyCd,
                                    bBox=bBox,
                                    parameterCd=parameterCd,
                                    period=period
                                    )
        self.ok = self.response.ok
        self.url = self.response.url
        self.json = self.response.json()

        self.siteName = hf.get_nwis_property(self.json,
                                             key='siteName',
                                             remove_duplicates=True)
        self.name = hf.get_nwis_property(self.json,
                                         key='name',
                                         remove_duplicates=True)

        self._dataframe, self.meta = hf.extract_nwis_df(self.json)
        #value = hf.get_nwis_property(self.json, key='siteCode', remove_duplicates=True)
        #sites = []
        #for site in value:
        #    site_id = site[0]['value']
        #    sites.append(site_id)
        self.site = site
        self.service = service
        self.start_date = start_date
        self.end_date = end_date
        self.start = self._dataframe.index.min()
        self.end = self._dataframe.index.max()

    def __repr__(self):
        repr_string = ""
        for site_id in sorted(self.meta.keys()):
            repr_string += site_id + ": " + self.meta[site_id]['siteName'] + "\n"
            for param in sorted(self.meta[site_id]['timeSeries'].keys()):
                repr_string += "    " + param + ": " + \
                    self.meta[site_id]['timeSeries'][param]['variableFreq'] + \
                    "  " + self.meta[site_id]['timeSeries'][param]['variableDescription'] + "\n"
        repr_string += "Start: " + str(self.start) + "\n" + \
        "End:   " + str(self.end)
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
        data_cols = self._dataframe.columns.str.contains(r'[0-9]$') # Data ends in a number.
        flag_cols = self._dataframe.columns.str.contains('_qualifiers')
        Q_cols = self._dataframe.columns.str.contains(':00060:') # This includes data & flags
        stage_cols = self._dataframe.columns.str.contains(':00065:')
        all_cols = self._dataframe.columns != ""
        param_re = r'^\d{5}$' # parameters are a five-digit number.
        station_re = r'\d{8,12}$' # station ID's are between 8 and 12 digits.

        sites = all_cols
        params = all_cols
        meta = all_cols
        if len(args) == 0:
            pass
        else:
            meta = data_cols
            for item in args:
                if item == 'all':
                    sites = all_cols
                    params = all_cols
                    meta = all_cols
                    break
                elif item == 'discharge':
                    params = Q_cols
                elif item == 'q':
                    params = Q_cols
                elif item == 'stage':
                    params = stage_cols
                elif item == 'data':
                    meta = data_cols
                elif item == 'flags':
                    meta = flag_cols
                elif re.search(param_re, item):
                    param_arg = ":" + item + ":"
                    params = self._dataframe.columns.str.contains(param_arg)
                    if not params.any():
                        raise ValueError("The parameter '{param}' is not contained in this dataset.".format(param=item))
                elif re.search(station_re, item):
                    station_arg = ":" + item + ":"
                    sites = self._dataframe.columns.str.contains(station_arg)
                    if not sites.any():
                        raise ValueError("The site '{site}' is not in this dataset.".format(site=item))
                else:
                    raise ValueError("The argument '{item}' is not recognized.".format(item=item))
        selection = sites & params & meta
        requested_df = self._dataframe.loc[:, selection]
        return requested_df

    def get_data(self):
        print("It is no longer necessary to call .get_data() to request data.")
        return self
