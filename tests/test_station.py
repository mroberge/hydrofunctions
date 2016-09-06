# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 21:13:34 2016

@author: Marty
"""

from __future__ import absolute_import, print_function
import unittest
from hydrofunctions import station


class TestStation(unittest.TestCase):

    def test_station_is_obj(self):
        actual = station.Station()
        self.assertIsInstance(actual, station.Station)

    def test_station_site_defaults_to_empty_str(self):
        actual = station.Station()
        self.assertEqual(actual.site, "")

    def test_station_site_sets(self):
        expected = "0123"
        actual = station.Station(expected)
        another = station.Station("ABC")
        self.assertEqual(actual.site, expected)
        self.assertEqual(another.site, "ABC")

    def test_station_service_defaults_to_dv(self):
        actual = station.Station()
        self.assertEqual(actual.service, "dv")

    def test_station_start_defaults_to_None(self):
        actual = station.Station()
        self.assertIsNone(actual.start_date)

    def test_station_end_defaults_to_None(self):
        actual = station.Station()
        self.assertIsNone(actual.end_date)

if __name__ == '__main__':
    unittest.main(verbosity=2)
