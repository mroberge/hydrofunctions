# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 10:14:38 2016

@author: Marty

test_online_resources.py

This module can be used to check whether various online data servers are up
and returning the expected data.

These tests have all been named so that they will not be included in
the normal test suite.

Nose2 will find these tests, but unittest will not. The continuous integration
and setup.py will use unittests, and therefore won't find this test.
"""
from __future__ import absolute_import, print_function
from hydrofunctions import hydrofunctions as hf


def will_NWIS_return_200_response():
    """This test should not be run as a part of the normal test suite.
    This is a resource test only!
    Because of the function name, it is not discoverable by Unittest or pytest.
    """

    expected = 200
    response = hf.get_nwis('01585200', 'dv', '2001-01-01', '2001-01-02')
    actual = response.status_code
    assert expected == actual
    print('NWIS is up and running!')


if __name__ == "__main__":
    will_NWIS_return_200_response()
