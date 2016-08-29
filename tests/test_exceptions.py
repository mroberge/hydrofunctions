# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 21:55:04 2016

test_exceptions.py
"""
from __future__ import absolute_import, print_function
import unittest

from hydrofunctions import exceptions
from hydrofunctions import hydrofunctions as hydrof


class TestExceptions(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_001_something(self):
        pass
        print("test001")
        assert True

    def test_exception(self):
        self.assertRaises(exceptions.HydroNoDataError, hydrof.raiseit)
