# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 21:55:04 2016

test_exceptions.py
"""
from __future__ import absolute_import, print_function, division, unicode_literals
import unittest
import warnings

from hydrofunctions import exceptions


def raiseHydroNoDataError():
    raise exceptions.HydroNoDataError("Error!!")


class TestExceptions(unittest.TestCase):

    def test_exceptions_HydroNoDataError_can_be_raised(self):
        self.assertRaises(exceptions.HydroNoDataError, raiseHydroNoDataError)


class TestWarnings(unittest.TestCase):

    def test_exceptions_HydroUserWarning_can_be_called(self):
        with self.assertWarns(exceptions.HydroUserWarning):
            warnings.warn("test warning message", exceptions.HydroUserWarning)

if __name__ == '__main__':
    unittest.main(verbosity=2)
