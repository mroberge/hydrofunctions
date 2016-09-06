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

    def test_station_site_defaults_to_None(self):
        actual = station.Station()
        self.assertIsNone(actual.site)

    def test_station_site_sets(self):
        expected = "0123"
        actual = station.Station(expected)
        another = station.Station("ABC")
        self.assertEqual(actual.site, expected)
        self.assertEqual(another.site, "ABC")

    def test_station_service_defaults_to_dv(self):
        actual = station.Station()
        service = "problem!"
        self.assertEqual(actual.service, "dv")

    def test_station_start_defaults_to_None(self):
        actual = station.Station()
        self.assertIsNone(actual.start_date)

    def test_station_end_defaults_to_None(self):
        actual = station.Station()
        self.assertIsNone(actual.end_date)

    def test_station_setters_work(self):
        actual = station.Station("A", "B", "C", "D")
        self.assertIsInstance(actual, station.Station)
        self.assertEqual(actual.site, "A")
        self.assertEqual(actual.service, "B")
        self.assertEqual(actual.start_date, "C")
        self.assertEqual(actual.end_date, "D")
        # self.assertIs(type(actual.fetch), function)

    @mock.patch("hydrofunctions.hydrofunctions.get_nwis")
    def test_station_fetch_calls_get_nwis_correctly(self, mock_get_nwis):
        actual = station.Station("A", "B", "1111-11-11", "1111-11-11")
        try_it_out = actual.fetch()
        mock_get_nwis.assert_called_once_with("A", "B", "1111-11-11", "1111-11-11")

    @mock.patch("hydrofunctions.hydrofunctions.get_nwis")
    def test_station_fetch2_calls_get_nwis_correctly(self, mock_get_nwis):
        actual = station.Station("A", "B", "2002-03-03", "2002-03-03")
        try_it_out = actual.fetch()
        # This won't raise TypeError for "C" not matching "yyyy-mm-dd"
        mock_get_nwis.assert_called_once_with("A", "B", "2002-03-03", "2002-03-03")


if __name__ == '__main__':
    unittest.main(verbosity=2)
