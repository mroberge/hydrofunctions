import json
import unittest
from unittest import mock

import hydrofunctions as hf


class TestFloodStage(unittest.TestCase):
    def test_correct_filtering(self):
        stages = {"07144100": {"action_stage": "20"}}
        expected = {"07144100": {"action_stage": "20"}, "07144101": None}
        stations = ["07144100", "07144101"]

        actual = hf.filter_flood_stages(stages, stations)
        self.assertDictEqual(actual, expected)

    @mock.patch("hydrofunctions.waterwatch._get_flood_stages")
    def test_waterwatch_get_stage(self, mock_get_fs):
        site = "07144100"
        expected = {
            site: {
                "action_stage": "20",
                "flood_stage": "22",
                "moderate_flood_stage": "25",
            }
        }
        mock_get_fs.content = json.dumps(
            {
                "sites": [
                    {
                        "site_no": site,
                        "action_stage": "20",
                        "flood_stage": "22",
                        "moderate_flood_stage": "25",
                    }
                ]
            },
            separators=(",", ":"),
        ).encode("utf-8")
        mock_get_fs.return_value = expected

        actual = hf.get_flood_stage(site=site)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
