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

    def __init__(self, name=None):
        Station.station_dict[name] = self
        self.name = name
        # One option is to make it so that you can pass in a get_data function
        # during the creation of an instance.
        self.get_data = None


class NWIS(Station):
    """A class for working with data from the USGS NWIS service.

    TODO: decide if data should be requested when the object is created
            or when the user calls get_data().

            Opt 1: request automatically
                self.response = self.fetchNWIS()

            **==>Opt 2:** only request when user asks.
                self.get_data = self.fetchNWIS
                This has to be the way, otherwise testing is impossible...?

                now, when the user types myInstance.get_data() it returns the response object.

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
                 name=None,
                 service="dv",
                 start_date=None,
                 end_date=None,
                 parameterCd='00060'):

        sites = typing.check_NWIS_name(name)
        self.name = sites
        self.service = service
        self.start_date = start_date
        self.end_date = end_date
        self.parameterCd = parameterCd
        self.response = None
        self.df = lambda: print("You must call .get_data() before calling .df().")
        self.json = lambda: print("You must call .get_data() before calling .json().")

    def get_data(self):
        self.name = typing.check_NWIS_name(self.name)
        self.service = typing.check_NWIS_service(self.service)
        self.start_date = typing.check_datestr(self.start_date)
        self.end_date = typing.check_datestr(self.end_date)
        self.response = hf.get_nwis(self.name, self.service,
                                    self.start_date, self.end_date,
                                    parameterCd=self.parameterCd)
        # set self.json without calling it.
        self.json = lambda: self.response.json()
        # set self.df without calling it.
        self.df = lambda: hf.extract_nwis_df(self.response)

        # Another option might be to do this:
        # self.df = hf.extract_nwis_df(self.response)
        # This would make myinst.df return a plain df.
        # Unfortunately, it would be tough to test. you call get_data(), and
        # it would try to process the mocked response.

        return self

    def dataframe(self):
        """return data as a Pandas dataframe"""
        pass
