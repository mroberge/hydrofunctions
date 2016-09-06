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

    def test_exception(self):
        self.assertRaises(exceptions.HydroNoDataError, hydrof.raiseit)

if __name__ == '__main__':
    unittest.main(verbosity=2)
