# -*- coding: utf-8 -*-
"""
    exceptions.py

    Use this module to store all exceptions defined in this package.

    Use the errors like this:

    try:
        #some code here that might return no data
        #more code that might get encoded improperly
    except HyrdoNoDataError('This site has no data')
        # handle error here.
    except HydroEncodeError()
        # handle this error here.

https://axialcorps.com/2013/08/29/5-simple-rules-for-building-great-python-packages/
"""
from __future__ import absolute_import, print_function


def second():
    return 2


class HydroException(Exception):
    """
        This is the base class for all exceptions created for the
        HydroFunctions package. This class is not meant to be raised.
    """
    pass


class HydroNoDataError(HydroException):
    """An error if something cannot be loaded from nwis, or nwis has an invalid
       value"""
    pass


class HydroEncodeError(HydroException):
    """An error occured while encoding or decoding an argument"""
    pass


"""
try:
    #bunch of code from your package
except HydroException:
    '''blanked condition to handle all errors from your package'''
"""
