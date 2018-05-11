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
* Retrieve data using multiple site numbers, state, county codes, or boundary box
* Preserves NWIS metadata, including NoData values
* Helpful error messages to help you write valid requests
* Extracts data into a Pandas dataframe, json, or dict
* Plotting and manipulation through Pandas dataframes
* Interactive map for finding stream gage ID numbers
* Still in early development! More features to come!

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

We've set up our system, now we submit our request for data and get a
response::

    >>> herring.get_data()
    <hydrofunctions.station.NWIS at 0x127506d6ac8>

Create a dataframe from our data, and list the first five items::

    >>> herring.df().head()

*--a table with our data appears--*

    +------------+--------------------------------------------------+
    |  datetime  | 01585200 - Mean Discharge, cubic feet per second |
    +------------+--------------------------------------------------+
    | 2017-06-01 |                                       0.71       |
    +------------+--------------------------------------------------+
    | 2017-06-02 |                                       0.64       |
    +------------+--------------------------------------------------+
    | 2017-06-03 |                                       0.61       |
    +------------+--------------------------------------------------+
    | 2017-06-04 |                                       0.58       |
    +------------+--------------------------------------------------+
    | 2017-06-05 |                                       1.95       |
    +------------+--------------------------------------------------+

Plot the data using built-in methods from Pandas and mathplotlib::

    >>> herring.df().plot()

*--a stream hydrograph appears--*

.. image:: _static/HerringHydrograph.png
        :alt: a stream hydrograph for Herring Run

Draw an interactive map in a Jupyter Notebook:

.. image:: _static/draw_map.jpg
        :alt: a map in an interactive Jupyter Notebook.

Learn more:

* `More usage <https://hydrofunctions.readthedocs.io/en/master/usage.html>`_ tips
* `Introduction to Hydrofunctions <https://github.com/mroberge/hydrofunctions/blob/master/Introduction%20to%20Hydrofunctions.ipynb>`_, a Jupyter Notebook with a quick tutorial.

Easy Installation
-----------------

The easiest way to install Hydrofunctions is by typing this from your 
command line:

.. code-block:: console

    $ pip install hydrofunctions


Hydrofunctions depends upon Pandas and numerous other scientific packages
for Python. `Anaconda <https://www.continuum.io/open-source-core-modern-software>`_ 
is an easy, safe, open-source method for downloading everything and avoiding
conflicts with other versions of Python that might be running on your
computer.

Visit the `Installation Page <https://hydrofunctions.readthedocs.io/en/master/installation.html>`_ 
in the Users Guide to learn how to install
Anaconda, or if you have problems using the Easy Installation method above.


Other Projects You Should See
-----------------------------

`Hydropy <https://github.com/stijnvanhoey/hydropy>`_, a Python package that builds upon Pandas for enhanced data selection and plotting of hydrology data.

`WellApplication <https://github.com/inkenbrandt/WellApplication>`_ a Python package that provides functions for working with dataloggers and USGS well data.

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

MIT License

Copyright (c) 2016, Martin Roberge and contributors
