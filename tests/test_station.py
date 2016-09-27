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

    def test_station_id_defaults_to_None(self):
        actual = station.Station()
        self.assertIsNone(actual.id)

    def test_station_id_sets(self):
        expected = "0123"
        actual = station.Station(expected)
        another = station.Station("ABC")
        self.assertEqual(actual.id, expected)
        self.assertEqual(another.id, "ABC")

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
        actual = station.NWIS()
        service = "problem!"
        self.assertEqual(actual.service, "dv")

    def test_NWIS_start_defaults_to_None(self):
        actual = station.NWIS()
        self.assertIsNone(actual.start_date)

    def test_NWIS_end_defaults_to_None(self):
        actual = station.NWIS()
        self.assertIsNone(actual.end_date)

    def test_NWIS_setters_work(self):
        actual = station.NWIS("A", "B", "C", "D")
        self.assertIsInstance(actual, station.NWIS)
        self.assertEqual(actual.id, "A")
        self.assertEqual(actual.service, "B")
        self.assertEqual(actual.start_date, "C")
        self.assertEqual(actual.end_date, "D")
        # self.assertIs(type(actual.fetch), function)

    @mock.patch("hydrofunctions.hydrofunctions.get_nwis")
    def test_NWIS_fetch_calls_get_nwis_correctly(self, mock_get_nwis):
        actual = station.NWIS("A", "B", "1111-11-11", "1111-11-11")
        try_it_out = actual.get_data()
        mock_get_nwis.assert_called_once_with("A", "B", "1111-11-11", "1111-11-11")

    @mock.patch("hydrofunctions.hydrofunctions.get_nwis")
    def test_NWIS_fetch2_calls_get_nwis_correctly(self, mock_get_nwis):
        actual = station.NWIS("A", "B", "2002-03-03", "2002-03-03")
        try_it_out = actual.get_data()
        # This won't raise TypeError for "C" not matching "yyyy-mm-dd"
        mock_get_nwis.assert_called_once_with("A", "B", "2002-03-03", "2002-03-03")


if __name__ == '__main__':
    unittest.main(verbosity=2)
