# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 20:07:38 2018

@author: Marty
"""

from __future__ import absolute_import, print_function, division, unicode_literals
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

    def test_helpers_count_truthy_two_true(self):
        expect_two1 = [False, True, False, True]
        self.assertEqual(hf.count_number_of_truthy(expect_two1), 2, 'test 1 failed.')

        expect_two2 = ['text', False, False, True]
        self.assertEqual(hf.count_number_of_truthy(expect_two2), 2, 'test 2 failed.')

        expect_two3 = [True, True]
        self.assertEqual(hf.count_number_of_truthy(expect_two3), 2, 'test 3 failed.')

        expect_two4 = [5, 'text', False, False]
        self.assertEqual(hf.count_number_of_truthy(expect_two4), 2, 'test 4 failed.')


    def test_helpers_count_truthy_no_true(self):
        expect_no_true1 = [False, False, False, False]
        self.assertEqual(hf.count_number_of_truthy(expect_no_true1), 0, 'test 1 failed.')

        expect_no_true2 = [None, False, False, None]
        self.assertEqual(hf.count_number_of_truthy(expect_no_true2), 0, 'test 2 failed.')

        expect_no_true3 = []
        self.assertEqual(hf.count_number_of_truthy(expect_no_true3), 0, 'test 3 failed.')
