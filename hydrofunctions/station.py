# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 21:11:36 2016

@author: Marty


station.py
"""
from __future__ import absolute_import, print_function

class Station(object):
    """A class for organizing stream gauge data for a single site."""

    def __init__(self, site="", service="dv", start_date=None, end_date=None):
        self.site = site
        self.service = service
        self.start_date = start_date
        self.end_date = end_date


