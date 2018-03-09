# -*- coding: utf-8 -*-
"""
test_charts.py

Tests for the charts.py module.
"""
from __future__ import absolute_import, print_function
import unittest
import matplotlib
import pandas as pd

from hydrofunctions import charts


class TestFlowDuration(unittest.TestCase):

    def test_charts_flowduration_exists(self):
        d = {'col1': [1, 2, 3, 38, 23, 1, 19],
             'col2': [3, 4, 45, 23, 2, 4, 76]}
        expected = pd.DataFrame(data=d)
        actual = charts.flow_duration(expected)
        self.assertIsInstance(actual, tuple)
        self.assertIsInstance(actual[0], matplotlib.figure.Figure)
        self.assertIsInstance(actual[1], matplotlib.axes.Axes)


if __name__ == '__main__':
    unittest.main(verbosity=2)
