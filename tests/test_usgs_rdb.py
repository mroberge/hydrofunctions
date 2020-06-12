#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_usgs_rdb
----------------------------------

Tests for `usgs_rdb` module.

"""
from __future__ import absolute_import, print_function, division, unicode_literals
from unittest import mock
import unittest

import pandas as pd
import numpy as np
from requests import Response
from requests.exceptions import HTTPError

import hydrofunctions as hf
from .fixtures import (
        fakeResponse,
        field_fixture,
        rating_fixture,
        peaks_fixture,
        )


class TestReadRdb(unittest.TestCase):
    """Test the functions that request and parse rdb files from the USGS.

    Test the following topics:
        - ✓Is the correct url formed?
        - What happens when a bad station ID is requested?
            - See Issue #71. a 200 status gets returned, so this error is not caught!
        - ✓does the request header ask for zipped data?
        - Is the # header preserved?
        - Can # header variables be retrieved? (such as found in rating fixture)
        - Are the column names retrieved & parsed?
        - Do the dtypes note date columns? (I think that's the only type reliably noted)
        - Does the dataframe get returned with the proper number of rows and columns?
        - Are the column names recorded properly?
        - Are numbers converted to floats?
        - Are strings recorded as strings?
        - Are dates recorded as dates?
        - Are dates recorded with the proper time zone and converted to UTC?
    """
    def test_read_rdb_returns_4_tuple_of_DF_list_list_str(self):
        test_data = field_fixture
        header, outputDF, columns, dtype = hf.read_rdb(test_data)
        self.assertIs(type(outputDF), pd.core.frame.DataFrame,
                      msg="Read_dbf did not return a dataframe.")
        self.assertIs(type(columns), list, msg="read_dbf did not return columns as a list.")
        self.assertIs(type(dtype), list, msg="read_dbf did not return dtype as a list.")
        self.assertIs(type(header), str, msg="read_dbf did not return header as a string.")

    @mock.patch('requests.get')
    def test_get_usgs_RDB_service_returns_response_if_RDB(self, mock_get):
        # Does this call Requests.get properly?
        expected_url = 'expected_url'
        expected_status_code = 200
        expected_text = field_fixture

        expected = fakeResponse(code=expected_status_code, text=expected_text)
        mock_get.return_value = expected

        actual = hf.get_usgs_RDB_service(url=expected_url, headers=None, params=None)
        mock_get.assert_called_once_with(expected_url, headers=None, params=None)

    @mock.patch('requests.get')
    def test_get_usgs_RDB_raises_for_200_but_not_RDB(self, mock_get):
        # The function should raise even if status code is 200 but it doesn't return a RDB file.
        expected_url = 'expected_url'
        expected_status_code = 200
        expected_text = 'not an RDB file'
        expected = fakeResponse(code=expected_status_code, text=expected_text)
        mock_get.return_value = expected

        with self.assertRaises(hf.HydroNoDataError):
            hf.get_usgs_RDB_service(expected_url)

    @mock.patch("requests.get")
    def test_get_usgs_RDB_raises_for_400(self, mock_get):
        # Does this raise for a non-200 status code?
        expected_url = 'expected_url'
        failed_response = mock.Mock(Response)
        failed_response.status_code = 400
        failed_response.text = ''
        failed_response.raise_for_status.side_effect = HTTPError()
        mock_get.return_value = failed_response

        with self.assertRaises(HTTPError):
            hf.get_usgs_RDB_service(expected_url)

    @mock.patch('requests.get')
    def test_site_file(self, mock_get):
        mock_response = mock.Mock(Response)
        mock_response.status_code = 200
        mock_response.text = field_fixture
        mock_get.return_value = mock_response
        actual = hf.site_file('site')
        self.assertIs(type(actual.table), pd.core.frame.DataFrame,
                      msg="site_file did not return a dataframe as expected.")
        self.assertIs(type(actual), hf.hydroRDB,
                      msg="site_file did not return a hydroRDB as expected.")

    @mock.patch('requests.get')
    def test_data_catalog(self, mock_get):
        mock_response = mock.Mock(Response)
        mock_response.status_code = 200
        mock_response.text = field_fixture
        mock_get.return_value = mock_response
        actual = hf.data_catalog('site')
        self.assertIs(type(actual.table), pd.core.frame.DataFrame,
                      msg="data_catalog did not return a dataframe as expected.")
        self.assertIs(type(actual), hf.hydroRDB,
                      msg="data_catalog did not return a hydroRDB as expected.")

    @mock.patch('requests.get')
    def test_field_meas_request_proper_url(self, mock_get):
        sample_site_id = '666'
        expected_url = 'https://waterdata.usgs.gov/nwis/measurements?site_no='\
                       + sample_site_id + '&agency_cd=USGS&format=rdb_expanded'

        expected_status_code = 200
        expected_text = field_fixture

        expected = fakeResponse(code=expected_status_code, text=expected_text)
        expected_headers = {'Accept-encoding': 'gzip'}

        expected_params = None

        mock_get.return_value = expected
        actual = hf.field_meas(sample_site_id)
        mock_get.assert_called_once_with(expected_url, headers=expected_headers, params = expected_params)

    @mock.patch('requests.get')
    def test_field_meas_returns_well_formed_DF(self, mock_get):
        sample_site_id = '026546'

        expected = fakeResponse()
        expected.status_code = 200
        expected.reason = "any text"
        expected.text = field_fixture
        expected_rows = 9
        expected_cols = 31  # 31 = 32 cols - 1 col for index.
        expected_col_names = ['agency_cd', 'site_no', 'measurement_nu',
                              'tz_cd', 'q_meas_used_fg', 'party_nm', 'site_visit_coll_agency_cd',
                              'gage_height_va', 'discharge_va', 'measured_rating_diff',
                              'gage_va_change', 'gage_va_time', 'control_type_cd',
                              'discharge_cd', 'chan_nu', 'chan_name', 'meas_type',
                              'streamflow_method', 'velocity_method', 'chan_discharge',
                              'chan_width', 'chan_area', 'chan_velocity', 'chan_stability',
                              'chan_material', 'chan_evenness', 'long_vel_desc',
                              'horz_vel_desc', 'vert_vel_desc', 'chan_loc_cd',
                              'chan_loc_dist']

        expected_row_2 = ['USGS', '01541200', 3, np.nan, 'Yes', 'GAR',
                          'USGS', 6.77, 3490, 'Good', -0.17, 1.30, 'Clear', 'MEAS',
                          1, 'Imported Channel 1', 'UNSP', 'other', np.nan, 3490,
                          np.nan, np.nan, np.nan, 'UNSP', 'UNSP', 'UNSP', 'unkn',
                          'UNSP', 'UNSP', 'UNSP', np.nan]

        mock_get.return_value = expected
        actual = hf.field_meas(sample_site_id)

        self.assertIs(type(actual.table), pd.core.frame.DataFrame,
                      msg="field_meas did not return a dataframe as expected.")
        actual_rows, actual_cols = actual.table.shape
        self.assertEqual(actual_rows, expected_rows,
                         msg="field_meas returned the wrong number of rows.")
        self.assertEqual(actual_cols, expected_cols,
                         msg="field_meas returned the wrong number of columns.")
        actual_col_names = actual.table.columns.values.tolist()
        self.assertListEqual(actual_col_names, expected_col_names,
                             msg="field_meas returned the wrong set of column names.")
        actual_row_2 = actual.table.iloc[2].values.tolist()
        # This works better when comparing nans, sometimes.
        np.testing.assert_array_equal(actual_row_2, expected_row_2,
                                      err_msg="field_meas returned the wrong values for row 2.")


#************
    @mock.patch('requests.get')
    def test_peaks_request_proper_url(self, mock_get):
        sample_site_id = '666'
        expected_url = 'https://nwis.waterdata.usgs.gov/nwis/peak?site_no='\
                       + sample_site_id + '&agency_cd=USGS&format=rdb'

        expected_status_code = 200
        expected_text = peaks_fixture

        expected = fakeResponse(code=expected_status_code, text=expected_text)
        expected_headers = {'Accept-encoding': 'gzip'}

        expected_params = None

        mock_get.return_value = expected
        actual = hf.peaks(sample_site_id)
        mock_get.assert_called_once_with(expected_url, headers=expected_headers, params=expected_params)

    @mock.patch('requests.get')
    def test_peaks_returns_well_formed_DF(self, mock_get):
        sample_site_id = '026546'

        expected = fakeResponse()
        expected.status_code = 200
        expected.reason = "any text"
        expected.text = peaks_fixture
        expected_rows = 18
        expected_cols = 12  # 12 = 13 cols - 1 col for index.
        expected_col_names = ['agency_cd',
                              'site_no',
                              'peak_tm',
                              'peak_va',
                              'peak_cd',
                              'gage_ht',
                              'gage_ht_cd',
                              'year_last_pk',
                              'ag_dt',
                              'ag_tm',
                              'ag_gage_ht',
                              'ag_gage_ht_cd'
                              ]

        expected_row_2 = ['USGS',
                          '01542500',
                          np.nan,
                          '19600',
                          np.nan,
                          '8.79',
                          '2.0',
                          np.nan,
                          '1941-03-05',
                          np.nan,
                          '8.95',
                          '1.0'
                          ]

        mock_get.return_value = expected
        actual = hf.peaks(sample_site_id)

        self.assertIs(type(actual.table), pd.core.frame.DataFrame,
                      msg="field_meas did not return a dataframe as expected.")
        actual_rows, actual_cols = actual.table.shape
        self.assertEqual(actual_rows, expected_rows,
                         msg="field_meas returned the wrong number of rows.")
        self.assertEqual(actual_cols, expected_cols,
                         msg="field_meas returned the wrong number of columns.")
        actual_col_names = actual.table.columns.values.tolist()
        self.assertListEqual(actual_col_names, expected_col_names,
                             msg="field_meas returned the wrong set of column names.")
        actual_row_2 = actual.table.iloc[2].values.tolist()
        # This works better when comparing nans, sometimes.
        np.testing.assert_array_equal(actual_row_2, expected_row_2,
                                      err_msg="field_meas returned the wrong values for row 2.")


#**************


    @mock.patch('requests.get')
    def test_rating_curve_requests_proper_url(self, mock_get):
        sample_site_id = '095695826546'
        expected_url = "https://waterdata.usgs.gov/nwisweb/data/ratings/exsa/USGS."\
                       + sample_site_id + ".exsa.rdb"

        expected = fakeResponse()
        expected.status_code = 200
        expected.reason = "any text"
        expected.text = rating_fixture
        expected_headers = {'Accept-encoding': 'gzip'}

        expected_params = None

        mock_get.return_value = expected
        actual = hf.rating_curve(sample_site_id)
        mock_get.assert_called_once_with(expected_url, headers=expected_headers, params=expected_params)

    @mock.patch('requests.get')
    def test_rating_curve_returns_well_formed_DF(self, mock_get):
        sample_site_id = '095695826546'

        expected = fakeResponse()
        expected.status_code = 200
        expected.reason = "any text"
        expected.text = rating_fixture
        expected_rows = 9
        expected_cols = 4
        expected_col_names = ['stage', 'shift', 'discharge', 'stor']
        expected_row_2 = [2.52, 0.00, 30.65, np.nan]

        mock_get.return_value = expected
        actual = hf.rating_curve(sample_site_id)

        self.assertIs(type(actual.table), pd.core.frame.DataFrame,
                      msg="rating_curve did not return a dataframe as expected.")
        actual_rows, actual_cols = actual.table.shape
        self.assertEqual(actual_rows, expected_rows,
                         msg="rating_curve returned the wrong number of rows.")
        self.assertEqual(actual_cols, expected_cols,
                         msg="rating_curve returned the wrong number of columns.")
        actual_col_names = actual.table.columns.values.tolist()
        self.assertListEqual(actual_col_names, expected_col_names,
                             msg="rating_curve returned the wrong set of column names.")
        actual_row_2 = actual.table.loc[2].values.tolist()
        self.assertListEqual(actual_row_2, expected_row_2,
                              msg="rating_curve returned the wrong values for row 2.")

    @mock.patch('requests.get')
    def test_stats_requests_proper_url(self, mock_get):
        sample_site_id = '095695826546'
        expected_url = "https://waterservices.usgs.gov/nwis/stat/"

        expected = fakeResponse()
        expected.text = rating_fixture
        expected.status_code = 200
        expected_headers = {'Accept-encoding': 'gzip'}
        expected_params = {
            'statReportType': 'daily',
            'statType': 'all',
            'sites': sample_site_id,
            'format': 'rdb',
            'parameterCd': '00060'
            }

        mock_get.return_value = expected
        actual = hf.stats(sample_site_id, 'daily', parameterCd='00060')
        mock_get.assert_called_once_with(
                expected_url,
                headers=expected_headers,
                params=expected_params)

class Test_hydroRDB(unittest.TestCase):
    """Test the hydroRDB class.

            - Do the RDB functions (peaks, stats, rating_curve, field_meas) return
        hydroRDB object?
        - Does the hydroRDB have a proper repr?
        - Does the hydroRDB have a working __iter__ function?
    """
    def test_hydroRDB_is_obj(self):
        header = 'expected header'
        table = 'expected table'
        columns = 'expected columns'
        dtypes = 'expected dtypes'
        actual = hf.hydroRDB(header, table, columns, dtypes)
        self.assertIsInstance(actual, hf.hydroRDB)

    def test_hydroRDB_has_properties_and_methods(self):
        header = 'expected header'
        table = 'expected table'
        columns = 'expected columns'
        dtypes = 'expected dtypes'
        actual = hf.hydroRDB(header, table, columns, dtypes)
        self.assertIsInstance(actual, hf.hydroRDB)
        self.assertEqual(actual.header, header)
        self.assertEqual(actual.table, table)
        self.assertEqual(actual.columns, columns)
        self.assertEqual(actual.dtypes, dtypes)
        actual_repr = actual.__repr__()
        # actual._repr_html_() requires that table is a dataframe with a _repr_html_()
        #actual_html_repr = actual._repr_html_()
