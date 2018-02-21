# -*- coding: utf-8 -*-
"""
station.py

This module contains the Station class, which is used for organizing and
managing data for a single USGS stream gauge.
"""
from __future__ import absolute_import, print_function
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

        start_date (str):
           should take on the form yyyy-mm-dd

        end_date (str):
            should take on the form yyyy-mm-dd

        stateCd (str):
            a valid two-letter state postal abbreviation. Default is None.

        countyCd (str or list of strings):
            a valid county abbreviation. Default is None.

        parameterCd (str):
            NWIS parameter code. Default is stream discharge '00060'
                * stage: '00065'
                * discharge: '00060'
                * not all sites collect all parameters!
                * See https://nwis.waterdata.usgs.gov/usa/nwis/pmcodes for \
                full list


    TODO: decide if data should be requested when the object is created
            or when the user calls get_data().

            Opt 1: request automatically
                self.response = self.fetchNWIS()

            **==>Opt 2:** only request when user asks.
                self.get_data = self.fetchNWIS
                This has to be the way, otherwise testing is impossible...?

                now, when the user types myInstance.get_data() it returns the \
                response object.

    TODO: decide how the service, start_date, and end_date should be passed
        to the instance so that requests can be made from NWIS.

            **==>Opt 1:** pass these variables to the instance when it is made. (current option)
                HerringRun = NWIS("01585200", "dv", "2014-04-01", "2014-06-01")

            Opt 2: Create a session object that contains the data folder location
                    and an Analysis object that contains the start & end date.
                    ??when would the service get passed??
                    -create both NWISiv and NWISdv classes (this would make it hard to keep both data sets in the same object)
    """

    def __init__(self,
                 site=None,
                 service="dv",
                 start_date=None,
                 end_date=None,
                 stateCd=None,
                 countyCd=None,
                 parameterCd='00060',
                 period=None):

        self.site = typing.check_NWIS_site(site)
        self.service = typing.check_NWIS_service(service)
        self.start_date = typing.check_datestr(start_date)
        self.end_date = typing.check_datestr(end_date)
        self.stateCd = stateCd
        self.countyCd = countyCd
        self.parameterCd = parameterCd
        self.period = typing.check_period(period)
        self.response = None
        self.df = lambda: print("You must call .get_data() before calling .df().")
        self.json = lambda: print("You must call .get_data() before calling .json().")
        if (self.site and self.stateCd) or \
           (self.stateCd and self.countyCd) or \
           (self.site and self.countyCd):
            raise ValueError("Select sites using either site, stateCd, or "
                             "countyCd, but not more than one.")
        if (self.start_date and self.period):
            raise ValueError("Use either start_date or period, but not both.")

    def get_data(self):
        self.site = typing.check_NWIS_site(self.site)
        self.service = typing.check_NWIS_service(self.service)
        self.start_date = typing.check_datestr(self.start_date)
        self.end_date = typing.check_datestr(self.end_date)
        self.response = hf.get_nwis(self.site,
                                    self.service,
                                    self.start_date,
                                    self.end_date,
                                    stateCd=self.stateCd,
                                    countyCd=self.countyCd,
                                    parameterCd=self.parameterCd)
        # If the response status_code is anything other than 200,
        # an error will be reported and an Exception raised.
        # The response object will be saved for examination.
        hf.handle_status_code(self.response)
        # set self.json without calling it.
        self.json = lambda: self.response.json()
        # set self.df without calling it.
        self.df = lambda: hf.extract_nwis_df(self.response)

        # Another option might be to do this:
        # self.df = hf.extract_nwis_df(self.response)
        # This would make myInstance.df return a plain df.

        return self
