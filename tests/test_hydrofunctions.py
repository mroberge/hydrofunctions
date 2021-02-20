#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_hydrofunctions
----------------------------------

Tests for `hydrofunctions` module.
"""
from __future__ import (
    absolute_import,
    print_function,
    division,
    unicode_literals,
)
from unittest import mock
import unittest
import warnings
import os

from pandas.testing import assert_frame_equal

import pandas as pd
import numpy as np
import pyarrow as pa
import json

print("Pyarrow version: ", pa.__version__)

import hydrofunctions as hf
from .fixtures import (
    fakeResponse,
    daily_dupe,
    daily_dupe_altered,
    tzfail,
    JSON15min2day,
    two_sites_two_params_iv,
    nothing_avail,
    mult_flags,
    diff_freq,
    startDST,
    endDST,
    recent_only,
)


class TestHydrofunctionsParsing(unittest.TestCase):
    """Test the parsing of hf.extract_nwis_df()

    test the following:
        Can it handle multiple qualifier flags?
        how does it encode mult params & mult sites?
        Does it raise HydroNoDataError if nothing returned?

    """

    def test_hf_extract_nwis_df_accepts_response_obj(self):
        fake_response = fakeResponse()
        actual_df, actual_dict = hf.extract_nwis_df(fake_response, interpolate=False)
        self.assertIsInstance(
            actual_df, pd.core.frame.DataFrame, msg="Did not return a df"
        )
        self.assertIsInstance(actual_dict, dict, msg="Did not return a dict.")

    def test_hf_extract_nwis_df_parse_multiple_flags(self):
        actual_df, actual_dict = hf.extract_nwis_df(mult_flags, interpolate=False)
        self.assertIsInstance(
            actual_df, pd.core.frame.DataFrame, msg="Did not return a df"
        )
        self.assertIsInstance(actual_dict, dict, msg="Did not return a dict.")

    def test_hf_extract_nwis_df_parse_two_sites_two_params_iv_return_meta_dict(self):
        actual_df, actual_dict = hf.extract_nwis_df(
            two_sites_two_params_iv, interpolate=False
        )
        self.assertIs(
            type(actual_df), pd.core.frame.DataFrame, msg="Did not return a df"
        )
        self.assertIs(type(actual_dict), dict, msg="Did not return a dict.")
        # TODO: test that metadata is organized correctly

    def test_hf_extract_nwis_df_parse_two_sites_two_params_iv_return_df(self):
        actual_df, actual_dict = hf.extract_nwis_df(
            two_sites_two_params_iv, interpolate=False
        )
        actual_len, actual_width = actual_df.shape
        self.assertIs(
            type(actual_df), pd.core.frame.DataFrame, msg="Did not return a df"
        )
        self.assertEqual(actual_len, 93, "Wrong length for dataframe")
        self.assertEqual(actual_width, 8, "Wrong width for dataframe")
        expected_columns = [
            "USGS:01541000:00060:00000",
            "USGS:01541000:00060:00000_qualifiers",
            "USGS:01541000:00065:00000",
            "USGS:01541000:00065:00000_qualifiers",
            "USGS:01541200:00060:00000",
            "USGS:01541200:00060:00000_qualifiers",
            "USGS:01541200:00065:00000",
            "USGS:01541200:00065:00000_qualifiers",
        ]
        actual_columns = actual_df.columns.values
        self.assertCountEqual(
            actual_columns, expected_columns, "column names don't match expected"
        )
        self.assertTrue(actual_df.index.is_unique, "index has repeated values.")
        self.assertTrue(actual_df.index.is_monotonic, "index is not monotonic.")

    def test_hf_extract_nwis_df_parse_JSON15min2day_return_df(self):
        actual_df, actual_dict = hf.extract_nwis_df(JSON15min2day, interpolate=False)
        actual_len, actual_width = actual_df.shape
        self.assertIs(
            type(actual_df), pd.core.frame.DataFrame, msg="Did not return a df"
        )
        self.assertEqual(actual_len, 192, "Wrong length for dataframe")
        self.assertEqual(actual_width, 2, "Wrong width for dataframe")
        expected_columns = [
            "USGS:03213700:00060:00000",
            "USGS:03213700:00060:00000_qualifiers",
        ]
        actual_columns = actual_df.columns.values
        self.assertCountEqual(
            actual_columns, expected_columns, "column names don't match expected"
        )
        self.assertTrue(actual_df.index.is_unique, "index has repeated values.")
        self.assertTrue(actual_df.index.is_monotonic, "index is not monotonic.")

    def test_hf_extract_nwis_df_parse_mult_flags_return_df(self):
        actual_df, actual_dict = hf.extract_nwis_df(mult_flags, interpolate=False)
        actual_len, actual_width = actual_df.shape
        self.assertIs(
            type(actual_df), pd.core.frame.DataFrame, msg="Did not return a df"
        )
        self.assertEqual(actual_len, 480, "Wrong length for dataframe")
        self.assertEqual(actual_width, 2, "Wrong width for dataframe")
        expected_columns = [
            "USGS:01542500:00060:00000",
            "USGS:01542500:00060:00000_qualifiers",
        ]
        actual_columns = actual_df.columns.values
        self.assertCountEqual(
            actual_columns, expected_columns, "column names don't match expected"
        )
        self.assertTrue(actual_df.index.is_unique, "index has repeated values.")
        self.assertTrue(actual_df.index.is_monotonic, "index is not monotonic.")

    def test_hf_extract_nwis_raises_exception_when_df_is_empty(self):
        empty_response = {"value": {"timeSeries": []}}
        with self.assertRaises(hf.HydroNoDataError):
            hf.extract_nwis_df(empty_response, interpolate=False)

    def test_hf_extract_nwis_raises_exception_when_df_is_empty_nothing_avail(self):
        with self.assertRaises(hf.HydroNoDataError):
            hf.extract_nwis_df(nothing_avail, interpolate=False)

    @unittest.skip(
        "assertWarns errors on Linux. See https://bugs.python.org/issue29620"
    )
    def test_hf_extract_nwis_warns_when_diff_series_have_diff_freq(self):
        with self.assertWarns(hf.HydroUserWarning):
            hf.extract_nwis_df(diff_freq, interpolate=False)

    def test_hf_extract_nwis_accepts_no_startdate_no_period_no_interpolate(self):
        actual_df, actual_dict = hf.extract_nwis_df(recent_only, interpolate=False)
        expected_shape = (
            2,
            4,
        )  # only the most recent data for two parameters, plus qualifiers = 4 columns; 2 rows: different dates.
        self.assertEqual(
            actual_df.shape,
            expected_shape,
            "The dataframe should have four columns and two rows.",
        )

    def test_hf_extract_nwis_accepts_no_startdate_no_period_interpolate(self):
        actual_df, actual_dict = hf.extract_nwis_df(recent_only, interpolate=True)
        expected_shape = (
            2,
            4,
        )  #  only the most recent data for two parameters, plus qualifiers = 4 columns; 2 rows: different dates.
        self.assertEqual(
            actual_df.shape,
            expected_shape,
            "The dataframe should have four columns and two rows.",
        )

    def test_hf_extract_nwis_returns_comma_separated_qualifiers_1(self):
        actual_df, actual_dict = hf.extract_nwis_df(mult_flags, interpolate=False)
        actual_flags_1 = actual_df.loc[
            "2019-01-24T10:30:00.000-05:00", "USGS:01542500:00060:00000_qualifiers"
        ]
        expected_flags_1 = "P,e"
        self.assertEqual(
            actual_flags_1,
            expected_flags_1,
            "The data qualifier flags were not parsed correctly.",
        )

    def test_hf_extract_nwis_returns_comma_separated_qualifiers_2(self):
        actual_df, actual_dict = hf.extract_nwis_df(mult_flags, interpolate=False)
        actual_flags_2 = actual_df.loc[
            "2019-01-28T16:00:00.000-05:00", "USGS:01542500:00060:00000_qualifiers"
        ]
        expected_flags_2 = "P,Ice"
        self.assertEqual(
            actual_flags_2,
            expected_flags_2,
            "The data qualifier flags were not parsed correctly.",
        )

    def test_hf_extract_nwis_replaces_NWIS_noDataValue_with_npNan(self):
        actual_df, actual_dict = hf.extract_nwis_df(mult_flags, interpolate=False)
        actual_nodata = actual_df.loc[
            "2019-01-28T16:00:00.000-05:00", "USGS:01542500:00060:00000"
        ]
        self.assertTrue(
            np.isnan(actual_nodata),
            "The NWIS no data value was not replaced with np.nan. ",
        )

    def test_hf_extract_nwis_adds_missing_tags(self):
        actual_df, actual_dict = hf.extract_nwis_df(mult_flags, interpolate=False)
        actual_missing = actual_df.loc[
            "2019-01-24 17:00:00-05:00", "USGS:01542500:00060:00000_qualifiers"
        ]
        self.assertEqual(
            actual_missing,
            "hf.missing",
            "Missing records should be given 'hf.missing' _qualifier tags.",
        )

    def test_hf_extract_nwis_adds_upsample_tags(self):
        actual_df, actual_dict = hf.extract_nwis_df(diff_freq, interpolate=False)
        actual_upsample = actual_df.loc[
            "2018-06-01 00:15:00-04:00", "USGS:01570500:00060:00000_qualifiers"
        ]
        self.assertEqual(
            actual_upsample,
            "hf.upsampled",
            "New records created by upsampling should be given 'hf.upsample' _qualifier tags.",
        )

    def test_hf_extract_nwis_interpolates(self):
        actual_df, actual_dict = hf.extract_nwis_df(diff_freq, interpolate=True)
        actual_upsample_interpolate = actual_df.loc[
            "2018-06-01 00:15:00-04:00", "USGS:01570500:00060:00000"
        ]
        self.assertEqual(
            actual_upsample_interpolate,
            42200.0,
            "New records created by upsampling should have NaNs replaced with interpolated values.",
        )

    @unittest.skip("This feature is not implemented yet.")
    def test_hf_extract_nwis_interpolates_and_adds_tags(self):
        # Ideally, every data value that was interpolated should have a tag
        # added to the qualifiers that says it was interpolated.
        actual_df, actual_dict = hf.extract_nwis_df(diff_freq, interpolate=True)
        actual_upsample_interpolate_flag = actual_df.loc[
            "2018-06-01 00:15:00-04:00", "USGS:01570500:00060:00000_qualifiers"
        ]
        expected_flag = "hf.interpolated"
        self.assertEqual(
            actual_upsample_interpolate_flag,
            expected_flag,
            "Interpolated values should be marked with a flag.",
        )

    def test_hf_extract_nwis_corrects_for_start_of_DST(self):
        actual_df, actual_dict = hf.extract_nwis_df(startDST, interpolate=False)
        actual_len, width = actual_df.shape
        expected = 284
        self.assertEqual(
            actual_len,
            expected,
            "Three days including the start of DST should have 3 * 24 * 4 = 288 observations, minus 4 = 284",
        )

    def test_hf_extract_nwis_corrects_for_end_of_DST(self):
        actual_df, actual_dict = hf.extract_nwis_df(endDST, interpolate=False)
        actual_len, width = actual_df.shape
        expected = 292
        self.assertEqual(
            actual_len,
            expected,
            "Three days including the end of DST should have 3 * 24 * 4 = 288 observations, plus 4 = 292",
        )

    def test_hf_extract_nwis_can_find_tz_in_tzfail(self):
        actualDF = hf.extract_nwis_df(tzfail, interpolate=False)

    def test_hf_extract_nwis_can_deal_with_duplicated_records_as_input(self):
        actualDF = hf.extract_nwis_df(daily_dupe, interpolate=False)

    def test_hf_extract_nwis_can_deal_with_duplicated_records_that_have_been_altered_as_input(
        self,
    ):
        # What happens if a scientist replaces an empty record with new
        # estimated data, and forgets to discard the old data?
        actualDF = hf.extract_nwis_df(daily_dupe_altered, interpolate=False)

    def test_hf_get_nwis_property(self):
        sites = None
        bBox = (-105.430, 39.655, -104, 39.863)
        # TODO: test should be the json for a multiple site request.
        names = hf.get_nwis_property(JSON15min2day, key="name")
        self.assertIs(type(names), list, msg="Did not return a list")


class TestHydrofunctions(unittest.TestCase):
    @mock.patch("requests.get")
    def test_hf_get_nwis_calls_correct_url(self, mock_get):

        """
        Thanks to
        http://engineroom.trackmaven.com/blog/making-a-mockery-of-python/
        """

        site = "A"
        service = "iv"
        start = "C"
        end = "D"

        expected_url = "https://waterservices.usgs.gov/nwis/" + service + "/?"
        expected_headers = {"Accept-encoding": "gzip", "max-age": "120"}
        expected_params = {
            "format": "json,1.1",
            "sites": "A",
            "stateCd": None,
            "countyCd": None,
            "bBox": None,
            "parameterCd": None,
            "period": None,
            "startDT": "C",
            "endDT": "D",
        }

        expected = fakeResponse()
        expected.status_code = 200
        expected.reason = "any text"

        mock_get.return_value = expected
        actual = hf.get_nwis(site, service, start, end)
        mock_get.assert_called_once_with(
            expected_url, params=expected_params, headers=expected_headers
        )
        self.assertEqual(actual, expected)

    @mock.patch("requests.get")
    def test_hf_get_nwis_calls_correct_url_multiple_sites(self, mock_get):

        site = ["site1", "site2"]
        parsed_site = hf.check_parameter_string(site, "site")
        service = "iv"
        start = "C"
        end = "D"

        expected_url = "https://waterservices.usgs.gov/nwis/" + service + "/?"
        expected_headers = {"max-age": "120", "Accept-encoding": "gzip"}
        expected_params = {
            "format": "json,1.1",
            "sites": parsed_site,
            "stateCd": None,
            "countyCd": None,
            "bBox": None,
            "parameterCd": None,
            "period": None,
            "startDT": "C",
            "endDT": "D",
        }

        expected = fakeResponse()
        expected.status_code = 200
        expected.reason = "any text"

        mock_get.return_value = expected
        actual = hf.get_nwis(site, service, start, end)
        mock_get.assert_called_once_with(
            expected_url, params=expected_params, headers=expected_headers
        )
        self.assertEqual(actual, expected)

    @mock.patch("requests.get")
    def test_hf_get_nwis_service_defaults_dv(self, mock_get):
        site = "01541200"
        expected_service = "dv"

        expected_url = "https://waterservices.usgs.gov/nwis/" + expected_service + "/?"
        expected_headers = {"max-age": "120", "Accept-encoding": "gzip"}
        expected_params = {
            "format": "json,1.1",
            "sites": site,
            "stateCd": None,
            "countyCd": None,
            "bBox": None,
            "parameterCd": None,
            "period": None,
            "startDT": None,
            "endDT": None,
        }
        expected = fakeResponse()
        expected.status_code = 200
        expected.reason = "any text"

        mock_get.return_value = expected
        actual = hf.get_nwis(site)
        mock_get.assert_called_once_with(
            expected_url, params=expected_params, headers=expected_headers
        )
        self.assertEqual(actual, expected)

    @mock.patch("requests.get")
    def test_hf_get_nwis_converts_parameterCd_all_to_None(self, mock_get):
        site = "01541200"
        service = "iv"
        parameterCd = "all"
        expected_parameterCd = None
        expected_url = "https://waterservices.usgs.gov/nwis/" + service + "/?"
        expected_headers = {"max-age": "120", "Accept-encoding": "gzip"}
        expected_params = {
            "format": "json,1.1",
            "sites": site,
            "stateCd": None,
            "countyCd": None,
            "bBox": None,
            "parameterCd": None,
            "period": None,
            "startDT": None,
            "endDT": None,
        }
        expected = fakeResponse()
        expected.status_code = 200
        expected.reason = "any text"

        mock_get.return_value = expected
        actual = hf.get_nwis(site, service, parameterCd=parameterCd)
        mock_get.assert_called_once_with(
            expected_url, params=expected_params, headers=expected_headers
        )
        self.assertEqual(actual, expected)

    def test_hf_get_nwis_raises_ValueError_too_many_locations(self):
        with self.assertRaises(ValueError):
            hf.get_nwis("01541000", stateCd="MD")

    def test_hf_get_nwis_raises_ValueError_start_and_period(self):
        with self.assertRaises(ValueError):
            hf.get_nwis("01541000", start_date="2014-01-01", period="P1D")

    def test_hf_nwis_custom_status_codes_returns_None_for_200(self):
        fake = fakeResponse()
        fake.status_code = 200
        fake.reason = "any text"
        fake.url = "any text"
        self.assertIsNone(hf.nwis_custom_status_codes(fake))

    @unittest.skip(
        "assertWarns errors on Linux. See https://bugs.python.org/issue29620"
    )
    def test_hf_nwis_custom_status_codes_raises_warning_for_non200(self):
        expected_status_code = 400
        bad_response = fakeResponse(code=expected_status_code)
        with self.assertWarns(SyntaxWarning) as cm:
            hf.nwis_custom_status_codes(bad_response)

    def test_hf_nwis_custom_status_codes_returns_status_for_non200(self):
        expected_status_code = 400
        bad_response = fakeResponse(code=expected_status_code)
        actual = hf.nwis_custom_status_codes(bad_response)
        self.assertEqual(actual, expected_status_code)

    def test_hf_calc_freq_returns_Timedelta_and_60min(self):
        test_index = pd.date_range("2014-12-29", "2015-01-03", freq="60T")
        actual = hf.calc_freq(test_index)
        self.assertIsInstance(
            actual, pd.Timedelta, "Calc_freq() should return pd.Timedelta."
        )
        expected = pd.Timedelta("60 minutes")
        self.assertEqual(
            actual, expected, "Calc_freq() should have converted 60T to 60 minutes."
        )

    def test_hf_calc_freq_accepts_Day(self):
        test_index = pd.date_range("2014-12-29", periods=3)
        actual = hf.calc_freq(test_index)
        self.assertIsInstance(
            actual, pd.Timedelta, "Calc_freq() should return pd.Timedelta."
        )
        expected = pd.Timedelta("1 day")
        self.assertEqual(
            actual, expected, "Calc_freq() should have found a 1 day frequency."
        )

    def test_hf_calc_freq_accepts_hour(self):
        test_index = pd.date_range("2014-12-29", freq="1H", periods=30)
        actual = hf.calc_freq(test_index)
        self.assertIsInstance(
            actual, pd.Timedelta, "Calc_freq() should return pd.Timedelta."
        )
        expected = pd.Timedelta("1 hour")
        self.assertEqual(
            actual, expected, "Calc_freq() should have found a 1 hour frequency."
        )

    def test_hf_calc_freq_accepts_1Day_1hour(self):
        test_index = pd.date_range("2014-12-29", freq="1D1H2T", periods=30)
        actual = hf.calc_freq(test_index)
        self.assertIsInstance(
            actual, pd.Timedelta, "Calc_freq() should return pd.Timedelta."
        )
        expected = pd.Timedelta("1 day 1 hour 2 minutes")
        self.assertEqual(
            actual,
            expected,
            "Calc_freq() should have found a 1 day, 1 hour, 2 minutes frequency.",
        )

    def test_hf_calc_freq_accepts_freq_None(self):
        dates = ["2014-12-20", "2014-12-22", "2014-12-24", "2014-12-26"]
        test_index = pd.DatetimeIndex(dates)
        self.assertIsNone(
            test_index.freq,
            msg="The test_index was not properly set up so that test_index.freq is None.",
        )
        actual = hf.calc_freq(test_index)
        self.assertIsInstance(
            actual, pd.Timedelta, "Calc_freq() should return pd.Timedelta."
        )
        expected = pd.Timedelta("48 hours")
        self.assertEqual(
            actual, expected, "Calc_freq() should have returned a 48 hour period."
        )

    def test_hf_calc_freq_accepts_df(self):
        test_index = pd.date_range("2014-12-29", "2014-12-30", freq="1T")
        test_df = pd.DataFrame(index=test_index)
        actual = hf.calc_freq(test_df)
        self.assertIsInstance(
            actual, pd.Timedelta, "Calc_freq() should return pd.Timedelta."
        )
        expected = pd.Timedelta("1 minute")
        self.assertEqual(
            actual, expected, "Calc_freq() should have returned a 1 minute period."
        )

    def test_hf_calc_freq_accepts_difficult_ts_freq_deleted(self):
        test_index = pd.date_range("2014-12-29", "2014-12-30", freq="1H")
        actual = hf.calc_freq(test_index)
        self.assertIsInstance(
            actual, pd.Timedelta, "Calc_freq() should return pd.Timedelta."
        )
        expected = pd.Timedelta("1 hour")
        self.assertEqual(
            actual, expected, "Calc_freq() should have returned a 1 hour frequency."
        )

    @unittest.skip("Difficulty dropping rows.")
    def test_hf_calc_freq_accepts_difficult_ts_freq_deleted_row_dropped(self):
        test_index = pd.date_range("2014-12-29", "2014-12-30", freq="1H")
        test_df = pd.DataFrame(index=test_index)
        # Can't get this to work.
        test_df.drop("2014-12-30", axis=0)
        actual = hf.calc_freq(test_df)
        self.assertIsInstance(
            actual, pd.Timedelta, "Calc_freq() should return pd.Timedelta."
        )
        expected = pd.Timedelta("1 hour")
        self.assertEqual(
            actual, expected, "Calc_freq() should have returned a 1 hour frequency."
        )

    @unittest.skip("")
    def test_hf_calc_freq_accepts_difficult_ts_freq_deleted_no_rows(self):
        pass

    @unittest.skip("")
    def test_hf_calc_freq_accepts_difficult_ts_freq_deleted_no_time_index(self):
        pass

    @unittest.skip("Not sure how to trigger a warning.")
    def test_hf_calc_freq_raises_warning(self):
        test_df = pd.DataFrame(data={"A": [1, 2, 3], "B": [4, 5, 6]})
        actual = hf.calc_freq(test_df)
        self.assertIsInstance(
            actual, pd.Timedelta, "Calc_freq() should return pd.Timedelta."
        )
        expected = pd.Timedelta("15 minutes")
        self.assertEqual(
            actual, expected, "Calc_freq() should have returned a 15 minute frequency."
        )

    def test_hf_select_data_returns_data_cols(self):
        actual_df, actual_dict = hf.extract_nwis_df(two_sites_two_params_iv)
        actual_df = actual_df.reindex(sorted(actual_df.columns), axis=1)
        actual = hf.select_data(actual_df)
        expected = [True, False, True, False, True, False, True, False]
        self.assertListEqual(
            actual.tolist(),
            expected,
            "select_data should return an array of which columns contain the data, not the qualifiers.",
        )

    def test_integration_test_save_read_parquet(self):
        # This test has side effects: it will create a file.
        expected_df, expected_meta = hf.extract_nwis_df(two_sites_two_params_iv)
        filename = "test_filename_delete_me"
        hf.save_parquet(filename, expected_df, expected_meta)
        actual_df, actual_meta = hf.read_parquet(filename)
        assert_frame_equal(expected_df, actual_df)
        self.assertEqual(expected_meta, actual_meta, "The metadata dict has changed.")
        os.remove("test_filename_delete_me")

    @mock.patch("pyarrow.parquet.read_table")
    def test_hf_read_parquet(self, mock_read):
        expected_df, expected_meta = hf.extract_nwis_df(two_sites_two_params_iv)
        expected_table = pa.Table.from_pandas(expected_df)
        meta_dict = expected_table.schema.metadata
        meta_string = json.dumps(expected_meta).encode()
        meta_dict[b"hydrofunctions_meta"] = meta_string
        expected_table = expected_table.replace_schema_metadata(meta_dict)
        mock_read.return_value = expected_table
        actual_df, actual_meta = hf.read_parquet("fake_filename")

        assert_frame_equal(expected_df, actual_df)
        self.assertEqual(expected_meta, actual_meta, "The metadata dict has changed.")

    @mock.patch("pyarrow.parquet.write_table")
    def test_hf_save_parquet(self, mock_write):
        filename = "expected_filename"
        expected_df, expected_meta = hf.extract_nwis_df(two_sites_two_params_iv)
        hf.save_parquet(filename, expected_df, expected_meta)
        pass


if __name__ == "__main__":
    unittest.main(verbosity=2)
