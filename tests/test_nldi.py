# -*- coding: utf-8 -*-
"""
test_nldi
----------------------------------

Tests the functions in the nldi module.
"""
from __future__ import (
        absolute_import,
        print_function,
        division,
        unicode_literals,
        )
from unittest import mock
import unittest
import hydrofunctions as hf
from .fixtures import (
        fakeResponse,
        )


class TestNLDI(unittest.TestCase):

    @mock.patch('requests.get')
    def test_nldi_calls_correct_url(self, mock_get):
        path = 'PATH/PATH/PATH'

        expected_url = 'https://cida.usgs.gov/nldi/' + path
        expected_parameters = {'distance': '150'}
        expected_headers = {'Accept-encoding': 'gzip'}

        expected = fakeResponse()
        expected.status_code = 200
        expected.reason = "any text"

        mock_get.return_value = expected
        actual = hf.get_nldi(path, expected_parameters)
        mock_get.assert_called_once_with(expected_url,
                                         headers=expected_headers,
                                         params = expected_parameters)

    @mock.patch('requests.get')
    def test_nldi_displays_HTML_for_non_200_status(self, mock_get):
        path = ''

        expected_url = 'https://cida.usgs.gov/nldi/' + path
        expected_parameters = None
        expected_headers = {'Accept-encoding': 'gzip'}

        expected = fakeResponse()
        expected.status_code = 400
        expected.text = "expected text"

        mock_get.return_value = expected
        actual = hf.get_nldi()
        mock_get.assert_called_once_with(expected_url,
                                         headers=expected_headers,
                                         params = expected_parameters)
        self.assertEqual(actual.text, expected.text)

    def test_nldi_raises_Error_for_non_200_status(self):
        pass # To test this, I'll need a more realistic mock Requests response.

    @mock.patch('requests.get')
    def test_nldi_raises_HydroNoDataError_if_no_data(self, mock_get):
        path = ''

        expected_url = 'https://cida.usgs.gov/nldi/' + path
        expected_parameters = None
        expected_headers = {'Accept-encoding': 'gzip'}

        expected = fakeResponse()
        expected.status_code = 400
        expected.text = ''

        mock_get.return_value = expected
        with self.assertRaises(hf.HydroNoDataError):
            actual = hf.get_nldi()

        mock_get.assert_called_once_with(expected_url,
                                         headers=expected_headers,
                                         params = expected_parameters)


if __name__ == '__main__':
    unittest.main(verbosity=2)
