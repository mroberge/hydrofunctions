# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 11:20:51 2016

@author: Marty

test_validate.py
tests for va;idate.py
"""
from __future__ import absolute_import, print_function, division, unicode_literals
import unittest
from hydrofunctions import validate


class TestValidate(unittest.TestCase):
    def test_validate_check_parameter_string_None_returns_None(self):
        self.assertIsNone(validate.check_parameter_string(None, "site"))

    def test_validate_check_parameter_string_accepts_str_returns_str(self):
        test1 = "any string"
        test2 = "any string"
        test3 = "any unicode string"
        test4 = "a,comma,delimited,list"
        self.assertEqual(
            validate.check_parameter_string(test1, "site"), test1, "test 1 failed"
        )
        self.assertEqual(
            validate.check_parameter_string(test2, "site"), test2, "test 2 failed"
        )
        self.assertEqual(
            validate.check_parameter_string(test3, "site"), test3, "test 3 failed"
        )
        self.assertEqual(
            validate.check_parameter_string(test4, "site"), test4, "test 4 failed"
        )

    def test_validate_check_parameter_string_accepts_list_of_str(self):
        test1 = ["any string"]
        test2 = ["any string", "any string"]
        test3 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        # Why assert True?
        self.assertTrue(validate.check_parameter_string(test1, "site"), "test 1 failed")
        self.assertTrue(validate.check_parameter_string(test2, "site"), "test 2 failed")
        self.assertTrue(validate.check_parameter_string(test3, "site"), "test 3 failed")

    def test_validate_check_parameter_string_accepts_site_county_parameterCd(self):
        text = "text"
        self.assertTrue(validate.check_parameter_string(text, "site"), "test 1 failed")
        self.assertTrue(validate.check_parameter_string(text, "county"), "test 2 failed")
        self.assertTrue(
            validate.check_parameter_string(text, "parameterCd"), "test 3 failed"
        )

    def test_validate_check_parameter_string_raises_TypeError(self):
        not_string = 5
        self.assertRaises(TypeError, validate.check_parameter_string, not_string, "site")

    def test_validate_check_parameter_string_rejects_bad_list(self):
        test1 = []
        test2 = [""]
        test3 = [""]
        test4 = [4]
        test5 = ["good", None]
        test6 = ["good", 9]
        test7 = ["good", ""]
        self.assertRaises(TypeError, validate.check_parameter_string, test1)
        self.assertRaises(TypeError, validate.check_parameter_string, test2)
        self.assertRaises(TypeError, validate.check_parameter_string, test3)
        self.assertRaises(TypeError, validate.check_parameter_string, test4)
        self.assertRaises(TypeError, validate.check_parameter_string, test5)
        self.assertRaises(TypeError, validate.check_parameter_string, test6)
        self.assertRaises(TypeError, validate.check_parameter_string, test7)

    def test_validate_check_NWIS_bBox_accepts_list_tuple_string(self):
        b0 = (-105.43, 39.655, -104.0, 39.863)
        b1 = [-105.43, 39.655, -104.0, 39.863]
        bt = "-105.43,39.655,-104.0,39.863"
        self.assertEqual(validate.check_NWIS_bBox(b0), bt)
        self.assertEqual(validate.check_NWIS_bBox(b1), bt)
        self.assertEqual(validate.check_NWIS_bBox(bt), bt)

    def test_validate_bBox_None_returns_None(self):
        self.assertIsNone(validate.check_NWIS_bBox(None))

    def test_validate_bBox_accepts_list_of_four_latlongs(self):
        goodList = [-80, 20, -70, 30]
        actual = validate.check_NWIS_bBox(goodList)
        expected = "-80,20,-70,30"
        self.assertEqual(actual, expected)

    def test_validate_bBox_raises_TypeError_bad_input(self):
        bad1 = []
        bad2 = [1, 2, 3]  # We only test for insufficient args right now
        self.assertRaises(TypeError, validate.check_NWIS_bBox, bad1)
        self.assertRaises(TypeError, validate.check_NWIS_bBox, bad2)

    def test_validate_check_NWIS_service_accepts_iv_and_dv(self):
        self.assertTrue(validate.check_NWIS_service("iv"))
        self.assertEqual(validate.check_NWIS_service("iv"), "iv")
        self.assertTrue(validate.check_NWIS_service("dv"))
        self.assertEqual(validate.check_NWIS_service("dv"), "dv")

    def test_validate_check_NWIS_service_raises_TypeError(self):
        bad_input = "v"
        self.assertRaises(TypeError, validate.check_NWIS_service, bad_input)

    def test_validate_check_datestr_raises_TypeError(self):
        not_string = 5
        self.assertRaises(TypeError, validate.check_datestr, not_string)

    def test_validate_check_datestr_returns_true_for_good_date(self):
        # re pattern = r"[1-2]\d\d\d-[0-1]\d-[0-3]\d"
        actual = validate.check_datestr("2002-03-03")
        actual = validate.check_datestr("2002-03-03")
        self.assertTrue(actual)

    def test_validate_check_datestr_rejects_bad_date(self):
        # re pattern = r"[1-2]\d\d\d-[0-1]\d-[0-3]\d"
        bad1 = "3002-03-03"
        bad2 = "0000-03-03"
        bad3 = "1111-21-03"
        bad4 = "1111-03-43"
        self.assertRaises(TypeError, validate.check_datestr, bad1)
        self.assertRaises(TypeError, validate.check_datestr, bad2)
        self.assertRaises(TypeError, validate.check_datestr, bad3)
        self.assertRaises(TypeError, validate.check_datestr, bad4)

    def test_validate_check_period_accepts_good_period(self):
        # pattern = r^P\d{1,3}D$
        test1 = "P1D"
        test2 = "P12D"
        test3 = "P999D"  # Only accepts up to 999 days.
        self.assertEqual(validate.check_period(test1), test1)
        self.assertEqual(validate.check_period(test2), test2)
        self.assertEqual(validate.check_period(test3), test3)

    def test_validate_check_period_rejects_bad_period(self):
        # pattern = r^P\d{1,3}D$
        bad1 = "p34d"
        bad2 = "bad"
        bad3 = "P1234D"  # Too long
        bad4 = "P12"
        self.assertRaises(TypeError, validate.check_datestr, bad1)
        self.assertRaises(TypeError, validate.check_datestr, bad2)
        self.assertRaises(TypeError, validate.check_datestr, bad3)
        self.assertRaises(TypeError, validate.check_datestr, bad4)


if __name__ == "__main__":
    unittest.main(verbosity=2)
