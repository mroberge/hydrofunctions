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
    def test_nldi_get_nldi_calls_correct_url(self, mock_get):
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
    def test_nldi_get_nldi_displays_HTML_for_non_200_status(self, mock_get):
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

    def test_nldi_get_nldi_raises_Error_for_non_200_status(self):
        pass # To test this, I'll need a more realistic mock Requests response.
        #mock.auto_spec(requests. ?response?)

    @mock.patch('requests.get')
    def test_nldi_get_nldi_raises_HydroNoDataError_if_no_data(self, mock_get):
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

    @mock.patch('requests.get')
    def test_nldi_get_station_calls_get_nldi_with_correct_url(self, mock_nldi):
        station = 'Fake_Station_ID'
        expected_url = 'https://cida.usgs.gov/nldi/nwissite/USGS-' + station
        expected_parameters = None
        expected_headers = {'Accept-encoding': 'gzip'}

        expected = fakeResponse()
        expected.text = 'mock json'
        mock_nldi.return_value = expected
        actual = hf.get_station(station)
        mock_nldi.assert_called_once_with(expected_url,
                                          headers=expected_headers,
                                          params=expected_parameters)

    @mock.patch('requests.get')
    def test_nldi_get_basin_calls_get_nldi_with_correct_url(self, mock_nldi):
        station = 'Fake_Station_ID'
        expected_url = 'https://cida.usgs.gov/nldi/nwissite/USGS-' + station + '/basin'
        expected_parameters = None
        expected_headers = {'Accept-encoding': 'gzip'}

        expected = fakeResponse()
        expected.text = 'mock json'
        mock_nldi.return_value = expected
        actual = hf.get_basin(station)
        mock_nldi.assert_called_once_with(expected_url,
                                          headers=expected_headers,
                                          params=expected_parameters)

    @mock.patch('requests.get')
    def test_nldi_get_DS_stations_calls_get_nldi_with_correct_url(self, mock_nldi):
        station = 'Fake_Station_ID'
        expected_url = 'https://cida.usgs.gov/nldi/nwissite/USGS-' + station + '/navigate/DM/nwissite'
        expected_parameters = None
        expected_headers = {'Accept-encoding': 'gzip'}

        expected = fakeResponse()
        expected.text = 'mock json'
        mock_nldi.return_value = expected
        actual = hf.get_DS_stations(station)
        mock_nldi.assert_called_once_with(expected_url,
                                          headers=expected_headers,
                                          params=expected_parameters)

    @mock.patch('requests.get')
    def test_nldi_get_DS_stations_calls_get_nldi_with_correct_url_w_distance(self, mock_nldi):
        station = 'Fake_Station_ID'
        distance = '150'
        expected_url = 'https://cida.usgs.gov/nldi/nwissite/USGS-' + station + '/navigate/DM/nwissite?distance=' + distance
        expected_parameters = None
        expected_headers = {'Accept-encoding': 'gzip'}

        expected = fakeResponse()
        expected.text = 'mock json'
        mock_nldi.return_value = expected
        actual = hf.get_DS_stations(station, distance_km=distance)
        mock_nldi.assert_called_once_with(expected_url,
                                          headers=expected_headers,
                                          params=expected_parameters)

    @mock.patch('requests.get')
    def test_nldi_get_DS_channels_calls_get_nldi_with_correct_url(self, mock_nldi):
        station = 'Fake_Station_ID'
        expected_url = 'https://cida.usgs.gov/nldi/nwissite/USGS-' + station + '/navigate/DM'
        expected_parameters = None
        expected_headers = {'Accept-encoding': 'gzip'}

        expected = fakeResponse()
        expected.text = 'mock json'
        mock_nldi.return_value = expected
        actual = hf.get_DS_channels(station)
        mock_nldi.assert_called_once_with(expected_url,
                                          headers=expected_headers,
                                          params=expected_parameters)

    @mock.patch('requests.get')
    def test_nldi_get_DS_channels_calls_get_nldi_with_correct_url_w_distance(self, mock_nldi):
        station = 'Fake_Station_ID'
        distance = '999'
        expected_url = 'https://cida.usgs.gov/nldi/nwissite/USGS-' + station + '/navigate/DM?distance=' + distance
        expected_parameters = None
        expected_headers = {'Accept-encoding': 'gzip'}

        expected = fakeResponse()
        expected.text = 'mock json'
        mock_nldi.return_value = expected
        actual = hf.get_DS_channels(station, distance_km=distance)
        mock_nldi.assert_called_once_with(expected_url,
                                          headers=expected_headers,
                                          params=expected_parameters)

if __name__ == '__main__':
    unittest.main(verbosity=2)
