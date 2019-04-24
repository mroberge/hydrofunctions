# -*- coding: utf-8 -*-

"""
hydrofunctions.typing
~~~~~~~~~~~~~~~~~~~~~

This module contains functions for testing that user input is valid.

Why 'pre-check' user imputs, instead of using standard
python duck typing? These functions are meant to enhance an interactive
session for the user, and will check a user's parameters
before requesting data from an online resource. Otherwise, the server will
return a 404 code and the user will have no idea why. This tries to raise
an exception (usually a TypeError) before a request is made, so that the user
can fix their request. It also tries to provide a helpful error message to an
interactive session user.

Suggested format for these functions:

* first check that the input is a string,
* then do a regular expression to check that the input is more or less valid.
* raise exceptions when user input breaks format.

-----
"""
from __future__ import absolute_import, print_function, division, unicode_literals
import re


def check_parameter_string(candidate, param):
    parameters = {
        'site': 'NWIS station id(s) should be a string or list of strings,' +
                'often in the form of an eight digit number enclosed in quotes.',
        'parameterCd':
            "NWIS parameter codes are five-digit strings that specify " +
            "the parameter that is being measured at the site. Common " +
            "codes are '00060' for stream stage in feet, '00065' for " +
            "stream discharge in cubic feet per second, and '72019' for " +
            "groundwater levels. Not all sites collect data for all " +
            "parameters. See a complete list of physical parameters here: " +
            "https://help.waterdata.usgs.gov/parameter_cd?group_cd=PHY " +
            "You may request multiple parameters by submitting a comma-" +
            "delimited string of codes with no spaces, or by submitting " +
            "a list of codes, like this: parameterCd = '00065,00060' or " +
            "parameterCd = ['00065', '00060'] ",
        'county':
            "The NWIS county parameter accepts a five-digit string or " +
            "a list of five-digit strings to select all of the sites " +
            "within a county or list of counties. " +
            "Example: '51059' or ['51059', '51061'] are acceptable.",
        'state':
            "This parameter uses US two-letter postal codes " +
            "such as 'MD' for Maryland or 'AZ' for Arizona.",
        'default':
            'This parameter should be a string or a list of strings.'
        }
    if param in parameters:
        msg = parameters[param] + ' Actual value: {}'.format(candidate)
    else:
        msg = 'This parameter should be a string or a list of strings.' + \
          ' Actual value: {}'.format(candidate)

    if candidate is None:
        return None
    elif isinstance(candidate, str) and candidate:
        return candidate
    elif (isinstance(candidate, list) or isinstance(candidate, tuple)) and candidate:
        for s in candidate:
            if not isinstance(s, str):
                raise TypeError(msg + "   bad element: {}".format(s))
        return ','.join([str(s) for s in candidate])
    else:
        raise TypeError(msg)


def check_NWIS_bBox(input):
    """Checks that the USGS bBox is valid.
    """
    msg = 'NWIS bBox should be a string, list of strings, or tuple ' + \
          'containing the longitude and latitude of the lower left corner ' + \
          'of the bounding box, followed by the longitude and latitude ' + \
          'of the upper right corner of the bounding box. Most often in ' + \
          'the form of "ll_long,ll_lat,ur_long,ur_lat" . ' + \
          'All latitude and longitude values should have less than 8 ' + \
          'places. ' + \
          'Actual value: {}'.format(input)
    if input is None:
        return None
    # assume that if it is a string it will be fine as is.
    # don't accept a series of sites in a single string.
    # Test for and reject empty strings: empty strings are false.
    if isinstance(input, str) and input:
        t = input.split(',')
        if len(t) < 4:
            raise TypeError(msg)
        return input
    # test for input is a list and it is not empty
    elif (isinstance(input, list) or isinstance(input, tuple)) and input:
        if len(input) < 4:
            raise TypeError(msg)
        # format:  [-83.000000, 36.500000, -81.000000, 38.500000] ==> '-83.000000,36.500000,-81.000000,38.500000'
        return ','.join([str(s) for s in input])
    else:
        raise TypeError(msg)


def check_NWIS_service(input):
    """Checks that the service is valid: either iv or dv"""
    if input is None:
        return None
    if input == "iv" or input == "dv":
        return input
    else:
        raise TypeError("The NWIS service type accepts 'dv' for daily values, "
                        "or 'iv' for instantaneous values. Actual value: "
                        "{}".format(input))


def check_datestr(input):
    """Checks that the start_date or end_date parameter is in yyyy-mm-dd format.
    """
    # Use a regular expression to ensure in form of yyyy-mm-dd
    if input is None:
        return None
    pattern = r"[1-2]\d\d\d-[0-1]\d-[0-3]\d\Z"
    datestr = re.compile(pattern)
    if isinstance(input, str) and datestr.match(input):
        return input
    else:
        raise TypeError("Dates should be a string in the form of 'YYYY-MM-DD' "
                        "enclosed in quotes. Actual value: {}".format(input))


def check_period(input):
    """Checks that the period parameter in is the P##D format, where ## is
    the number of days before now.
    """
    if input is None:
        return None
    # TODO: check how many days maximum NWIS is willing to respond to.
    # This pattern sets a maximum of 999 days (between 1 and 3 digits).
    pattern = r"^P\d{1,3}D$"
    periodstr = re.compile(pattern)
    if isinstance(input, str) and periodstr.match(input):
        return input
    else:
        raise TypeError("Period should be a string in the form of 'PxD', "
                        "where x represents the number of days before today, "
                        "with a maximum of 999 days. "
                        "Example: to request the previous 10 days, "
                        "enter 'period=P10D'. Actual value entered: {}"
                        .format(input))
