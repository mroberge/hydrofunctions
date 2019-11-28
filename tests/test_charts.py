# -*- coding: utf-8 -*-
"""
test_charts.py

Tests for the charts.py module.
"""
from __future__ import absolute_import, print_function, division, unicode_literals
import unittest
import matplotlib
import pandas as pd

from hydrofunctions import charts
import hydrofunctions as hf
from .test_data import JSON15min2day as test_json

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
        actual_legend = actual_ax.get_legend()
        actual_legend_loc = actual_legend._loc
        actual_title = actual_ax.get_title()

        self.assertEqual(actual_xscale, 'logit')
        self.assertEqual(actual_yscale, 'log')
        self.assertEqual(actual_ylabel, 'Stream Discharge (m³/s)')
        self.assertEqual(actual_marker, '.')
        self.assertTrue(actual_legend)
        self.assertEqual(actual_legend_loc, 0) # '0' is internal code for 'best'.
        self.assertEqual(actual_title, '')

    def test_charts_flowduration_accepts_params(self):
        expected = pd.DataFrame(data=dummy)
        params = {'xscale': 'linear',
                  'yscale': 'linear',
                  'ylabel': 'test value',
                  'symbol': ',',
                  'legend': False,
                  'legend_loc': 'center',
                  'title': 'Test Title',
                  }

        actual_fig, actual_ax = charts.flow_duration(expected, **params)

        actual_xscale = actual_ax.xaxis.get_scale()
        actual_yscale = actual_ax.yaxis.get_scale()
        actual_ylabel = actual_ax.yaxis.get_label_text()
        actual_marker = actual_ax.get_lines()[0].get_marker()
        actual_legend = actual_ax.get_legend()
        # There is no legend in this test, so there is no legend property.
        #actual_legend_loc = actual_legend._loc
        actual_title = actual_ax.get_title()

        self.assertEqual(actual_xscale, 'linear')
        self.assertEqual(actual_yscale, 'linear')
        self.assertEqual(actual_ylabel, 'test value')
        self.assertEqual(actual_marker, ',')
        self.assertIsNone(actual_legend)
        # There is no legend, so there is no legend location property.
        #self.assertEqual(actual_legend_loc, 10) # 'center' is equal to 10.
        self.assertEqual(actual_title, 'Test Title')

