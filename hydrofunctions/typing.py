# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 11:20:36 2016

@author: Marty

typing.py

Functions for testing that user input is valid.
Duck typing, sure.
But if these functions get used in an interactive session, it would be helpful
if the user knew why the USGS was returning a 404.

These functions can be used as needed, I guess.

format: check for type, then do a regular expression.
return exceptions when input breaks format.
"""
import re


def check_NWIS_station_id(input):
    if isinstance(input, str):
        return True
    else:
        raise TypeError("NWIS station id should be a string, often in the" +
                        "form of an eight digit number enclosed in quotes")


def check_datestr(input):
    # Use a regular expression to ensure in form of yyyy-mm-dd
    pattern = r"[1-2]\d\d\d-[0-1]\d-[0-3]\d\Z"
    datestr = re.compile(pattern)
    if isinstance(input, str) and datestr.match(input):
        return True
    else:
        raise TypeError('dates should be in the form of "YYYY-MM-DD" ' +
                        "enclosed in quotes")
