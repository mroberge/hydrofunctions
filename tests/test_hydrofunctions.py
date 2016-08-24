#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_hydrofunctions
----------------------------------

Tests for `hydrofunctions` module.
"""
from __future__ import absolute_import, print_function
import unittest

from hydrofunctions import hydrofunctions as hf


class TestHydrofunctions(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass
        print("test000")
        assert True

    def test_first_returns_true(self):
        expected = True
        actual = hf.first()
        self.assertEqual(expected, actual, msg="first() did not return True.")

    def test_get_nwis_returns_response(self):
        expected = 200
        response = hf.get_nwis('01585200', 'dv', '2001-01-01', '2001-01-02')
        actual = response.status_code
        self.assertEqual(expected, actual, msg="get_nwis did not return a 200 code.")
