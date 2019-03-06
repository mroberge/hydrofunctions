# -*- coding: utf-8 -*-
"""
fixtures.py

This module is for storing all of the relavant fixtures used in testing.
"""
from .test_data import (
        JSON15min2day,
        two_sites_two_params_iv,
        nothing_avail,
        mult_flags,
        diff_freq,
        startDST,
        endDST
        )

class fakeResponse(object):

    def __init__(self, code=200, url=None, reason=None, text=None, json=None):
        self.status_code = code
        self.url = "fake url"
        self.reason = "fake reason"
        self.text = text
        # .json will return a function
        # .json() will return JSON15min2day
        self.json = lambda: JSON15min2day
        if code == 200:
            pass
        else:
            self.status_code = code

    def raise_for_status(self):
        return self.status_code
