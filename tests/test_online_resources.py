# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 10:14:38 2016

@author: Marty

test_online_resources.py

This module can be used to check whether various online data servers are up
and returning the expected data.

These tests have all been commented out so that they will not be included in
the normal test suite.
"""
from hydrofunctions import hydrofunctions as hf


def will_get_nwis_return_response():
    """The name of this function should not start with test_ or else nose2
    will find it and run it every time the test suite is run. This is a
    resource test only!
    """

    expected = 200
    response = hf.get_nwis('01585200', 'dv', '2001-01-01', '2001-01-02')
    actual = response.status_code
    assert expected == actual
    print('NWIS is up and running!')

if __name__ == "__main__":
    will_get_nwis_return_response()
