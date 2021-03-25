# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 21:13:34 2016

@author: Marty
"""

from __future__ import absolute_import, print_function, division, unicode_literals
import unittest
from unittest import mock
import pandas as pd
from pandas.testing import assert_frame_equal
import numpy as np

from hydrofunctions import station, typing
from .fixtures import (
    fakeResponse,
    recent_only,
)


class TestingNWIS(station.NWIS):
    """
    This subclass of NWIS is for testing all of the NWIS methods except
    __init__, which we will replace. All of the other methods get inherited
    verbatim, so we can test them using TestingNWIS instead of NWIS.
    """

    def __init__(
        self,
        site=None,
        service=None,
        start_date=None,
        end_date=None,
        dataframe=None,
        meta=None,
        start=None,
        end=None,
    ):
        self.site = site
        self.service = service
        self.start_date = start_date
        self.end_date = end_date
        self._dataframe = dataframe
        self.meta = meta
        self.start = start
        self.end = end


class TestStation(unittest.TestCase):
    def test_station_is_obj(self):
        actual = station.Station()
        self.assertIsInstance(actual, station.Station)

    def test_station_site_defaults_to_None(self):
        actual = station.Station()
        self.assertIsNone(actual.site)

    def test_station_id_sets(self):
        expected = "01234567"
        actual = station.Station(expected)
        another = station.Station("23456789")
        self.assertEqual(actual.site, expected)
        self.assertEqual(another.site, "23456789")

    def test_station_dict_returns_dict(self):
        actual = station.Station("first")
        self.assertIsInstance(actual.station_dict, dict)

    def test_multiple_instances_only_one_list(self):
        first = station.Station("first")
        second = station.Station("second")
        self.assertEqual(first.station_dict, second.station_dict)

    def test_station_dict_keeps_keys(self):
        first = station.Station("first")
        second = station.Station("second")
        actual = first.station_dict
        self.assertIn("first", actual)
        self.assertIn("second", actual)
        self.assertEqual(
            len(actual),
            2,
            "The dict length is not equal to the \
                                            number of instances",
        )

    def test_station_dict_returns_instance(self):
        first = station.Station("first")
        second = station.Station("second")
        expected = first
        # Look at the station_dict; does it contain a ref to 'first'?
        actual = second.station_dict["first"]
        self.assertEqual(actual, expected)

    def test_station_subclasses_maintain_same_station_dict(self):
        class Foo(station.Station):
            pass

        foo_inst = Foo("foo")
        station_inst = station.Station("station")
        self.assertIn("station", foo_inst.station_dict)
        self.assertIn("foo", station_inst.station_dict)
        actual = station_inst.station_dict["foo"]
        self.assertIsInstance(actual, Foo)


class TestNWISinit(unittest.TestCase):
    @mock.patch("hydrofunctions.hydrofunctions.get_nwis")
    @mock.patch("hydrofunctions.hydrofunctions.get_nwis_property")
    def test_NWIS_init_check_defaults(self, mock_get_nwis_property, mock_get_nwis):
        default_site = None
        default_service = "dv"
        default_start = None
        default_end = None
        default_parameterCd = "all"
        default_period = None
        default_stateCd = None
        default_countyCd = None
        default_bBox = None

        mock_get_nwis_property.return_value = "expected"
        mock_get_nwis.return_value = fakeResponse()

        station.NWIS()

        mock_get_nwis.assert_called_once_with(
            default_site,
            default_service,
            default_start,
            default_end,
            parameterCd=default_parameterCd,
            period=default_period,
            stateCd=default_stateCd,
            countyCd=default_countyCd,
            bBox=default_bBox,
        )
        self.assertTrue(mock_get_nwis_property)

    @mock.patch("hydrofunctions.hydrofunctions.get_nwis")
    @mock.patch("hydrofunctions.hydrofunctions.get_nwis_property")
    def test_NWIS_init_calls_get_nwis_and_get_prop(
        self, mock_get_nwis_property, mock_get_nwis
    ):
        site = "expected site"
        service = "expected service"
        start = "expected start"
        end = "expected end"
        parameterCd = "expected pCode"
        mock_get_nwis_property.return_value = "expected"
        mock_get_nwis.return_value = fakeResponse()

        station.NWIS(site, service, start, end, parameterCd=parameterCd)
        mock_get_nwis.assert_called_once_with(
            site,
            service,
            start,
            end,
            parameterCd=parameterCd,
            period=None,
            stateCd=None,
            countyCd=None,
            bBox=None,
        )
        self.assertTrue(mock_get_nwis_property)

    @mock.patch("hydrofunctions.hydrofunctions.get_nwis")
    @mock.patch("hydrofunctions.hydrofunctions.get_nwis_property")
    @mock.patch("hydrofunctions.hydrofunctions.extract_nwis_df")
    def test_NWIS_init_sets_url_ok_json(
        self, mock_extract_nwis_df, mock_get_nwis_property, mock_get_nwis
    ):
        expected_url = "expected url"
        expected_ok = True
        expected_json = "expected json"

        mock_get_nwis.return_value = fakeResponse(
            code=200, url=expected_url, json=expected_json
        )
        mock_df = pd.DataFrame(
            np.random.randn(5, 1),
            columns=["A"],
            index=pd.date_range("20130101", periods=5, freq="T"),
        )
        mock_extract_nwis_df.return_value = (mock_df, "expected_dict")

        actual = station.NWIS()
        # self.assertEqual(actual.url, expected_url, "NWIS.__init__() did not set self.url properly.")
        self.assertEqual(
            actual.ok, expected_ok, "NWIS.__init__() did not set self.ok properly."
        )
        self.assertEqual(
            actual.json,
            expected_json,
            "NWIS.__init__() did not set self.json properly.",
        )

    @mock.patch("hydrofunctions.hydrofunctions.get_nwis")
    @mock.patch("hydrofunctions.hydrofunctions.get_nwis_property")
    @mock.patch("hydrofunctions.hydrofunctions.extract_nwis_df")
    def test_NWIS_init_calls_extract_nwis_df(
        self, mock_extract_nwis_df, mock_get_nwis_property, mock_get_nwis
    ):
        expected_json = "expected json"
        mock_get_nwis.return_value = fakeResponse(json=expected_json)
        mock_df = pd.DataFrame(
            np.random.randn(5, 1),
            columns=["A"],
            index=pd.date_range("20130101", periods=5, freq="T"),
        )
        mock_extract_nwis_df.return_value = (mock_df, "expected dict")
        actual = station.NWIS()
        mock_extract_nwis_df.assert_called_once_with(expected_json)

    @mock.patch("hydrofunctions.hydrofunctions.read_parquet")
    def test_NWIS_init_filename_calls_read_parquet(self, mock_read):
        expected_filename = "expected_filename.parquet"
        expected_meta = "expected meta"
        expected_df = pd.DataFrame(
            np.random.randn(5, 1),
            columns=["A"],
            index=pd.date_range("20130101", periods=5, freq="T"),
        )
        mock_start = "expected start"
        mock_end = "expected end"
        mock_read.return_value = (expected_df, expected_meta)
        actual = station.NWIS(file=expected_filename)
        mock_read.assert_called_once_with(expected_filename)
        assert_frame_equal(expected_df, actual._dataframe)
        self.assertEqual(
            expected_meta,
            actual.meta,
            "The metadata were not retrieved by NWIS.read().",
        )

    @mock.patch("hydrofunctions.hydrofunctions.read_parquet")
    @mock.patch("hydrofunctions.hydrofunctions.get_nwis")
    # @mock.patch("hydrofunctions.hydrofunctions.get_nwis_property")
    @mock.patch("hydrofunctions.hydrofunctions.extract_nwis_df")
    @mock.patch("hydrofunctions.hydrofunctions.save_parquet")
    def test_NWIS_init_filename_calls_read_parquet_then_get_nwis(
        self, mock_save, mock_extract_nwis_df, mock_get_nwis, mock_read
    ):
        # Mocks listed in order that they get called.

        # mock_read: pretend file doesn't exist, so return OSError
        #    file exists:
        #         mock_read.return_value = (expected_df, expected_meta)
        #    file doesn't exist, raise error:
        mock_read.side_effect = OSError()

        # mock_get_nwis
        expected_json = "expected json"
        mock_get_nwis.return_value = fakeResponse(json=expected_json)

        # mock_get_nwis_property
        # never called

        # mock_extract_nwis_df
        mock_df = pd.DataFrame(
            np.random.randn(5, 1),
            columns=["A"],
            index=pd.date_range("20130101", periods=5, freq="T"),
        )
        mock_meta = "mock meta"
        mock_extract_nwis_df.return_value = (mock_df, mock_meta)

        # mock_save
        expected_filename = "expected_filename.parquet"
        mock_save.return_value = "expected self"

        # Create an NWIS with a filename, but the filename doesn't exist.
        # so an OSError is returned.
        # So now get_nwis is called, extract_nwis_df, save().
        actual = station.NWIS(file=expected_filename)
        mock_save.assert_called_once_with(expected_filename, mock_df, mock_meta)

    @mock.patch("hydrofunctions.hydrofunctions.get_nwis")
    def test_NWIS_init_request_most_recent_only(self, mock_get_nwis):
        expected_json = recent_only
        expected_url = (
            "https://waterservices.usgs.gov/nwis/dv/?format=json%2C1.1&sites=01541200"
        )
        mock_get_nwis.return_value = fakeResponse(json=expected_json, url=expected_url)
        actual = station.NWIS("01541200")
        self.assertEqual(
            actual.df().shape,
            (2, 4),
            "The dataframe should only have two rows and four columns.",
        )


class TestNWISmethods(unittest.TestCase):
    """
    Tests for NWIS methods
    The following section is for testing all of the NWIS methods
    EXCEPT the NWIS.__init__() method.

    Creating an NWIS instance will always run the __init__ method, which we
    usually don't want to do. It calls a bunch of functions that we test
    elsewhere and it causes a bunch of side effects that we don't want. Yes,
    you can mock all of the functions that __init__ calls, but even then there
    can be unwanted side effects not to mention it can be tedious to mock so
    many different things.

    To test any method other than __init__, we will use the following strategy:
        - create a sub-class of NWIS called TestingNWIS.
        - TestingNWIS has a different __init__ method that allows you to pass
            in a dataframe and any other initial parameter
        - all other methods gets inherited from NWIS, so we can test them.
