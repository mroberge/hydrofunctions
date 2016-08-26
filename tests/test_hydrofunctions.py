#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_hydrofunctions
----------------------------------

Tests for `hydrofunctions` module.
"""
from __future__ import absolute_import, print_function
from unittest import mock
import unittest

from hydrofunctions import hydrofunctions as hf


class TestHydrofunctions(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass
        print("test000")
        assert True

    def test_first_returns_true(self):
        expected = True
        actual = hf.first()
        self.assertEqual(expected, actual, msg="first() did not return True.")

    @mock.patch('requests.get')
    def test_get_nwis_calls_correct_url(self, mock_get):
        """Thanks to
        http://engineroom.trackmaven.com/blog/making-a-mockery-of-python/
        """

        site = 'A'
        service = 'B'
        start = 'C'
        end = 'D'

        expected_url = 'http://waterservices.usgs.gov/nwis/B/?'
        expected_headers = {'max-age': '120', 'Accept-encoding': 'gzip'}
        expected_params = {'format': 'json,1.1', 'sites': 'A', 'endDT': 'D', 'startDT': 'C', 'parameterCd': '00060'}
        expected = 'mock data'

        mock_get.return_value = expected
        actual = hf.get_nwis(site, service, start, end)
        mock_get.assert_called_once_with(expected_url, params=expected_params, headers=expected_headers)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
