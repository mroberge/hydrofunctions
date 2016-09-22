# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 21:55:04 2016

test_exceptions.py
"""
from __future__ import absolute_import, print_function
import unittest

from hydrofunctions import exceptions


def raiseHydroNoDataError():
    raise exceptions.HydroNoDataError("Error!!")


class TestExceptions(unittest.TestCase):

    def test_exceptions_HydroNoDataError_can_be_raised(self):
        self.assertRaises(exceptions.HydroNoDataError, raiseHydroNoDataError)

if __name__ == '__main__':
    unittest.main(verbosity=2)