"""

    def test_NWIS_df_returns_all_columns(self):
        expected_cols = [
            "USGS:01541200:00060:00000_qualifiers",
            "USGS:01541200:00060:00000",
            "USGS:01541200:00065:00000_qualifiers",
            "USGS:01541200:00065:00000",
            "USGS:01541303:00060:00000_qualifiers",
            "USGS:01541303:00060:00000",
            "USGS:01541303:00065:00000_qualifiers",
            "USGS:01541303:00065:00000",
        ]
        data = [
            ["test", 5, "test", 5, "test", 5, "test", 5],
            ["test", 5, "test", 5, "test", 5, "test", 5],
        ]
        test_df = pd.DataFrame(data=data, columns=expected_cols)
        test_nwis = TestingNWIS(dataframe=test_df)
        actual_df = test_nwis.df()
        actual_cols = actual_df.columns.tolist()
        self.assertListEqual(
            actual_cols, expected_cols, "NWIS.df() should return all of the columns."
        )

    def test_NWIS_df_all_returns_all_columns(self):
        cols = [
            "USGS:01541200:00060:00000_qualifiers",
            "USGS:01541200:00060:00000",
            "USGS:01541200:00065:00000_qualifiers",
            "USGS:01541200:00065:00000",
            "USGS:01541303:00060:00000_qualifiers",
            "USGS:01541303:00060:00000",
            "USGS:01541303:00065:00000_qualifiers",
            "USGS:01541303:00065:00000",
        ]
        expected_cols = cols
        data = [
            ["test", 5, "test", 5, "test", 5, "test", 5],
            ["test", 5, "test", 5, "test", 5, "test", 5],
        ]
        test_df = pd.DataFrame(data=data, columns=cols)
        test_nwis = TestingNWIS(dataframe=test_df)
        actual_df = test_nwis.df("all")
        actual_cols = actual_df.columns.tolist()
        self.assertListEqual(
            actual_cols,
            expected_cols,
            "NWIS.df('all') should return all of the columns.",
        )

    def test_NWIS_df_data_returns_data_columns(self):
        cols = [
            "USGS:01541200:00060:00000_qualifiers",
            "USGS:01541200:00060:00000",
            "USGS:01541200:00065:00000_qualifiers",
            "USGS:01541200:00065:00000",
            "USGS:01541303:00060:00000_qualifiers",
            "USGS:01541303:00060:00000",
            "USGS:01541303:00065:00000_qualifiers",
            "USGS:01541303:00065:00000",
        ]
        expected_cols = [
            "USGS:01541200:00060:00000",
            "USGS:01541200:00065:00000",
            "USGS:01541303:00060:00000",
            "USGS:01541303:00065:00000",
        ]

        data = [
            ["test", 5, "test", 5, "test", 5, "test", 5],
            ["test", 5, "test", 5, "test", 5, "test", 5],
        ]
        test_df = pd.DataFrame(data=data, columns=cols)
        test_nwis = TestingNWIS(dataframe=test_df)
        actual_df = test_nwis.df("data")
        actual_cols = actual_df.columns.tolist()
        self.assertListEqual(
            actual_cols,
            expected_cols,
            "NWIS.df('data') should return all of the data columns.",
        )

    def test_NWIS_df_discharge_returns_discharge_data_columns(self):
        cols = [
            "USGS:01541200:00060:00000_qualifiers",
            "USGS:01541200:00060:00000",
            "USGS:01541200:00065:00000_qualifiers",
            "USGS:01541200:00065:00000",
            "USGS:01541303:00060:00000_qualifiers",
            "USGS:01541303:00060:00000",
            "USGS:01541303:00065:00000_qualifiers",
            "USGS:01541303:00065:00000",
        ]

        expected_cols = ["USGS:01541200:00060:00000", "USGS:01541303:00060:00000"]

        data = [
            ["test", 5, "test", 5, "test", 5, "test", 5],
            ["test", 5, "test", 5, "test", 5, "test", 5],
        ]
        test_df = pd.DataFrame(data=data, columns=cols)
        test_nwis = TestingNWIS(dataframe=test_df)
        actual_df = test_nwis.df("discharge")
        actual_cols = actual_df.columns.tolist()
        self.assertListEqual(
            actual_cols,
            expected_cols,
            "NWIS.df('discharge') should return all of the discharge data columns.",
        )

    def test_NWIS_df_q_returns_discharge_data_columns(self):
        cols = [
            "USGS:01541200:00060:00000_qualifiers",
            "USGS:01541200:00060:00000",
            "USGS:01541200:00065:00000_qualifiers",
            "USGS:01541200:00065:00000",
            "USGS:01541303:00060:00000_qualifiers",
            "USGS:01541303:00060:00000",
            "USGS:01541303:00065:00000_qualifiers",
            "USGS:01541303:00065:00000",
        ]

        expected_cols = ["USGS:01541200:00060:00000", "USGS:01541303:00060:00000"]

        data = [
            ["test", 5, "test", 5, "test", 5, "test", 5],
            ["test", 5, "test", 5, "test", 5, "test", 5],
        ]
        test_df = pd.DataFrame(data=data, columns=cols)
        test_nwis = TestingNWIS(dataframe=test_df)
        actual_df = test_nwis.df("q")
        actual_cols = actual_df.columns.tolist()
        self.assertListEqual(
            actual_cols,
            expected_cols,
            "NWIS.df('q') should return all of the discharge data columns.",
        )

    def test_NWIS_df_stage_returns_stage_data_columns(self):
        cols = [
            "USGS:01541200:00060:00000_qualifiers",
            "USGS:01541200:00060:00000",
            "USGS:01541200:00065:00000_qualifiers",
            "USGS:01541200:00065:00000",
            "USGS:01541303:00060:00000_qualifiers",
            "USGS:01541303:00060:00000",
            "USGS:01541303:00065:00000_qualifiers",
            "USGS:01541303:00065:00000",
        ]

        expected_cols = ["USGS:01541200:00065:00000", "USGS:01541303:00065:00000"]

        data = [
            ["test", 5, "test", 5, "test", 5, "test", 5],
            ["test", 5, "test", 5, "test", 5, "test", 5],
        ]
        test_df = pd.DataFrame(data=data, columns=cols)
        test_nwis = TestingNWIS(dataframe=test_df)
        actual_df = test_nwis.df("stage")
        actual_cols = actual_df.columns.tolist()
        self.assertListEqual(
            actual_cols,
            expected_cols,
            "NWIS.df('stage') should return all of the stage data columns.",
        )

    def test_NWIS_df_flags_returns_qualifiers_columns(self):
        cols = [
            "USGS:01541200:00060:00000_qualifiers",
            "USGS:01541200:00060:00000",
            "USGS:01541200:00065:00000_qualifiers",
            "USGS:01541200:00065:00000",
            "USGS:01541303:00060:00000_qualifiers",
            "USGS:01541303:00060:00000",
            "USGS:01541303:00065:00000_qualifiers",
            "USGS:01541303:00065:00000",
        ]

        expected_cols = [
            "USGS:01541200:00060:00000_qualifiers",
            "USGS:01541200:00065:00000_qualifiers",
            "USGS:01541303:00060:00000_qualifiers",
            "USGS:01541303:00065:00000_qualifiers",
        ]

        data = [
            ["test", 5, "test", 5, "test", 5, "test", 5],
            ["test", 5, "test", 5, "test", 5, "test", 5],
        ]
        test_df = pd.DataFrame(data=data, columns=cols)
        test_nwis = TestingNWIS(dataframe=test_df)
        actual_df = test_nwis.df("flags")
        actual_cols = actual_df.columns.tolist()
        self.assertListEqual(
            actual_cols,
            expected_cols,
            "NWIS.df('flags') should return all of the qualifier columns.",
        )

    def test_NWIS_df_flags_q_returns_discharge_qualifiers_columns(self):
        cols = [
            "USGS:01541200:00060:00000_qualifiers",
            "USGS:01541200:00060:00000",
            "USGS:01541200:00065:00000_qualifiers",
            "USGS:01541200:00065:00000",
            "USGS:01541303:00060:00000_qualifiers",
            "USGS:01541303:00060:00000",
            "USGS:01541303:00065:00000_qualifiers",
            "USGS:01541303:00065:00000",
        ]

        expected_cols = [
            "USGS:01541200:00060:00000_qualifiers",
            "USGS:01541303:00060:00000_qualifiers",
        ]

        data = [
            ["test", 5, "test", 5, "test", 5, "test", 5],
            ["test", 5, "test", 5, "test", 5, "test", 5],
        ]
        test_df = pd.DataFrame(data=data, columns=cols)
        test_nwis = TestingNWIS(dataframe=test_df)
        actual_df = test_nwis.df("flags", "q")
        actual_cols = actual_df.columns.tolist()
        self.assertListEqual(
            actual_cols,
            expected_cols,
            "NWIS.df('flags', 'q') should return all of the discharge qualifier columns.",
        )

    def test_NWIS_df_stage_flags_returns_stage_qualifiers_columns(self):
        cols = [
            "USGS:01541200:00060:00000_qualifiers",
            "USGS:01541200:00060:00000",
            "USGS:01541200:00065:00000_qualifiers",
            "USGS:01541200:00065:00000",
            "USGS:01541303:00060:00000_qualifiers",
            "USGS:01541303:00060:00000",
            "USGS:01541303:00065:00000_qualifiers",
            "USGS:01541303:00065:00000",
        ]

        expected_cols = [
            "USGS:01541200:00065:00000_qualifiers",
            "USGS:01541303:00065:00000_qualifiers",
        ]

        data = [
            ["test", 5, "test", 5, "test", 5, "test", 5],
            ["test", 5, "test", 5, "test", 5, "test", 5],
        ]
        test_df = pd.DataFrame(data=data, columns=cols)
        test_nwis = TestingNWIS(dataframe=test_df)
        actual_df = test_nwis.df("stage", "flags")
        actual_cols = actual_df.columns.tolist()
        self.assertListEqual(
            actual_cols,
            expected_cols,
            "NWIS.df('stage', 'flags') should return all of the stage qualifier columns.",
        )

    def test_NWIS_df_crazy_input_raises_ValueError(self):
        cols = [
            "USGS:01541200:00060:00000_qualifiers",
            "USGS:01541200:00060:00000",
            "USGS:01541200:00065:00000_qualifiers",
            "USGS:01541200:00065:00000",
            "USGS:01541303:00060:00000_qualifiers",
            "USGS:01541303:00060:00000",
            "USGS:01541303:00065:00000_qualifiers",
            "USGS:01541303:00065:00000",
        ]

        data = [
            ["test", 5, "test", 5, "test", 5, "test", 5],
            ["test", 5, "test", 5, "test", 5, "test", 5],
        ]
        test_df = pd.DataFrame(data=data, columns=cols)
        test_nwis = TestingNWIS(dataframe=test_df)

        with self.assertRaises(
            ValueError,
            msg="unmatched args such as NWIS.df('crazy', 'input') should cause NWIS.df() to raise a ValueError.",
        ):
            actual_df = test_nwis.df("discharge", "crazy", "input")

    def test_NWIS_df_5digits_returns_param_data_columns(self):
        cols = [
            "USGS:01541200:00060:00000_qualifiers",
            "USGS:01541200:00060:00000",
            "USGS:01541200:00065:00000_qualifiers",
            "USGS:01541200:00065:00000",
            "USGS:01541303:00060:00000_qualifiers",
            "USGS:01541303:00060:00000",
            "USGS:01541303:00065:00000_qualifiers",
            "USGS:01541303:00065:00000",
        ]

        expected_cols = ["USGS:01541200:00065:00000", "USGS:01541303:00065:00000"]

        data = [
            ["test", 5, "test", 5, "test", 5, "test", 5],
            ["test", 5, "test", 5, "test", 5, "test", 5],
        ]
        test_df = pd.DataFrame(data=data, columns=cols)
        test_nwis = TestingNWIS(dataframe=test_df)
        actual_df = test_nwis.df("00065")
        actual_cols = actual_df.columns.tolist()
        self.assertListEqual(
            actual_cols,
            expected_cols,
            "NWIS.df('00065') should return all of the 00065 data columns.",
        )

    def test_NWIS_df_5digits_and_flags_returns_00065_qualifiers_columns(self):
        cols = [
            "USGS:01541200:00060:00000_qualifiers",
            "USGS:01541200:00060:00000",
            "USGS:01541200:00065:00000_qualifiers",
            "USGS:01541200:00065:00000",
            "USGS:01541303:00060:00000_qualifiers",
            "USGS:01541303:00060:00000",
            "USGS:01541303:00065:00000_qualifiers",
            "USGS:01541303:00065:00000",
        ]

        expected_cols = [
            "USGS:01541200:00065:00000_qualifiers",
            "USGS:01541303:00065:00000_qualifiers",
        ]

        data = [
            ["test", 5, "test", 5, "test", 5, "test", 5],
            ["test", 5, "test", 5, "test", 5, "test", 5],
        ]
        test_df = pd.DataFrame(data=data, columns=cols)
        test_nwis = TestingNWIS(dataframe=test_df)
        actual_df = test_nwis.df("00065", "flags")
        actual_cols = actual_df.columns.tolist()
        self.assertListEqual(
            actual_cols,
            expected_cols,
            "NWIS.df('00065', 'flags') should return all of the 00065 _qualifiers columns.",
        )

    def test_NWIS_df_5digits_no_match_raises_ValueError(self):
        cols = [
            "USGS:01541200:00060:00000_qualifiers",
            "USGS:01541200:00060:00000",
            "USGS:01541200:00065:00000_qualifiers",
            "USGS:01541200:00065:00000",
            "USGS:01541303:00060:00000_qualifiers",
            "USGS:01541303:00060:00000",
            "USGS:01541303:00065:00000_qualifiers",
            "USGS:01541303:00065:00000",
        ]

        data = [
            ["test", 5, "test", 5, "test", 5, "test", 5],
            ["test", 5, "test", 5, "test", 5, "test", 5],
        ]
        test_df = pd.DataFrame(data=data, columns=cols)
        test_nwis = TestingNWIS(dataframe=test_df)

        with self.assertRaises(
            ValueError,
            msg="A five-digit input that doesn't match a paramCode should raise a ValueError.",
        ):
            actual_df = test_nwis.df("00000")

    def test_NWIS_df_6digits_raises_ValueError(self):
        cols = [
            "USGS:01541200:00060:00000_qualifiers",
            "USGS:01541200:00060:00000",
            "USGS:01541200:00065:00000_qualifiers",
            "USGS:01541200:00065:00000",
            "USGS:01541303:00060:00000_qualifiers",
            "USGS:01541303:00060:00000",
            "USGS:01541303:00065:00000_qualifiers",
            "USGS:01541303:00065:00000",
        ]

        data = [
            ["test", 5, "test", 5, "test", 5, "test", 5],
            ["test", 5, "test", 5, "test", 5, "test", 5],
        ]
        test_df = pd.DataFrame(data=data, columns=cols)
        test_nwis = TestingNWIS(dataframe=test_df)

        with self.assertRaises(
            ValueError,
            msg="A six-digit input like .df('123456') should raise a ValueError.",
        ):
            actual_df = test_nwis.df("123456")

    def test_NWIS_df_7digits_raises_ValueError(self):
        cols = [
            "USGS:01541200:00060:00000_qualifiers",
            "USGS:01541200:00060:00000",
            "USGS:01541200:00065:00000_qualifiers",
            "USGS:01541200:00065:00000",
            "USGS:01541303:00060:00000_qualifiers",
            "USGS:01541303:00060:00000",
            "USGS:01541303:00065:00000_qualifiers",
            "USGS:01541303:00065:00000",
        ]

        data = [
            ["test", 5, "test", 5, "test", 5, "test", 5],
            ["test", 5, "test", 5, "test", 5, "test", 5],
        ]
        test_df = pd.DataFrame(data=data, columns=cols)
        test_nwis = TestingNWIS(dataframe=test_df)

        with self.assertRaises(
            ValueError,
            msg="A seven-digit input like .df('1234567') should raise a ValueError.",
        ):
            actual_df = test_nwis.df("1234567")

    def test_NWIS_df_8digits_returns_station_data_columns(self):
        cols = [
            "USGS:01541200:00060:00000_qualifiers",
            "USGS:01541200:00060:00000",
            "USGS:01541200:00065:00000_qualifiers",
            "USGS:01541200:00065:00000",
            "USGS:01541303:00060:00000_qualifiers",
            "USGS:01541303:00060:00000",
            "USGS:01541303:00065:00000_qualifiers",
            "USGS:01541303:00065:00000",
        ]

        expected_cols = ["USGS:01541200:00060:00000", "USGS:01541200:00065:00000"]

        data = [
            ["test", 5, "test", 5, "test", 5, "test", 5],
            ["test", 5, "test", 5, "test", 5, "test", 5],
        ]
        test_df = pd.DataFrame(data=data, columns=cols)
        test_nwis = TestingNWIS(dataframe=test_df)
        actual_df = test_nwis.df("01541200")
        actual_cols = actual_df.columns.tolist()
        self.assertListEqual(
            actual_cols,
            expected_cols,
            "NWIS.df('01541200') should return all of the data columns for station 01541200.",
        )

    def test_NWIS_df_8digits_and_flags_returns_station_qualifiers_columns(self):
        cols = [
            "USGS:01541200:00060:00000_qualifiers",
            "USGS:01541200:00060:00000",
            "USGS:01541200:00065:00000_qualifiers",
            "USGS:01541200:00065:00000",
            "USGS:01541303:00060:00000_qualifiers",
            "USGS:01541303:00060:00000",
            "USGS:01541303:00065:00000_qualifiers",
            "USGS:01541303:00065:00000",
        ]

        expected_cols = [
            "USGS:01541200:00060:00000_qualifiers",
            "USGS:01541200:00065:00000_qualifiers",
        ]

        data = [
            ["test", 5, "test", 5, "test", 5, "test", 5],
            ["test", 5, "test", 5, "test", 5, "test", 5],
        ]
        test_df = pd.DataFrame(data=data, columns=cols)
        test_nwis = TestingNWIS(dataframe=test_df)
        actual_df = test_nwis.df("01541200", "flags")
        actual_cols = actual_df.columns.tolist()
        self.assertListEqual(
            actual_cols,
            expected_cols,
            "NWIS.df('01541200', 'flags') should return all of the _qualifiers columns for station '01541200'.",
        )

    def test_NWIS_df_8digits_no_match_raises_ValueError(self):
        cols = [
            "USGS:01541200:00060:00000_qualifiers",
            "USGS:01541200:00060:00000",
            "USGS:01541200:00065:00000_qualifiers",
            "USGS:01541200:00065:00000",
            "USGS:01541303:00060:00000_qualifiers",
            "USGS:01541303:00060:00000",
            "USGS:01541303:00065:00000_qualifiers",
            "USGS:01541303:00065:00000",
        ]

        data = [
            ["test", 5, "test", 5, "test", 5, "test", 5],
            ["test", 5, "test", 5, "test", 5, "test", 5],
        ]
        test_df = pd.DataFrame(data=data, columns=cols)
        test_nwis = TestingNWIS(dataframe=test_df)

        with self.assertRaises(
            ValueError,
            msg="An eight-digit input that doesn't match a station id should raise a ValueError.",
        ):
            actual_df = test_nwis.df("12345678")

    def test_NWIS_df_two_sites_returns_two_site_columns(self):
        cols = [
            "USGS:01541200:00060:00000_qualifiers",
            "USGS:01541200:00060:00000",
            "USGS:01541200:00065:00000_qualifiers",
            "USGS:01541200:00065:00000",
            "USGS:01541303:00060:00000_qualifiers",
            "USGS:01541303:00060:00000",
            "USGS:01541303:00065:00000_qualifiers",
            "USGS:01541303:00065:00000",
        ]

        expected_cols = [
            "USGS:01541200:00060:00000",
            "USGS:01541200:00065:00000",
            "USGS:01541303:00060:00000",
            "USGS:01541303:00065:00000",
        ]

        data = [
            ["test", 5, "test", 5, "test", 5, "test", 5],
            ["test", 5, "test", 5, "test", 5, "test", 5],
        ]
        test_df = pd.DataFrame(data=data, columns=cols)
        test_nwis = TestingNWIS(dataframe=test_df)
        actual_df = test_nwis.df("01541200", "01541303")
        actual_cols = actual_df.columns.tolist()
        self.assertListEqual(
            actual_cols,
            expected_cols,
            "NWIS.df('01541200', '01541303') should return data columns for two sites.",
        )

    def test_NWIS_df_two_params_returns_two_param_columns(self):
        cols = [
            "USGS:01541200:00060:00000_qualifiers",
            "USGS:01541200:00060:00000",
            "USGS:01541200:00065:00000_qualifiers",
            "USGS:01541200:00065:00000",
            "USGS:01541303:00060:00000_qualifiers",
            "USGS:01541303:00060:00000",
            "USGS:01541303:00065:00000_qualifiers",
            "USGS:01541303:00065:00000",
        ]

        expected_cols = [
            "USGS:01541200:00060:00000",
            "USGS:01541200:00065:00000",
            "USGS:01541303:00060:00000",
            "USGS:01541303:00065:00000",
        ]

        data = [
            ["test", 5, "test", 5, "test", 5, "test", 5],
            ["test", 5, "test", 5, "test", 5, "test", 5],
        ]
        test_df = pd.DataFrame(data=data, columns=cols)
        test_nwis = TestingNWIS(dataframe=test_df)
        actual_df = test_nwis.df("00060", "00065")
        actual_cols = actual_df.columns.tolist()
        self.assertListEqual(
            actual_cols,
            expected_cols,
            "NWIS.df('00060', '00065') should return data columns for two parameters.",
        )

    def test_NWIS_df_flag_and_data_returns_flags_and_data_columns(self):
        cols = [
            "USGS:01541200:00060:00000_qualifiers",
            "USGS:01541200:00060:00000",
            "USGS:01541200:00065:00000_qualifiers",
            "USGS:01541200:00065:00000",
            "USGS:01541303:00060:00000_qualifiers",
            "USGS:01541303:00060:00000",
            "USGS:01541303:00065:00000_qualifiers",
            "USGS:01541303:00065:00000",
        ]

        expected_cols = [
            "USGS:01541200:00060:00000_qualifiers",
            "USGS:01541200:00060:00000",
        ]

        data = [
            ["test", 5, "test", 5, "test", 5, "test", 5],
            ["test", 5, "test", 5, "test", 5, "test", 5],
        ]
        test_df = pd.DataFrame(data=data, columns=cols)
        test_nwis = TestingNWIS(dataframe=test_df)
        actual_df = test_nwis.df("flags", "data", "discharge", "01541200")
        actual_cols = actual_df.columns.tolist()
        self.assertListEqual(
            actual_cols,
            expected_cols,
            "NWIS.df('flags', 'data', 'discharge', '01541200') should return data columns and flags for one site and one parameter.",
        )

    def test_NWIS_repr_returns_str(self):
        mock_meta = {
            "USGS:01541200": {
                "siteName": "WB Susquehanna River near Curwensville, PA",
                "siteLatLongSrs": {
                    "srs": "EPSG:4326",
                    "latitude": 40.9614471,
                    "longitude": -78.5191906,
                },
                "timeSeries": {
                    "00060": {
                        "variableFreq": "<Day>",
                        "variableUnit": "ft3/s",
                        "variableDescription": "Discharge, cubic feet per second",
                        "methodDescription": ""
                    }
                },
            }
        }
        mock_start = "expected start"
        mock_end = "expected end"
        test_nwis = TestingNWIS(meta=mock_meta, start=mock_start, end=mock_end)
        expected_repr = "USGS:01541200: WB Susquehanna River near Curwensville, PA\n    00060: <Day>  Discharge, cubic feet per second \nStart: expected start\nEnd:   expected end"
        self.assertEqual(repr(test_nwis), expected_repr)

    def test_NWIS_repr_multisite_multi_param_returns_repr(self):
        self.maxDiff = None
        mock_meta = {
            "USGS:01585200": {
                "siteName": "WEST BRANCH HERRING RUN AT IDLEWYLDE, MD",
                "siteLatLongSrs": {
                    "srs": "EPSG:4326",
                    "latitude": 39.37363889,
                    "longitude": -76.5843333,
                },
                "timeSeries": {
                    "00060": {
                        "variableFreq": "<5 * Minutes>",
                        "variableUnit": "ft3/s",
                        "variableDescription": "Discharge, cubic feet per second",
                        "methodDescription": "",
                    },
                    "00065": {
                        "variableFreq": "<5 * Minutes>",
                        "variableUnit": "ft",
                        "variableDescription": "Gage height, feet",
                        "methodDescription": "",
                    },
                },
            },
            "USGS:01585219": {
                "siteName": "HERRING RUN AT SINCLAIR LANE AT BALTIMORE, MD",
                "siteLatLongSrs": {
                    "srs": "EPSG:4326",
                    "latitude": 39.31796389,
                    "longitude": -76.5551306,
                },
                "timeSeries": {
                    "00010": {
                        "variableFreq": "<5 * Minutes>",
                        "variableUnit": "deg C",
                        "variableDescription": "Temperature, water, degrees Celsius",
                        "methodDescription": "",
                    },
                    "00060": {
                        "variableFreq": "<5 * Minutes>",
                        "variableUnit": "ft3/s",
                        "variableDescription": "Discharge, cubic feet per second",
                        "methodDescription": "",
                    },
                    "00065": {
                        "variableFreq": "<5 * Minutes>",
                        "variableUnit": "ft",
                        "variableDescription": "Gage height, feet",
                        "methodDescription": "",
                    },
                    "00095": {
                        "variableFreq": "<5 * Minutes>",
                        "variableUnit": "uS/cm @25C",
                        "variableDescription": "Specific conductance, water, unfiltered, microsiemens per centimeter at 25 degrees Celsius",
                        "methodDescription": "",
                    },
                    "00400": {
                        "variableFreq": "<5 * Minutes>",
                        "variableUnit": "std units",
                        "variableDescription": "pH, water, unfiltered, field, standard units",
                        "methodDescription": "",
                    },
                },
            },
        }
        mock_start = "expected start"
        mock_end = "expected end"
        test_nwis = TestingNWIS(meta=mock_meta, start=mock_start, end=mock_end)
        expected_repr = """USGS:01585200: WEST BRANCH HERRING RUN AT IDLEWYLDE, MD
    00060: <5 * Minutes>  Discharge, cubic feet per second 
    00065: <5 * Minutes>  Gage height, feet 
