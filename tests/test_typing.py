# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 11:20:51 2016

@author: Marty

test_typing.py
tests for typing.py
"""
from __future__ import absolute_import, print_function
import unittest
from hydrofunctions import typing


class TestTyping(unittest.TestCase):

    def test_typing_check_NWIS_station_id_accepts_str(self):
        actual = typing.check_NWIS_station_id("any string")
        self.assertTrue(actual)

    def test_typing_check_NWIS_station_id_raises_TypeError(self):
        not_string = 5
        self.assertRaises(TypeError, typing.check_NWIS_station_id, not_string)

    def test_typing_check_datestr_raises_TypeError(self):
        not_string = 5
        self.assertRaises(TypeError, typing.check_datestr, not_string)

    def test_typing_check_datestr_returns_true_for_good_date(self):
        actual = typing.check_datestr("2002-03-03")
        self.assertTrue(actual)

    def test_typing_check_datestr_rejects_bad_date(self):
        # pattern = r"[1-2]\d\d\d-[0-1]\d-[0-3]\d"
        bad1 = "3002-03-03"
        bad2 = "0000-03-03"
        bad3 = "1111-21-03"
        bad4 = "1111-03-43"
        self.assertRaises(TypeError, typing.check_datestr, bad1)
        self.assertRaises(TypeError, typing.check_datestr, bad2)
        self.assertRaises(TypeError, typing.check_datestr, bad3)
        self.assertRaises(TypeError, typing.check_datestr, bad4)

if __name__ == '__main__':
    unittest.main(verbosity=2)