class TestCyclePlot(unittest.TestCase):

    def test_charts_groupby_not_object_dtype(self):
        # For reasons I don't understand, I think Pandas 0.25.0 counts
        # DataFrameGroupBy as an object, and you can't use .quintile() on it.?
        expected_df, expected_dict = hf.extract_nwis_df(test_json, interpolate=False)
        self.assertFalse(pd.api.types.is_object_dtype(expected_df))
        grouped = expected_df.groupby(expected_df.index.weekday)
        self.assertIsInstance(grouped, pd.core.groupby.generic.DataFrameGroupBy)
        self.assertFalse(pd.api.types.is_object_dtype(grouped))

    def test_charts_cycleplot_exists(self):
        expected_df, expected_dict = hf.extract_nwis_df(test_json, interpolate=False)
        actual_fig, actual_ax = charts.cycleplot(expected_df)
        self.assertIsInstance(actual_fig, matplotlib.figure.Figure)
        self.assertIsInstance(actual_ax[0], matplotlib.axes.Axes)

    def test_charts_cycleplot_parts(self):
        expected_df, expected_dict = hf.extract_nwis_df(test_json, interpolate=False)

        actual_fig, actual_ax = charts.cycleplot(expected_df, legend_loc='center', title='test title')

        actual_xscale = actual_ax[0].xaxis.get_scale()
        actual_yscale = actual_ax[0].yaxis.get_scale()
        actual_ylabel = actual_ax[0].yaxis.get_label_text()
        actual_legend = actual_ax[0].get_legend()
        actual_legend_loc = actual_legend._loc
        actual_title = actual_fig._suptitle.get_text() # unofficial title accessor! A little wonky.

        self.assertEqual(actual_xscale, 'linear')
        self.assertEqual(actual_yscale, 'linear')
        self.assertEqual(actual_ylabel, 'Discharge (ft³/s)')
        self.assertTrue(actual_legend)
        self.assertEqual(actual_legend_loc, 10) # '10' is internal code for legend(loc = 'center')
        self.assertEqual(actual_title, 'test title')

    def test_charts_cycleplot_compare_month(self):
        expected_df, expected_dict = hf.extract_nwis_df(test_json, interpolate=False)
        actual_fig, actual_ax = charts.cycleplot(expected_df, compare='month')
        self.assertIsInstance(actual_fig, matplotlib.figure.Figure)
        self.assertIsInstance(actual_ax[0], matplotlib.axes.Axes)

    def test_charts_cycleplot_cycle_annualweek(self):
        expected_df, expected_dict = hf.extract_nwis_df(test_json, interpolate=False)
        actual_fig, actual_ax = charts.cycleplot(expected_df, 'annual-week')
        self.assertIsInstance(actual_fig, matplotlib.figure.Figure)
        self.assertIsInstance(actual_ax[0], matplotlib.axes.Axes)

    def test_charts_cycleplot_cycle_annual(self):
        expected_df, expected_dict = hf.extract_nwis_df(test_json, interpolate=False)
        actual_fig, actual_ax = charts.cycleplot(expected_df, 'annual')
        self.assertIsInstance(actual_fig, matplotlib.figure.Figure)
        self.assertIsInstance(actual_ax[0], matplotlib.axes.Axes)

    def test_charts_cycleplot_cycle_annualdate(self):
        expected_df, expected_dict = hf.extract_nwis_df(test_json, interpolate=False)
        actual_fig, actual_ax = charts.cycleplot(expected_df, 'annual-date')
        self.assertIsInstance(actual_fig, matplotlib.figure.Figure)
        self.assertIsInstance(actual_ax[0], matplotlib.axes.Axes)

    def test_charts_cycleplot_cycle_annualmonth(self):
        expected_df, expected_dict = hf.extract_nwis_df(test_json, interpolate=False)
        actual_fig, actual_ax = charts.cycleplot(expected_df, 'annual-month')
        self.assertIsInstance(actual_fig, matplotlib.figure.Figure)
        self.assertIsInstance(actual_ax[0], matplotlib.axes.Axes)

    def test_charts_cycleplot_cycle_weekly(self):
        expected_df, expected_dict = hf.extract_nwis_df(test_json, interpolate=False)
        actual_fig, actual_ax = charts.cycleplot(expected_df, 'weekly')
        self.assertIsInstance(actual_fig, matplotlib.figure.Figure)
        self.assertIsInstance(actual_ax[0], matplotlib.axes.Axes)

    def test_charts_cycleplot_cycle_diurnalsmallest(self):
        expected_df, expected_dict = hf.extract_nwis_df(test_json, interpolate=False)
        actual_fig, actual_ax = charts.cycleplot(expected_df, 'diurnal-smallest')
        self.assertIsInstance(actual_fig, matplotlib.figure.Figure)
        self.assertIsInstance(actual_ax[0], matplotlib.axes.Axes)

    def test_charts_cycleplot_cycle_diurnalhour(self):
        expected_df, expected_dict = hf.extract_nwis_df(test_json, interpolate=False)
        actual_fig, actual_ax = charts.cycleplot(expected_df, 'diurnal-hour')
        self.assertIsInstance(actual_fig, matplotlib.figure.Figure)
        self.assertIsInstance(actual_ax[0], matplotlib.axes.Axes)

    def test_charts_cycleplot_cycle_nonsense_raises_ValueError(self):
        expected_df, expected_dict = hf.extract_nwis_df(test_json, interpolate=False)
        with self.assertRaises(ValueError):
            actual_fig, actual_ax = charts.cycleplot(expected_df, 'nonsense')

if __name__ == '__main__':
    unittest.main(verbosity=2)