USGS:01585219: HERRING RUN AT SINCLAIR LANE AT BALTIMORE, MD
    00010: <5 * Minutes>  Temperature, water, degrees Celsius 
    00060: <5 * Minutes>  Discharge, cubic feet per second 
    00065: <5 * Minutes>  Gage height, feet 
    00095: <5 * Minutes>  Specific conductance, water, unfiltered, microsiemens per centimeter at 25 degrees Celsius 
    00400: <5 * Minutes>  pH, water, unfiltered, field, standard units 
Start: expected start
End:   expected end"""
        self.assertEqual(repr(test_nwis), expected_repr)

    @mock.patch("hydrofunctions.hydrofunctions.save_parquet")
    def test_NWIS_save_calls_save_parquet(self, mock_save):
        expected_filename = "expected_filename.parquet"
        expected_meta = "expected meta"
        expected_df = "expected df"
        mock_start = "expected start"
        mock_end = "expected end"
        test_nwis = TestingNWIS(
            dataframe=expected_df, meta=expected_meta, start=mock_start, end=mock_end
        )
        test_nwis.save(expected_filename)
        mock_save.assert_called_once_with(expected_filename, expected_df, expected_meta)

    @mock.patch("hydrofunctions.hydrofunctions.save_json_gzip")
    def test_NWIS_save_calls_save_gz(self, mock_save):
        expected_filename = "expected_filename.gz"
        expected_json = "expected json"
        test_nwis = TestingNWIS()
        test_nwis.json = expected_json
        test_nwis.save(expected_filename)
        mock_save.assert_called_once_with(expected_filename, expected_json)

    def test_NWIS_save_gz_raises_error_if_no_json(self):
        expected_filename = "expected_filename.gz"
        test_nwis = TestingNWIS()
        with self.assertRaises(AttributeError):
            test_nwis.save(expected_filename)

    def test_NWIS_save_gz_raises_error_if_unrecognized_file_extension(self):
        expected_filename = "expected_filename.weird"
        test_nwis = TestingNWIS()
        with self.assertRaises(OSError):
            test_nwis.save(expected_filename)

    @mock.patch("hydrofunctions.hydrofunctions.read_parquet")
    def test_NWIS_read_calls_read_parquet(self, mock_read):
        expected_filename = "expected_filename.parquet"
        expected_meta = "expected meta"
        expected_df = "expected df"
        mock_start = "expected start"
        mock_end = "expected end"
        mock_read.return_value = (expected_df, expected_meta)
        test_nwis = TestingNWIS()
        test_nwis.read(expected_filename)
        mock_read.assert_called_once_with(expected_filename)
        self.assertEqual(
            expected_df,
            test_nwis._dataframe,
            "NWIS.read() did not retrieve the dataframe properly.",
        )
        self.assertEqual(
            expected_meta,
            test_nwis.meta,
            "The metadata were not retrieved by NWIS.read().",
        )

    @mock.patch("hydrofunctions.hydrofunctions.read_json_gzip")
    def test_NWIS_read_calls_read_json_gz(self, mock_read):
        expected_filename = "expected_filename.json.gz"
        expected_json = recent_only
        mock_read.return_value = expected_json
        expected_meta = {'USGS:01541200': {'siteName': 'WB Susquehanna River near Curwensville, PA', 'siteLatLongSrs': {'srs': 'EPSG:4326', 'latitude': 40.9614471, 'longitude': -78.5191906}, 'timeSeries': {'00010': {'variableFreq': '<0 * Minutes>', 'variableUnit': 'deg C', 'variableDescription': 'Temperature, water, degrees Celsius', 'methodID': '118850', 'methodDescription': ''}, '00060': {'variableFreq': '<0 * Minutes>', 'variableUnit': 'ft3/s', 'variableDescription': 'Discharge, cubic feet per second', 'methodID': '118849', 'methodDescription': ''}}}}
        test_nwis = TestingNWIS()
        test_nwis.read(expected_filename)
        mock_read.assert_called_once_with(expected_filename)
        actual_meta = test_nwis.meta
        self.assertEqual(
            actual_meta,
            expected_meta,
            f"The read function did not parse the json.gz file correctly. It returned"
            f"type {type(actual_meta)} when it was expected to return type {type(expected_meta)}."
            )


"""
    @mock.patch("hydrofunctions.typing.check_parameter_string")
    def test_NWIS_init_calls_check_parameter_string(self, mock_cps):

    def test_NWIS_start_defaults_to_None(self):
        actual = station.NWIS('01541200')
        self.assertIsNone(actual.start_date)

    def test_NWIS_end_defaults_to_None(self):
        actual = station.NWIS('01541200')
        self.assertIsNone(actual.end_date)

    def test_NWIS_setters_work(self):
        site = "01582500"
        service = "dv"
        start = "2011-01-01"
        end = "2011-01-02"
        actual = station.NWIS(site, service, start, end)
        self.assertIsInstance(actual, station.NWIS)
        self.assertEqual(actual.site, site)
        self.assertEqual(actual.service, service)
        self.assertEqual(actual.start_date, start)
        self.assertEqual(actual.end_date, end)
        # self.assertIs(type(actual.fetch), function)

    def test_NWIS_setters_parameterCd(self):
        site = "01582500"
        service = "dv"
        start = "2011-01-01"
        end = "2011-01-02"
        parameterCd = "00065"
        actual = station.NWIS(site, service, start, end,
                              parameterCd=parameterCd)
        self.assertIsInstance(actual, station.NWIS)
        self.assertEqual(actual.site, site)
        self.assertEqual(actual.service, service)
        self.assertEqual(actual.start_date, start)
        self.assertEqual(actual.parameterCd, parameterCd)

    @mock.patch("hydrofunctions.hydrofunctions.get_nwis")
    @mock.patch("hydrofunctions.hydrofunctions.get_nwis_property")
    def test_NWIS_get_data_calls_get_nwis_correctly(self, mock_get_prop, mock_get_nwis):
        site = "01582500"
        service = "dv"
        start = "2011-01-01"
        end = "2011-01-02"
        parameterCd = "00060"

        actual = station.NWIS(site, service, start, end, parameterCd=parameterCd)
        try_it_out = actual.get_data()
        # try_it_out should be a response object, I think
        mock_get_nwis.assert_called_once_with(site, service, start, end,
                                              parameterCd=parameterCd,
                                              period=None, stateCd=None,
                                              countyCd=None, bBox=None)

    @mock.patch("hydrofunctions.hydrofunctions.get_nwis")
    @mock.patch("hydrofunctions.hydrofunctions.get_nwis_property")
    def test_NWIS_get_data_calls_get_nwis_mult_sites(self, mock_get_prop, mock_get_nwis):
        site = ["01638500", "01646502"]
        siteEx = "01638500,01646502"
        service = "dv"
        start = "2011-01-01"
        end = "2011-01-02"
        parameterCd = None
        actual = station.NWIS(site, service, start, end)
        try_it_out = actual.get_data()
        # try_it_out should be an instance of NWIS.
        mock_get_nwis.assert_called_once_with(siteEx, service, start, end,
                                              parameterCd='all',
                                              period=None, stateCd=None,
                                              countyCd=None, bBox=None)

    @mock.patch('requests.get')
    @mock.patch("hydrofunctions.hydrofunctions.get_nwis_property")
    def test_NWIS_get_data_accepts_countyCd_array(self, mock_get_prop, mock_get):
        start = "2017-01-01"
        end = "2017-12-31"
        cnty = ['51059', '51061']
        cnty = typing.check_parameter_string(cnty, 'county')
        service2 = 'dv'

        expected_url = 'https://waterservices.usgs.gov/nwis/dv/?'
        expected_headers = {'max-age': '120', 'Accept-encoding': 'gzip'}
        expected_params = {'format': 'json,1.1', 'sites': None,
                           'stateCd': None, 'countyCd': cnty, 'bBox': None,
                           'parameterCd': None, 'period': None,
                           'startDT': start, 'endDT': end}

        expected = fakeResponse(200)

        mock_get.return_value = expected
        actual = station.NWIS(None, service2, start, countyCd=cnty,
                              end_date=end).get_data()
        mock_get.assert_called_once_with(expected_url, params=expected_params,
                                         headers=expected_headers)

    @mock.patch('requests.get')
    @mock.patch("hydrofunctions.hydrofunctions.get_nwis_property")
    def test_NWIS_get_data_accepts_parameterCd_array(self, mock_get_prop, mock_get):
        site = '01541200'
        start = "2017-01-01"
        end = "2017-12-31"
        service = 'iv'
        parameterCd = ['00060','00065']
        expected_parameterCd = '00060,00065'

        expected_url = 'https://waterservices.usgs.gov/nwis/iv/?'
        expected_headers = {'max-age': '120', 'Accept-encoding': 'gzip'}
        expected_params = {'format': 'json,1.1', 'sites': site,
                           'stateCd': None, 'countyCd': None, 'bBox': None,
                           'parameterCd': expected_parameterCd, 'period': None,
                           'startDT': start, 'endDT': end}

        expected = fakeResponse(200)

        mock_get.return_value = expected
        actual = station.NWIS(site, service, start, end_date=end,
                              parameterCd=parameterCd).get_data()
        mock_get.assert_called_once_with(expected_url, params=expected_params,
                                         headers=expected_headers)

    @mock.patch('requests.get')
    @mock.patch("hydrofunctions.hydrofunctions.get_nwis_property")
    def test_NWIS_get_data_converts_parameterCd_all_to_None(self, mock_get_prop, mock_get):
        site = '01541200'
        service = 'iv'
        parameterCd = 'all'
        expected_parameterCd = None
        expected_url = 'https://waterservices.usgs.gov/nwis/' + service + '/?'
        expected_headers = {'max-age': '120', 'Accept-encoding': 'gzip'}
        expected_params = {'format': 'json,1.1', 'sites': site,
                           'stateCd': None, 'countyCd': None, 'bBox': None,
                           'parameterCd': expected_parameterCd, 'period': None,
                           'startDT': None, 'endDT': None}
        expected = fakeResponse(200)
        mock_get.return_value = expected
        actual = station.NWIS(site, service, parameterCd = parameterCd).get_data()
        mock_get.assert_called_once_with(expected_url, params=expected_params,
                                         headers=expected_headers)

    # Now test .df() and .json()
    @unittest.skip("Test this differently")
    def test_NWIS_df_returns_df(self):
        site = "01582500"
        service = "dv"
        start = "2011-01-01"
        end = "2011-01-02"
        actual = station.NWIS(site, service, start, end)
        # You don't need to test the following like this.
        # Just test that actual.df() returns nothing if you call before get_data()
        # And actual.df() returns a df if you call after .get_data()
        actualdf = actual.get_data().df()  # returns a dataframe
        self.assertIs(type(actualdf), pd.core.frame.DataFrame,
                      msg="Did not return a df")

    def test_NWIS_raises_ValueError_too_many_location_arguments(self):
        with self.assertRaises(ValueError):
            station.NWIS('01541000', stateCd='MD')

    def test_NWIS_raises_ValueError_start_and_period_arguments(self):
        with self.assertRaises(ValueError):
            station.NWIS('01541000', start_date='2013-02-02', period='P9D')
    """


if __name__ == "__main__":
    unittest.main(verbosity=2)
