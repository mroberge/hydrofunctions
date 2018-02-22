#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_hydrofunctions
----------------------------------

Tests for `hydrofunctions` module.
"""
from __future__ import absolute_import, print_function
from unittest import mock
import unittest

import pandas as pd

import hydrofunctions as hf


class fakeResponse(object):
    pass


class TestHydrofunctions(unittest.TestCase):

    @mock.patch('requests.get')
    def test_hf_get_nwis_calls_correct_url(self, mock_get):

        """
        Thanks to
        http://engineroom.trackmaven.com/blog/making-a-mockery-of-python/
        """

        site = 'A'
        service = 'B'
        start = 'C'
        end = 'D'

        expected_url = 'http://waterservices.usgs.gov/nwis/B/?'
        expected_headers = {'Accept-encoding': 'gzip', 'max-age': '120'}
        expected_params = {'format': 'json,1.1', 'parameterCd': '00060', 'period': None, 'startDT': 'C', 'endDT': 'D', 'sites': 'A'}

        expected = fakeResponse()
        expected.status_code = 200

        mock_get.return_value = expected
        actual = hf.get_nwis(site, service, start, end)
        mock_get.assert_called_once_with(expected_url, params=expected_params,
                                         headers=expected_headers)
        self.assertEqual(actual, expected)

    @mock.patch('requests.get')
    def test_hf_get_nwis_calls_correct_url_multiple_sites(self, mock_get):

        site = ['site1', 'site2']
        service = 'B'
        start = 'C'
        end = 'D'

        expected_url = 'http://waterservices.usgs.gov/nwis/B/?'
        expected_headers = {'max-age': '120', 'Accept-encoding': 'gzip'}
        expected_params = {'format': 'json,1.1', 'sites': 'site1,site2', 'endDT': 'D',
                           'startDT': 'C', 'parameterCd': '00060', 'period': None}

        expected = fakeResponse()
        expected.status_code = 200

        mock_get.return_value = expected
        actual = hf.get_nwis(site, service, start, end)
        mock_get.assert_called_once_with(expected_url, params=expected_params,
                                         headers=expected_headers)
        self.assertEqual(actual, expected)

    @unittest.skip('Stop requesting data during test.')
    def test_hf_extract_nwis_dict(self):
        # TODO: I need to make a fake response object to test this properly!!
        test = hf.get_nwis("01589440", "dv", "2013-01-01", "2013-01-05")
        actual = hf.extract_nwis_dict(test)
        self.assertIs(type(actual), dict, msg="Did not return a dict")

    @unittest.skip('Stop requesting data during test.')
    def test_hf_extract_nwis_df(self):
        # TODO: I need to make a response fixture to test this out!!
        test = hf.get_nwis("01589440", "dv", "2013-01-01", "2013-01-05")
        actual = hf.extract_nwis_df(test)
        self.assertIs(type(actual), pd.core.frame.DataFrame,
                      msg="Did not return a df")

    @unittest.skip('Stop requesting data during test.')
    def test_hf_extract_nwis_stations_df(self):
        # TODO: I need to make a fake response with multiple sites to test this out!!
        sites = ["01638500", "01646502"]
        test = hf.get_nwis(sites, "dv",
                           "2013-01-01", "2013-01-05")
        actual = hf.extract_nwis_df(test)
        self.assertIs(type(actual), pd.core.frame.DataFrame,
                      msg="Did not return a df")

    @unittest.skip('Stop requesting data during test.')
    def test_hf_extract_nwis_iv_gwstations_df(self):
        # TODO: I need to make a response fixture to test this out!!
        sites = ["380616075380701", "394008077005601"]
        test = hf.get_nwis(sites, "iv",
                           "2018-01-01", "2018-01-05", parameterCd='72019')
        actual = hf.extract_nwis_df(test)
        self.assertIs(type(actual), pd.core.frame.DataFrame,
                      msg="Did not return a df")

    @unittest.skip("What happens if NWIS returns valid response with no data?")
    def test_hf_extract_nwis_raises_exception_when_df_is_empty(self):
        # See line 78 in hydrofunctions
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
