# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 21:13:34 2016

@author: Marty
"""

from __future__ import absolute_import, print_function
import unittest
from unittest import mock
import pandas as pd

from hydrofunctions import station, typing


class fakeResponse(object):
    """A fake response object to test with.
    """

    def __init__(self, code=200):
        self.status_code = code
        self.url = "fake url"
        self.reason = "fake reason"
        self.json = lambda: {'data': 'fake json'}
        if code == 200:
            self.ok = True
        else:
            self.status_code = code
            self.ok = False

    def raise_for_status(self):
        return self.status_code


class TestStation(unittest.TestCase):

    def test_station_is_obj(self):
        actual = station.Station()
        self.assertIsInstance(actual, station.Station)

    def test_station_site_defaults_to_None(self):
        actual = station.Station()
        self.assertIsNone(actual.site)

    def test_station_id_sets(self):
        expected = "01234567"
        actual = station.Station(expected)
        another = station.Station("23456789")
        self.assertEqual(actual.site, expected)
        self.assertEqual(another.site, "23456789")

    def test_station_dict_returns_dict(self):
        actual = station.Station('first')
        self.assertIsInstance(actual.station_dict, dict)

    def test_multiple_instances_only_one_list(self):
        first = station.Station('first')
        second = station.Station('second')
        self.assertEqual(first.station_dict, second.station_dict)

    def test_station_dict_keeps_keys(self):
        first = station.Station('first')
        second = station.Station('second')
        actual = first.station_dict
        self.assertIn('first', actual)
        self.assertIn('second', actual)
        self.assertEqual(len(actual), 2, "The dict length is not equal to the \
                                            number of instances")

    def test_station_dict_returns_instance(self):
        first = station.Station('first')
        second = station.Station('second')
        expected = first
        # Look at the station_dict; does it contain a ref to 'first'?
        actual = second.station_dict['first']
        self.assertEqual(actual, expected)

    def test_station_subclasses_maintain_same_station_dict(self):
        class Foo(station.Station):
            pass

        foo_inst = Foo('foo')
        station_inst = station.Station('station')
        self.assertIn('station', foo_inst.station_dict)
        self.assertIn('foo', station_inst.station_dict)
        actual = station_inst.station_dict['foo']
        self.assertIsInstance(actual, Foo)


class TestNWIS(unittest.TestCase):
    """Testing the station.NWIS object."""

    def test_NWIS_service_defaults_to_dv(self):
        site = "01582500"
        service = "dv"
        start = "2011-01-01"
        end = "2011-01-02"
        actual = station.NWIS(site, service, start, end)
        self.assertEqual(actual.service, "dv")

    def test_NWIS_start_defaults_to_None(self):
        actual = station.NWIS()
        self.assertIsNone(actual.start_date)

    def test_NWIS_end_defaults_to_None(self):
        actual = station.NWIS()
        self.assertIsNone(actual.end_date)

    def test_NWIS_setters_work(self):
        site = "01582500"
        service = "dv"
        start = "2011-01-01"
        end = "2011-01-02"
        actual = station.NWIS(site, service, start, end)
        self.assertIsInstance(actual, station.NWIS)
        self.assertEqual(actual.site, site)
        self.assertEqual(actual.service, service)
        self.assertEqual(actual.start_date, start)
        self.assertEqual(actual.end_date, end)
        # self.assertIs(type(actual.fetch), function)

    def test_NWIS_setters_parameterCd(self):
        site = "01582500"
        service = "dv"
        start = "2011-01-01"
        end = "2011-01-02"
        parameterCd = "00065"
        actual = station.NWIS(site, service, start, end,
                              parameterCd=parameterCd)
        self.assertIsInstance(actual, station.NWIS)
        self.assertEqual(actual.site, site)
        self.assertEqual(actual.service, service)
        self.assertEqual(actual.start_date, start)
        self.assertEqual(actual.parameterCd, parameterCd)

    @mock.patch("hydrofunctions.hydrofunctions.get_nwis")
    @mock.patch("hydrofunctions.hydrofunctions.get_nwis_property")
    def test_NWIS_get_data_calls_get_nwis_correctly(self, mock_get_prop, mock_get_nwis):
        site = "01582500"
        service = "dv"
        start = "2011-01-01"
        end = "2011-01-02"
        parameterCd = "00060"

        actual = station.NWIS(site, service, start, end)
        try_it_out = actual.get_data()
        # try_it_out should be a response object, I think
        mock_get_nwis.assert_called_once_with(site, service, start, end,
                                              parameterCd=parameterCd,
                                              period=None, stateCd=None,
                                              countyCd=None, bBox=None)

    @mock.patch("hydrofunctions.hydrofunctions.get_nwis")
    @mock.patch("hydrofunctions.hydrofunctions.get_nwis_property")
    def test_NWIS_get_data_calls_get_nwis_mult_sites(self, mock_get_prop, mock_get_nwis):
        site = ["01638500", "01646502"]
        siteEx = "01638500,01646502"
        service = "dv"
        start = "2011-01-01"
        end = "2011-01-02"
        parameterCd = "00060"
        actual = station.NWIS(site, service, start, end)
        try_it_out = actual.get_data()
        # try_it_out should be an instance of NWIS.
        mock_get_nwis.assert_called_once_with(siteEx, service, start, end,
                                              parameterCd=parameterCd,
                                              period=None, stateCd=None,
                                              countyCd=None, bBox=None)

    @mock.patch('requests.get')
    @mock.patch("hydrofunctions.hydrofunctions.get_nwis_property")
    def test_hf_get_nwis_accepts_countyCd_array(self, mock_get_prop, mock_get):
        start = "2017-01-01"
        end = "2017-12-31"
        cnty = ['51059', '51061']
        cnty = typing.check_NWIS_site(cnty)
        service2 = 'dv'

        expected_url = 'http://waterservices.usgs.gov/nwis/dv/?'
        expected_headers = {'max-age': '120', 'Accept-encoding': 'gzip'}
        expected_params = {'format': 'json,1.1', 'sites': None,
                           'stateCd': None, 'countyCd': cnty, 'bBox': None,
                           'parameterCd': '00060', 'period': None,
                           'startDT': start, 'endDT': end}

        expected = fakeResponse(200)

        mock_get.return_value = expected
        actual = station.NWIS(None, service2, start, countyCd=cnty,
                              end_date=end).get_data()
        mock_get.assert_called_once_with(expected_url, params=expected_params,
                                         headers=expected_headers)

    @mock.patch('requests.get')
    @mock.patch("hydrofunctions.hydrofunctions.get_nwis_property")
    def test_hf_get_nwis_accepts_parameterCd_array(self, mock_get_prop, mock_get):
        site = '01541200'
        start = "2017-01-01"
        end = "2017-12-31"
        service = 'iv'
        parameterCd = ['00060','00065']
        expected_parameterCd = '00060,00065'

        expected_url = 'http://waterservices.usgs.gov/nwis/iv/?'
        expected_headers = {'max-age': '120', 'Accept-encoding': 'gzip'}
        expected_params = {'format': 'json,1.1', 'sites': site,
                           'stateCd': None, 'countyCd': None, 'bBox': None,
                           'parameterCd': expected_parameterCd, 'period': None,
                           'startDT': start, 'endDT': end}

        expected = fakeResponse(200)

        mock_get.return_value = expected
        actual = station.NWIS(site, service, start, end_date=end,
                              parameterCd = parameterCd).get_data()
        mock_get.assert_called_once_with(expected_url, params=expected_params,
                                         headers=expected_headers)

    # Now test .df() and .json()
    @unittest.skip("Test this differently")
    def test_NWIS_df_returns_df(self):
        site = "01582500"
        service = "dv"
        start = "2011-01-01"
        end = "2011-01-02"
        actual = station.NWIS(site, service, start, end)
        # You don't need to test the following like this.
        # Just test that actual.df() returns nothing if you call before get_data()
        # And actual.df() returns a df if you call after .get_data()
        actualdf = actual.get_data().df()  # returns a dataframe
        self.assertIs(type(actualdf), pd.core.frame.DataFrame,
                      msg="Did not return a df")


if __name__ == '__main__':
    unittest.main(verbosity=2)
