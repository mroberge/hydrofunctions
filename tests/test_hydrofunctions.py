#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_hydrofunctions
----------------------------------

Tests for `hydrofunctions` module.
"""
from __future__ import absolute_import, print_function, division, unicode_literals
from unittest import mock
import unittest

import pandas as pd

import hydrofunctions as hf
from .test_data import JSON15min2month as test_json


class fakeResponse(object):

    def __init__(self, code=200):
        self.status_code = code
        self.url = "fake url"
        self.reason = "fake reason"
        # .json will return a function
        # .json() will return test_json
        self.json = lambda: test_json
        if code == 200:
            pass
        else:
            self.status_code = code

    def raise_for_status(self):
        return self.status_code


class TestHydrofunctions(unittest.TestCase):

    @mock.patch('requests.get')
    def test_hf_get_nwis_calls_correct_url(self, mock_get):

        """
        Thanks to
        http://engineroom.trackmaven.com/blog/making-a-mockery-of-python/
        """

        site = 'A'
        service = 'iv'
        start = 'C'
        end = 'D'

        expected_url = 'http://waterservices.usgs.gov/nwis/'+service+'/?'
        expected_headers = {'Accept-encoding': 'gzip', 'max-age': '120'}
        expected_params = {'format': 'json,1.1', 'sites': 'A', 'stateCd': None,
                           'countyCd': None, 'bBox': None,
                           'parameterCd': None, 'period': None,
                           'startDT': 'C', 'endDT': 'D'}

        expected = fakeResponse()
        expected.status_code = 200
        expected.reason = "any text"

        mock_get.return_value = expected
        actual = hf.get_nwis(site, service, start, end)
        mock_get.assert_called_once_with(expected_url, params=expected_params,
                                         headers=expected_headers)
        self.assertEqual(actual, expected)

    @mock.patch('requests.get')
    def test_hf_get_nwis_calls_correct_url_multiple_sites(self, mock_get):

        site = ['site1', 'site2']
        parsed_site = hf.check_parameter_string(site, 'site')
        service = 'iv'
        start = 'C'
        end = 'D'

        expected_url = 'http://waterservices.usgs.gov/nwis/'+service+'/?'
        expected_headers = {'max-age': '120', 'Accept-encoding': 'gzip'}
        expected_params = {'format': 'json,1.1', 'sites': parsed_site,
                           'stateCd': None, 'countyCd': None,
                           'bBox': None, 'parameterCd': None,
                           'period': None, 'startDT': 'C', 'endDT': 'D'}

        expected = fakeResponse()
        expected.status_code = 200
        expected.reason = "any text"

        mock_get.return_value = expected
        actual = hf.get_nwis(site, service, start, end)
        mock_get.assert_called_once_with(expected_url, params=expected_params,
                                         headers=expected_headers)
        self.assertEqual(actual, expected)

    @mock.patch('requests.get')
    def test_hf_get_nwis_service_defaults_dv(self, mock_get):
        site = '01541200'
        expected_service = 'dv'

        expected_url = 'http://waterservices.usgs.gov/nwis/'+expected_service+'/?'
        expected_headers = {'max-age': '120', 'Accept-encoding': 'gzip'}
        expected_params = {'format': 'json,1.1', 'sites': site,
                           'stateCd': None, 'countyCd': None,
                           'bBox': None, 'parameterCd': None,
                           'period': None, 'startDT': None, 'endDT': None}
        expected = fakeResponse()
        expected.status_code = 200
        expected.reason = "any text"

        mock_get.return_value = expected
        actual = hf.get_nwis(site)
        mock_get.assert_called_once_with(expected_url, params=expected_params,
                                         headers=expected_headers)
        self.assertEqual(actual, expected)

    @mock.patch('requests.get')
    def test_hf_get_nwis_converts_parameterCd_all_to_None(self, mock_get):
        site = '01541200'
        service = 'iv'
        parameterCd = 'all'
        expected_parameterCd = None
        expected_url = 'http://waterservices.usgs.gov/nwis/'+service+'/?'
        expected_headers = {'max-age': '120', 'Accept-encoding': 'gzip'}
        expected_params = {'format': 'json,1.1', 'sites': site,
                           'stateCd': None, 'countyCd': None,
                           'bBox': None, 'parameterCd': None,
                           'period': None, 'startDT': None, 'endDT': None}
        expected = fakeResponse()
        expected.status_code = 200
        expected.reason = "any text"

        mock_get.return_value = expected
        actual = hf.get_nwis(site, service, parameterCd=parameterCd)
        mock_get.assert_called_once_with(expected_url, params=expected_params,
                                         headers=expected_headers)
        self.assertEqual(actual, expected)

    def test_hf_get_nwis_raises_ValueError_too_many_locations(self):
        with self.assertRaises(ValueError):
            hf.get_nwis('01541000', stateCd='MD')

    def test_hf_get_nwis_raises_ValueError_start_and_period(self):
        with self.assertRaises(ValueError):
            hf.get_nwis('01541000', start_date='2014-01-01', period='P1D')

    def test_hf_extract_nwis_df(self):
        # TODO: I need to check this was parsed correctly!
        actual = hf.extract_nwis_df(test_json)
        self.assertIs(type(actual), pd.core.frame.DataFrame,
                      msg="Did not return a df")

    def test_hf_extract_nwis_stations_df(self):
        sites = ["01638500", "01646502"]
        # TODO: test should be the json for a multiple site request.
        actual = hf.extract_nwis_df(test_json)
        vD = hf.get_nwis_property(test_json, key='variableDescription')
        self.assertIs(type(actual), pd.core.frame.DataFrame,
                      msg="Did not return a df")

    def test_hf_extract_nwis_iv_gwstations_df(self):
        # TODO: I need to make a response fixture to test this out!!
        sites = ["380616075380701", "394008077005601"]
        actual = hf.extract_nwis_df(test_json)
        self.assertIs(type(actual), pd.core.frame.DataFrame,
                      msg="Did not return a df")

    def test_hf_extract_nwis_bBox_df(self):
        sites = None
        bBox = (-105.430, 39.655, -104, 39.863)
        # TODO: test should be the json for a multiple site request.
        names = hf.get_nwis_property(test_json, key='name')
        self.assertIs(type(names), list, msg="Did not return a list")
        actual = hf.extract_nwis_df(test_json)
        self.assertIs(type(actual), pd.core.frame.DataFrame,
                      msg="Did not return a df")

    def test_hf_extract_nwis_bBox2_df(self):
        sites = None
        bBox = '-105.430,39.655,-104,39.863'
        # TODO: test should be the json for a multiple site request.
        names = hf.get_nwis_property(test_json, key='name')
        actual = hf.extract_nwis_df(test_json)
        self.assertIs(type(actual), pd.core.frame.DataFrame,
                      msg="Did not return a df")

    def test_hf_extract_nwis_raises_exception_when_df_is_empty(self):
        # See line 78 in hydrofunctions
        empty_response = {'value': {'timeSeries': []}}

        with self.assertRaises(hf.HydroNoDataError):
            hf.extract_nwis_df(empty_response)

    def test_hf_nwis_custom_status_codes_returns_None_for_200(self):
        fake = fakeResponse()
        fake.status_code = 200
        fake.reason = "any text"
        fake.url = "any text"
        self.assertIsNone(hf.nwis_custom_status_codes(fake))

    def test_hf_nwis_custom_status_codes_returns_status_for_non200(self):
        bad_response = fakeResponse()
        bad_response.status_code = 400
        bad_response.reason = "any text"
        bad_response.url = "any text"
        expected = 400
        # bad_response should raise a warning that should be caught during test
        actual = None
        with self.assertWarns(SyntaxWarning) as cm:
            actual = hf.nwis_custom_status_codes(bad_response)
        # Does the function return the bad status_code?
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
