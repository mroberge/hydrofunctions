# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 21:13:34 2016

@author: Marty
"""

from __future__ import absolute_import, print_function
import unittest
from unittest import mock

from hydrofunctions import station


class TestStation(unittest.TestCase):

    def test_station_is_obj(self):
        actual = station.Station()
        self.assertIsInstance(actual, station.Station)

    def test_station_name_defaults_to_None(self):
        actual = station.Station()
        self.assertIsNone(actual.name)

    def test_station_id_sets(self):
        expected = "01234567"
        actual = station.Station(expected)
        another = station.Station("23456789")
        self.assertEqual(actual.name, expected)
        self.assertEqual(another.name, "23456789")

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

    @unittest.skip("service no longer defaults to dv.")
    def test_NWIS_service_defaults_to_dv(self):
        name = "01582500"
        service = "dv"
        start = "2011-01-01"
        end = "2011-01-02"
        actual = station.NWIS(name, service, start, end)
        self.assertEqual(actual.service, "dv")

    @unittest.skip("dates no longer default to None.")
    def test_NWIS_start_defaults_to_None(self):
        actual = station.NWIS()
        self.assertIsNone(actual.start_date)

    @unittest.skip("dates no longer default to None.")
    def test_NWIS_end_defaults_to_None(self):
        actual = station.NWIS()
        self.assertIsNone(actual.end_date)

    def test_NWIS_setters_work(self):
        name = "01582500"
        service = "dv"
        start = "2011-01-01"
        end = "2011-01-02"
        actual = station.NWIS(name, service, start, end)
        self.assertIsInstance(actual, station.NWIS)
        self.assertEqual(actual.name, name)
        self.assertEqual(actual.service, service)
        self.assertEqual(actual.start_date, start)
        self.assertEqual(actual.end_date, end)
        # self.assertIs(type(actual.fetch), function)

    @mock.patch("hydrofunctions.hydrofunctions.request_nwis")
    def test_NWIS_get_data_calls_request_nwis_correctly(self, mock_request_nwis):
        name = "01582500"
        service = "dv"
        start = "2011-01-01"
        end = "2011-01-02"
        actual = station.NWIS(name, service, start, end)
        try_it_out = actual.get_data()
        # try_it_out should be a response object, I think
        mock_request_nwis.assert_called_once_with(name, service, start, end)

      # Now I need to test .df() and .json()
    @unittest.skip("mock this out.")
    def test_NWIS_df_returns_df(self):
        name = "01582500"
        service = "dv"
        start = "2011-01-01"
        end = "2011-01-02"
        actual = station.NWIS(name, service, start, end)
        actual.get_data().df() #returns a dataframe

if __name__ == '__main__':
    unittest.main(verbosity=2)
