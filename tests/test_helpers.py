# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 20:07:38 2018

@author: Marty
"""

from __future__ import absolute_import, print_function
import unittest
from IPython.core.display import HTML
import re

import hydrofunctions as hf


class TestMap(unittest.TestCase):

    def test_helpers_draw_map_returns_HTML_obj(self):
        actual = hf.draw_map()
        self.assertIsInstance(actual, HTML)

    def test_helpers_draw_map_defaults(self):
        # Search through the generated html for the default values.
        widthRE = re.compile(r'width=700')
        heightRE = re.compile(r'height=400')
        urlRE = re.compile(r'http://hydrocloud.org')

        actual = hf.draw_map()
        self.assertTrue(widthRE.search(actual.data))
        self.assertTrue(heightRE.search(actual.data))
        self.assertTrue(urlRE.search(actual.data))
