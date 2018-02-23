# -*- coding: utf-8 -*-
"""
exceptions.py

This module contains all of the custom exceptions defined in this package. The
base class is HydroException, and all custom exceptions are subclasses of
HydroException.

Use the errors like this::

    try:
        #some code here that might return no data
        #more code that might get encoded improperly
    except HydroNoDataError('This site has no data'):
        # handle error here.
    except HydroEncodeError():
        # handle this error here.
    else:
        # code to complete if there is no exception raised.
    finally:
        # code that you want to run whether an exception is raised or not.
        # If an exception wasn't caught, then this code gets run, and the
        # exception gets re-raised after this finally clause gets run.

Keep the try clause short: if you put too many things in there, it can be
difficult to figure out what broke. On the other hand, like in my example
above, it is more readable if you group a series of statements and then
handle their exceptions together.

Example::

    raise HydroNoDataError("Oh no, NWIS doesn't have this data for you!")

https://axialcorps.com/2013/08/29/5-simple-rules-for-building-great-python-packages/
"""
from __future__ import absolute_import, print_function


class HydroException(Exception):
    """
        This is the base class for all exceptions created for the
        HydroFunctions package. This class is not meant to be raised.
    """
    pass


class HydroNoDataError(HydroException):
    """Raised when a service returns an empty dataset or indicates that\
        it has no data for the request.

        Usage::

            raise HydroNoDataError("The NWIS service had no data for this request.")

        Do not catch this error for interactive sessions: The user should
        get a useful message from the error when they try to request something
        that doesn't exits.

        Catch this error in automated systems so that the system can reconsider
        the request and either fix the request or move on to the next
        request.
    """
    pass


class HydroEncodeError(HydroException):
    """An error occured while encoding or decoding an argument"""
    pass


"""
example code::

try:
    #bunch of code from your package
except HydroException:
    '''blanked condition to handle all errors from your package'''
"""
