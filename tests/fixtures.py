"""
fixtures.py

This module is for storing all of the relavant fixtures used in testing.
"""
from .fixtures_data import (
    JSON15min2day,
    two_sites_two_params_iv,
    nothing_avail,
    mult_flags,
    diff_freq,
    startDST,
    endDST,
    daily_lake_level,
)

from .fixtures_daily_dupe import daily_dupe, daily_dupe_altered

from .fixtures_multiple_methods import multi_meth

from .fixtures_tzfail import tzfail

from .fixtures_recent_only import recent_only

from .fixtures_usgs_rdb import (
    field_fixture,
    rating_fixture,
    peaks_fixture,
    parsing_error_fixture,
)


class fakeResponse(object):
    def __init__(
        self,
        code=200,
        url="fake url",
        reason="fake reason",
        text="fake text",
        json=JSON15min2day,
    ):
        self.status_code = code
        self.url = url
        self.reason = reason
        self.text = text
        # .json will return a function
        # .json() will return JSON15min2day
        self.json = lambda: json
        if self.status_code == 200:
            self.ok = True
        else:
            self.ok = False

    def raise_for_status(self):
        return self.status_code
