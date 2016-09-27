# -*- coding: utf-8 -*-
"""
typing.py

Functions for testing that user input is valid. Why do this instead of standard
python duck typing? These functions are meant to enhance an interactive
session for the user. These functions are meant to check a user's parameters
before requesting data from an onlie resource. Otherwise, the server will
return a 404 code and the user will have no idea why. This tries to raise
an exception (usually a TypeError) before a request is made, so that the user
can fix their request. It also tries to provide a helpful error message to an
interactive session user.

Suggested format for these functions:

* first check that the input is a string,
* then do a regular expression to check that the input is more or less valid.
* raise exceptions when user input breaks format.
"""
import re


def check_NWIS_name(input):
    """Checks that the USGS station id is valid.
    """
    if isinstance(input, str):
        return input
    else:
        raise TypeError("NWIS station id should be a string, often in the \
                        form of an eight digit number enclosed in quotes")


def check_NWIS_service(input):
    """Checks that the service is valid: either iv or dv"""
    if input == "iv" or input == "dv":
        return input
    else:
        raise TypeError("The NWIS service type accepts 'dv' for daily values, or 'iv' for instantaneous values.")


def check_datestr(input):
    """Checks that the start_date or end_date parameter is in yyyy-mm-dd format.
    """
    # Use a regular expression to ensure in form of yyyy-mm-dd
    pattern = r"[1-2]\d\d\d-[0-1]\d-[0-3]\d\Z"
    datestr = re.compile(pattern)
    if isinstance(input, str) and datestr.match(input):
        return input
    else:
        raise TypeError('dates should be in the form of "YYYY-MM-DD" \
                        enclosed in quotes. Actual: {}'.format(input))
