#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_usgs_rdb
----------------------------------

Tests for `usgs_rdb` module.

contains the test fixtures:
    - field fixture: a sample rdb file containing field measurements.
        - Header contains four 'messages'
        - dtypes contains one date column
        - 32 columns, 9 data rows (shortened from original)

    - rating_fixture: a sample rdb file containing an 'expanded shift-adjusted'
        rating curve.
        - Header has extra // marks to start every line. ???
        - Header has many different parameters embedded.
        - Two warning messages are in the header
        - 4 columns, 9 data rows (shortened from original)
"""
from __future__ import absolute_import, print_function, division, unicode_literals
from unittest import mock
import unittest

import pandas as pd
import numpy as np

import hydrofunctions as hf
from .fixtures import (
        fakeResponse
        )


# shortened response from this URL: https://waterdata.usgs.gov/pa/nwis/measurements?site_no=01541200&agency_cd=USGS&format=rdb_expanded
field_fixture = """#
# U.S. Geological Survey, National Water Information System
# Surface water measurements
#
# Retrieved: 2019-03-04 10:15:59 EST     (sdww01)
#
# Further descriptions of the columns and codes used can be found at:
# https://help.waterdata.usgs.gov/output-formats#streamflow_measurement_data
#
# Data for the following 1 site(s) are contained in this file
#  USGS 01541200 WB Susquehanna River near Curwensville, PA
# -----------------------------------------------------------------------------------
#
#
agency_cd	site_no	measurement_nu	measurement_dt	tz_cd	q_meas_used_fg	party_nm	site_visit_coll_agency_cd	gage_height_va	discharge_va	measured_rating_diff	gage_va_change	gage_va_time	control_type_cd	discharge_cd	chan_nu	chan_name	meas_type	streamflow_method	velocity_method	chan_discharge	chan_width	chan_area	chan_velocity	chan_stability	chan_material	chan_evenness	long_vel_desc	horz_vel_desc	vert_vel_desc	chan_loc_cd	chan_loc_dist
5s	15s	6s	19d	12s	1s	12s	5s	12s	12s	12s	7s	6s	21s	15s	11n	64s	4s	5s	5s	14s	14s	14s	14s	4s	4s	4s	12s	9s	12s	7s	14s
USGS	01541200	1	1955-09-29		Yes	EVA	USGS	3.66	299	Good	-0.02	0.80	Clear	MEAS	1	Imported Channel 1	UNSP	other		299				UNSP	UNSP	UNSP	unkn	UNSP	UNSP	UNSP
USGS	01541200	2	1955-10-10		Yes	SNA	USGS	3.46	202	Good	0.00	1.00	Clear	MEAS	1	Imported Channel 1	UNSP	other		202				UNSP	UNSP	UNSP	unkn	UNSP	UNSP	UNSP
USGS	01541200	3	1955-11-17		Yes	GAR	USGS	6.77	3490	Good	-0.17	1.30	Clear	MEAS	1	Imported Channel 1	UNSP	other		3490				UNSP	UNSP	UNSP	unkn	UNSP	UNSP	UNSP
USGS	01541200	4	1955-12-18		Yes	YEH	USGS	3.64	193	Unspecified	0.00	0.80	Clear	MEAS	1	Imported Channel 1	UNSP	other		193				UNSP	UNSP	UNSP	unkn	UNSP	UNSP	UNSP
USGS	01541200	5	1956-01-11		Yes	YEH	USGS	3.52	152	Unspecified	0.00	1.00	Clear	MEAS	1	Imported Channel 1	UNSP	other		152				UNSP	UNSP	UNSP	unkn	UNSP	UNSP	UNSP
USGS	01541200	6	1956-02-15		Yes	GAR	USGS	4.87	1280	Good	0.10	1.20	Clear	MEAS	1	Imported Channel 1	UNSP	other		1280				UNSP	UNSP	UNSP	unkn	UNSP	UNSP	UNSP
USGS	01541200	7	1956-03-08		Yes	EVA	USGS	8.94	6750	Good	0.62	1.40	Clear	MEAS	1	Imported Channel 1	CRAN	unspe	unkno	6750	218	1610	4.19	UNSP	UNSP	UNSP	unkn	UNSP	UNSP	UNSP
USGS	01541200	8	1956-03-27		Yes	YEH	USGS	5.05	1410	Good	0.02	1.70	Clear	MEAS	1	Imported Channel 1	UNSP	other		1410				UNSP	UNSP	UNSP	unkn	UNSP	UNSP	UNSP
USGS	01541200	9	1956-04-23		Yes	WHY	USGS	5.08	1380	Good	0.01	1.20	Clear	MEAS	1	Imported Channel 1	UNSP	other		1380				UNSP	UNSP	UNSP	unkn	UNSP	UNSP	UNSP
"""

# shortened response from this URL: https://waterdata.usgs.gov/nwisweb/data/ratings/exsa/USGS.01541303.exsa.rdb
rating_fixture = """# //UNITED STATES GEOLOGICAL SURVEY       http://water.usgs.gov/
# //NATIONAL WATER INFORMATION SYSTEM     http://water.usgs.gov/data.html
# //DATA ARE PROVISIONAL AND SUBJECT TO CHANGE UNTIL PUBLISHED BY USGS
# //RETRIEVED: 2018-09-06 10:25:03
# //WARNING
# //WARNING The stage-discharge rating provided in this file should be
# //WARNING considered provisional and subject to change. Stage-discharge
# //WARNING ratings change over time as the channel features that control
# //WARNING the relation between stage and discharge vary. Users are
# //WARNING cautioned to consider carefully the applicability of this
# //WARNING rating before using it for decisions that concern personal or
# //WARNING public safety or operational consequences.
# //WARNING
# //WARNING This rating does not include any shifts that may have been
# //WARNING used along with this base rating in converting stage to
# //WARNING discharge at this site. Stage data processed with the rating
# //WARNING thus may not match that displayed or published by the USGS.
# //WARNING
# //FILE TYPE="NWIS RATING"
# //DATABASE NUMBER=01 DESCRIPTION=" Standard data base for this site."
# //STATION AGENCY="USGS " NUMBER="01541303       " TIME_ZONE="EST" DST_FLAG=Y
# //STATION NAME="West Branch Susquehanna River at Hyde, PA"
# //LABEL="Discharge (ft^3/s)"
# //PARAMETER CODE="00060"
# //RATING SHIFTED="20180906102503 EST"
# //RATING ID="11.0" TYPE="STGQ" NAME="stage-discharge" AGING=????
# //RATING REMARKS=""
# //RATING EXPANSION="logarithmic"
# //RATING OFFSET1=2.000000E+00
# //RATING_INDEP ROUNDING="????" PARAMETER="Gage height (ft)"
# //RATING_DEP ROUNDING="????" PARAMETER="Discharge (ft^3/s)"
# //RATING_DATETIME BEGIN=20160204024500 BZONE=-05:00 END=20170118000000 EZONE=-05:00 AGING=1
# //RATING_DATETIME BEGIN=20170118000000 BZONE=-05:00 END=-------------- EZONE=--- AGING=1
# //SHIFT_NEXT BEGIN="--------------" BZONE="---" END="--------------" EZONE="---"
# //SHIFT_NEXT STAGE1="---" SHIFT1="---" STAGE2="---" SHIFT2="---" STAGE3="---" SHIFT3="---"
# //SHIFT_NEXT COMMENT=" "
INDEP	SHIFT	DEP	STOR
16N	16N	16N	1S
2.50	0.00	27.90	*
2.51	0.00	29.25
2.52	0.00	30.65
2.53	0.00	32.08
2.54	0.00	33.54
2.55	0.00	35.05
2.56	0.00	36.59
2.57	0.00	38.18
2.58	0.00	39.80
"""


class TestReadRdb(unittest.TestCase):
    """Test the functions that request and parse rdb files from the USGS.

    Test the following topics:
        - ✓Is the correct url formed?
        - What happens when a bad station ID is requested?
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
    def test_read_rdb_returns_4_tuple_of_DF_list_list_list(self):
        test_data = field_fixture
        outputDF, columns, dtype, header = hf.read_rdb(test_data)
        self.assertIs(type(outputDF), pd.core.frame.DataFrame,
                      msg="Read_dbf did not return a dataframe.")
        self.assertIs(type(columns), list, msg="read_dbf did not return columns as a list.")
        self.assertIs(type(dtype), list, msg="read_dbf did not return dtype as a list.")
        self.assertIs(type(header), list, msg="read_dbf did not return header as a list.")


