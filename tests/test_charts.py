# -*- coding: utf-8 -*-
"""
test_charts.py

Tests for the charts.py module.
"""
from __future__ import absolute_import, print_function
import unittest
import matplotlib
# attempted matplotlib.use('Agg') here, but it was too late; backend already set
import pandas as pd

from hydrofunctions import charts

dummy = {'col1': [1, 2, 3, 38, 23, 1, 19],
         'col2': [3, 4, 45, 23, 2, 4, 76]}


class TestFlowDuration(unittest.TestCase):

    def test_charts_flowduration_exists(self):
        expected = pd.DataFrame(data=dummy)
        actual_fig, actual_ax = charts.flow_duration(expected)
        self.assertIsInstance(actual_fig, matplotlib.figure.Figure)
        self.assertIsInstance(actual_ax, matplotlib.axes.Axes)

    def test_charts_flowduration_defaults(self):
        expected = pd.DataFrame(data=dummy)

        actual_fig, actual_ax = charts.flow_duration(expected)

        actual_xscale = actual_ax.xaxis.get_scale()
        actual_yscale = actual_ax.yaxis.get_scale()
        actual_ylabel = actual_ax.yaxis.get_label_text()
        actual_marker = actual_ax.get_lines()[0].get_marker()

        self.assertEqual(actual_xscale, 'logit')
        self.assertEqual(actual_yscale, 'log')
        self.assertEqual(actual_ylabel, 'Stream Discharge (m³/s)')
        self.assertEqual(actual_marker, '.')

    def test_charts_flowduration_accepts_params(self):
        expected = pd.DataFrame(data=dummy)
        params = {'xscale': 'linear',
                  'yscale': 'linear',
                  'ylabel': 'test value',
                  'symbol': ','}

        actual_fig, actual_ax = charts.flow_duration(expected, **params)

        actual_xscale = actual_ax.xaxis.get_scale()
        actual_yscale = actual_ax.yaxis.get_scale()
        actual_ylabel = actual_ax.yaxis.get_label_text()
        actual_marker = actual_ax.get_lines()[0].get_marker()

        self.assertEqual(actual_xscale, 'linear')
        self.assertEqual(actual_yscale, 'linear')
        self.assertEqual(actual_ylabel, 'test value')
        self.assertEqual(actual_marker, ',')


if __name__ == '__main__':
    unittest.main(verbosity=2)
