# -*- coding: utf-8 -*-
"""
station.py

This module contains the Station class, which is used for organizing and
managing data for a single USGS stream gauge.
"""
from __future__ import absolute_import, print_function, division, unicode_literals
from . import typing
from . import hydrofunctions as hf


class Station(object):
    """A class for organizing stream gauge data for a single request.

    Store copies of each station in a dictionary station_dict.
    This dict will include descendant objects too.
    The dict will be

    Improvements:
        make each subclass store its own dictionary, parent class can combine.
        only store weakrefs to the objects, so that they can be garbage
        collected. maybe weakvaluedictionary.

            1) http://stackoverflow.com/a/18321898
            2) http://stackoverflow.com/a/9460070

    Future Feature:
        only create new instance if its id is not already in the list. ::

            if id in station_dict:
                # just re-use already existing obj.
                return station_dict[id]
                # prob need to use a factory to do this.
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
            a valid site is '01585200' or ['01585200', '01646502']. Site
            should be None if stateCd or countyCd are not None.

        service (str):
            can either be 'iv' or 'dv' for instantaneous or daily data.
            'dv'(default): daily values. Mean value for an entire day.
            'iv': instantaneous value measured at this time. Also known
            as 'Real-time data'. Can be measured as often as every
            five minutes by the USGS. 15 minutes is more typical.

        start_date (str):
           should take on the form yyyy-mm-dd

        end_date (str):
            should take on the form yyyy-mm-dd

        stateCd (str):
            a valid two-letter state postal abbreviation. Default is None.

        countyCd (str or list of strings):
            a valid county abbreviation. Default is None.

        bBox (str, list, or tuple):
            a set of coordinates that defines a bounding box.
                * Coordinates are in decimal degrees
                * Longitude values are negative (west of the prime meridian).
                * Latitude values are positive (north of the equator).
                * comma-delimited, no spaces, if provided as a string.
                * The order of the boundaries should be: "West,South,East,North"
                * Example: "-83.000000,36.500000,-81.000000,38.500000"

        parameterCd (str or list of strings):
            NWIS parameter code. Usually a five digit code. Default is 'all'.
            A valid code can also be given as a list: parameterCd=['00060','00065']
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

        self.site = typing.check_parameter_string(site, 'site')
        self.service = typing.check_NWIS_service(service)
        self.start_date = typing.check_datestr(start_date)
        self.end_date = typing.check_datestr(end_date)
        self.stateCd = stateCd
        self.countyCd = typing.check_parameter_string(countyCd, 'county')
        self.bBox = bBox
        self.ok = False
        self.parameterCd = typing.check_parameter_string(parameterCd, 'parameterCd')
        self.period = typing.check_period(period)
        self.response = None
        self.df = lambda: print("You must successfully call .get_data() before calling .df().")
        self.json = lambda: print("You must successfully call .get_data() before calling .json().")
        self.name = None
        self.siteName = None

        # Check that site selcetion parameters are exclusive!
        if (self.site and self.stateCd) \
            or (self.stateCd and self.countyCd) \
            or (self.site and self.countyCd) \
            or (self.site and self.bBox):
            raise ValueError("Select sites using either site, stateCd, or "
                             "countyCd, but not more than one.")

        # Check that time parameters are not both set.
        # If neither is set, then NWIS will return the most recent observation.
        if (self.start_date and self.period):
            raise ValueError("Use either start_date or period, or neither, "
                             "but not both.")

    def get_data(self):
        self.response = hf.get_nwis(self.site,
                                    self.service,
                                    self.start_date,
                                    self.end_date,
                                    stateCd=self.stateCd,
                                    countyCd=self.countyCd,
                                    bBox=self.bBox,
                                    parameterCd=self.parameterCd,
                                    period=self.period)
        # If the response status_code is anything other than 200,
        # an error will be reported and an Exception raised.
        # The response object will be saved for examination.

        #TODO: fix tests and uncomment this call
        #hf.handle_status_code(self.response)
        #nwis_custom_status_codes(self.response)
        # Raise an exception if non-200 status_code, or return None for 200.
        self.response.raise_for_status()

        # set self.json without calling it.
        self.json = lambda: self.response.json()
        # set self.df without calling it.
        self.df = lambda: hf.extract_nwis_df(self.json())

        # Another option might be to do this:
        # self.df = hf.extract_nwis_df(self.response)
        # This would make myInstance.df return a plain df.
        self.ok = self.response.ok
        self.siteName = hf.get_nwis_property(self.json(),
                                             key='siteName',
                                             remove_duplicates=True)
        self.name = hf.get_nwis_property(self.json(),
                                         key='name',
                                         remove_duplicates=True)

        return self