class TestFieldMeas(unittest.TestCase):

    @mock.patch('requests.get')
    def test_field_meas_request_proper_url(self, mock_get):
        sample_site_id = '666'
        expected_url = 'https://waterdata.usgs.gov/pa/nwis/measurements?site_no='\
                       + sample_site_id + '&agency_cd=USGS&format=rdb_expanded'


        expected_status_code = 200
        expected_text = field_fixture

        expected = fakeResponse(code=expected_status_code, text=expected_text)
        expected_headers = {'Accept-encoding': 'gzip'}

        mock_get.return_value = expected
        actual = hf.field_meas(sample_site_id)
        mock_get.assert_called_once_with(expected_url, headers=expected_headers)

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

        self.assertIs(type(actual), pd.core.frame.DataFrame,
                      msg="field_meas did not return a dataframe as expected.")
        actual_rows, actual_cols = actual.shape
        self.assertEqual(actual_rows, expected_rows,
                         msg="field_meas returned the wrong number of rows.")
        self.assertEqual(actual_cols, expected_cols,
                         msg="field_meas returned the wrong number of columns.")
        actual_col_names = actual.columns.values.tolist()
        self.assertListEqual(actual_col_names, expected_col_names,
                              msg="field_meas returned the wrong set of column names.")
        actual_row_2 = actual.iloc[2].values.tolist()
        # This works better when comparing nans, sometimes.
        np.testing.assert_array_equal(actual_row_2, expected_row_2,
                              err_msg="field_meas returned the wrong values for row 2.")


class TestRatingCurve(unittest.TestCase):

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

        mock_get.return_value = expected
        actual = hf.rating_curve(sample_site_id)
        mock_get.assert_called_once_with(expected_url, headers=expected_headers)

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

        self.assertIs(type(actual), pd.core.frame.DataFrame,
                      msg="rating_curve did not return a dataframe as expected.")
        actual_rows, actual_cols = actual.shape
        self.assertEqual(actual_rows, expected_rows,
                         msg="rating_curve returned the wrong number of rows.")
        self.assertEqual(actual_cols, expected_cols,
                         msg="rating_curve returned the wrong number of columns.")
        actual_col_names = actual.columns.values.tolist()
        self.assertListEqual(actual_col_names, expected_col_names,
                              msg="rating_curve returned the wrong set of column names.")
        actual_row_2 = actual.loc[2].values.tolist()
        self.assertListEqual(actual_row_2, expected_row_2,
                              msg="rating_curve returned the wrong values for row 2.")

