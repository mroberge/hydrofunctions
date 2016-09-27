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
    """A class for organizing stream gauge data for a single site.

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
        only create new instance if its id is not already in the list.
        if id in station_dict:
            #just re-use already existing obj.
            return station_dict[id]
            #prob need to use a factory to do this.
    """
    station_dict = {}

    def __init__(self, id=None):
        Station.station_dict[id] = self
        self.id = id
        # One option is to make it so that you can pass in a get_data function
        # during the creation of an instance.
        self.get_data = None


class NWIS(Station):
    """As class for working with data from the USGS NWIS service."""

    def __init__(self,
                 id=None,
                 service="dv",
                 start_date=None,
                 end_date=None):
        self.id = id
        self.service = service
        self.start_date = start_date
        self.end_date = end_date
        # self.get_data = hf.get_nwis(self.site, self.service, self.start_date, self.end_date)
        self.get_data = self.fetch2

    def fetch2(self):
        """Will request data from NWIS after checking input types."""
        # raise TypeError if parameters are wrong
        typing.check_NWIS_station_id(self.id)
        typing.check_datestr(self.start_date)
        typing.check_datestr(self.end_date)
        hf.get_nwis(self.id, self.service, self.start_date, self.end_date)
