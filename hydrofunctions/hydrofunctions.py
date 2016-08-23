# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from hydrofunctions import exceptions


def first():
    print("This is the first function.")
    return True


def raiseit():
    raise exceptions.HydroNoDataError


