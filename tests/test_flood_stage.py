import unittest
from unittest import mock
from .fixtures import (
    fakeResponse,
)
from hydrofunctions.flood_stage import get_flood_stage


class TestFloodStage(unittest.TestCase):
    def test_correct_filtering(self):
        stages = {
            "07144100": {
                "action_stage": "20",
                "flood_stage": "22",
                "moderate_flood_stage": "25",
            }
        }
        expected = {
            "07144100": {
                "action_stage": "20",
                "flood_stage": "22",
                "moderate_flood_stage": "25",
            },
            "07144101": None,
        }
        stations = ["07144100", "07144101"]
        self.assertDictEqual(get_flood_stage(stages, stations), expected)

    @mock.patch("requests.get")
    def test_waterwatch_get_stage(self, mock_get):
        site = "07144100"
        expected_format = "json"

        expected_url = "https://waterwatch.usgs.gov/webservices/floodstage"
        expected_headers = {"Accept-encoding": "gzip"}  #We should make sure to set this header, especially if we request all of the stations! (but it might be automatic)
        expected_params = {
            "format": expected_format,
            "sites": site,
        }
        expected = fakeResponse()  # I created 'fakeResponse' so we can have a mock request object to play with
        expected.json = {
            "07144100": {
                "action_stage": "20",
                "flood_stage": "22",
                "moderate_flood_stage": "25",
            }
        }

        mock_get.return_value = expected  # when we call requests, we want it to return a request object.
        actual = hf.get_flood_stage(site)      # finally, we get to the actual test!
        mock_get.assert_called_once_with(   # This is the important test: did the function call Requests properly?
            expected_url, params=expected_params, headers=expected_headers
        )
        self.assertEqual(actual, expected.json)
if __name__ == "__main__":
    unittest.main(verbosity=2)
