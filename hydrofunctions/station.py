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
    """A class for organizing stream gauge data for a single site."""

    def fetch2(self):
        """Will request data from NWIS after checking input types."""
        # raise TypeError if parameters are wrong
        typing.check_NWIS_station_id(self.site)
        typing.check_datestr(self.start_date)
        typing.check_datestr(self.end_date)
        hf.get_nwis(self.site, self.service, self.start_date, self.end_date)

    def __init__(self, site=None, service="dv", start_date=None, end_date=None):
        self.site = site
        self.service = service
        self.start_date = start_date
        self.end_date = end_date
        #self.fetch = hf.get_nwis(self.site, self.service, self.start_date, self.end_date)
        self.fetch = self.fetch2



