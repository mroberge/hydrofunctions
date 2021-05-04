import unittest

from hydrofunctions.flood_stage import get_flood_stage


class TestFloodStage(unittest.TestCase):

    def test_correct_filtering(self):
        stages = {'07144100': {'action_stage': '20', 'flood_stage': '22', 'moderate_flood_stage': '25'}}
        expected = {'07144100': {'action_stage': '20', 'flood_stage': '22', 'moderate_flood_stage': '25'}, '07144101': None}
        stations = ["07144100", "07144101"]
        self.assertDictEqual(get_flood_stage(stages, stations), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
