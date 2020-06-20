===============================
HydroFunctions
===============================

.. image:: https://img.shields.io/pypi/v/hydrofunctions.svg
        :target: https://pypi.python.org/pypi/hydrofunctions
        :alt: Visit Hydrofunctions on PyPI

.. image:: https://img.shields.io/travis/mroberge/hydrofunctions.svg
        :target: https://travis-ci.org/mroberge/hydrofunctions
        :alt: Unit Testing Status

.. image:: https://codecov.io/gh/mroberge/hydrofunctions/branch/master/graph/badge.svg
        :target: https://codecov.io/gh/mroberge/hydrofunctions
        :alt: Code Coverage Status

.. image:: https://readthedocs.org/projects/hydrofunctions/badge/?version=latest
        :target: https://hydrofunctions.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://img.shields.io/github/license/mashape/apistatus.svg
        :target: https://github.com/mroberge/hydrofunctions/blob/master/LICENSE
        :alt: MIT license

a suite of convenience functions for exploring water data in Python.

Features
--------

* Retrieves stream data from the USGS NWIS service
* Select data using multiple site numbers, by state, county codes, or a boundary box
* Preserves NWIS metadata, including NoData values
* Helpful error messages to help you write valid requests
* Extracts data into a Pandas dataframe, json, or dict
* Plot beautiful graphs in Jupyter Notebooks
   * hydrographs (or time series of any data)
   * flow duration charts
   * cycle plots to illustrate annual or diurnal cycles
   * Interactive map for finding stream gauge ID numbers
* Plotting and manipulation through Pandas dataframes
* Retrieve USGS rating curves, peak discharges, field notes, and site files for gauging stations
* Retrieve USGS daily, monthly, and annual statistics for gauging stations
* Saves data in compact, easy-to-use parquet files instead of requesting the same dataset repeatedly
* **Massive Users Guide that makes Hydrology AND Data Science easy!**

Still in active development! Let me know what features you want!

Read the `Users Guide <https://hydrofunctions.readthedocs.io/en/master>`_ for more details.


Basic Usage
-----------

First, import hydrofunctions into your project and enable automatic chart
display::

    >>> import hydrofunctions as hf
    >>> %matplotlib inline

Create NWIS data object to hold our request and the data we will retrieve.
We will request the daily values ('dv') for site '0158520' for the past
55 days::

    >>> herring = hf.NWIS('01585200', 'dv', period='P55D')
    Requested data from https://waterservices.usgs.gov/nwis/iv/?format=json%2C1.1&sites=01585200&period=P55D


Find out what data we received::

    >>> herring
    USGS:01585200: WEST BRANCH HERRING RUN AT IDLEWYLDE, MD
        00060: <5 * Minutes>  Discharge, cubic feet per second
        00065: <5 * Minutes>  Gage height, feet
    Start: 2019-05-25 01:05:00+00:00
    End:   2019-07-19 19:05:00+00:00

This tells us the name of our site, and gives a list of the parameters that we
have. For each parameter it lists how frequently the data were collected, and
it show the common name of the parameter and its units.

Create a dataframe from our data, and list the first five items::

    >>> herring.df().head()

*--a table with our data appears--*

    +------------------------------+---------------------------+
    |          datetimeUTC         | USGS:01585200:00060:00000 |
    +------------------------------+---------------------------+
    |   2019-05-25 01:05:00+00:00  |                1.57       |
    +------------------------------+---------------------------+
    |   2019-05-25 01:10:00+00:00  |                1.57       |
    +------------------------------+---------------------------+
    |   2019-05-25 01:15:00+00:00  |                1.51       |
    +------------------------------+---------------------------+
    |   2019-05-25 01:20:00+00:00  |                1.57       |
    +------------------------------+---------------------------+
    |   2019-05-25 01:25:00+00:00  |                1.57       |
    +------------------------------+---------------------------+

Plot the data using built-in methods from Pandas and mathplotlib::

    >>> herring.df().plot()

*--a stream hydrograph appears--*

.. image:: https://raw.githubusercontent.com/mroberge/hydrofunctions/master/_static/HerringHydrograph.png
        :alt: a stream hydrograph for Herring Run

Easy Installation
-----------------

The easiest way to install Hydrofunctions is by typing this from your
command line:

.. code-block:: console

    $ pip install hydrofunctions


Hydrofunctions depends upon Pandas and numerous other scientific packages
for Python. `Anaconda <https://docs.anaconda.com/anaconda/install/>`_
is an easy, safe, open-source method for downloading everything and avoiding
conflicts with other versions of Python that might be running on your
computer.


Other Projects You Should See
-----------------------------

`WellApplication <https://github.com/inkenbrandt/WellApplication>`_ a Python package that provides functions for working with dataloggers and USGS well data.

MIT License

Copyright (c) 2016, Martin Roberge and contributors