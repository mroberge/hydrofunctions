# -*- coding: utf-8 -*-
"""
test_charts.py

Tests for the charts.py module.
"""
from __future__ import absolute_import, print_function
import unittest

from hydrofunctions import charts


class TestFlowDuration(unittest.TestCase):

    def test_charts_flowduration_exists(self):
        expected = 5
        actual = charts.flow_duration(expected)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
