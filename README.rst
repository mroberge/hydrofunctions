===============================
HydroFunctions
===============================


.. image:: https://img.shields.io/pypi/v/hydrofunctions.svg
        :target: https://pypi.python.org/pypi/hydrofunctions

.. image:: https://img.shields.io/travis/mroberge/hydrofunctions.svg
        :target: https://travis-ci.org/mroberge/hydrofunctions

.. image:: https://readthedocs.org/projects/hydrofunctions/badge/?version=latest
        :target: https://hydrofunctions.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://img.shields.io/github/license/mashape/apistatus.svg
        :target: https://github.com/mroberge/hydrofunctions/blob/master/LICENSE
        :alt: MIT license

A suite of convenience functions for exploring water data in IPython.




Features
--------

* Retrieves stream gage data from the USGS NWIS service
* Retrieve data using multiple site numbers, state, or county code
* Preserves NWIS metadata, including NoData values.
* Extracts data into a Pandas dataframe, json, or dict
* Plotting and manipulation through Pandas dataframes!

Read the `online manual <http://hydrofunctions.readthedocs.io/en/master>`_

* Still under development! More features to come!

Basic Usage
-----------

First, import hydrofunctions into your project::

    >>> import hydrofunctions as hf
    >>> %matplotlib inline

    >>> start = '2017-06-01'
    >>> end = '2017-07-14'
    >>> herring = hf.NWIS('01585200', 'dv', start, end)

We've set up our system, now we submit our request for data::

    >>> herring.get_data()
    <hydrofunctions.station.NWIS at 0x127506d6ac8>

Create a Pandas dataframe, then list the first five items::

    >>> herring.df()

--a table with our data appears--

    +------------+--------------------------------------------------+
    |  datetime  | 01585200 - Mean Discharge, cubic feet per second |
    +------------+--------------------------------------------------+
    | 2017-06-01 |                                       0.71       |
    | 2017-06-02 |                                       0.64       |
    | 2017-06-03 |                                       0.61       |
    | 2017-06-04 |                                       0.58       |
    | 2017-06-05 |                                       1.95       |
    +------------+--------------------------------------------------+

Plot the data using Pandas and mathplotlib::

    >>> herring.df().plot()
    --a stream hydrograph appears--

Learn more:

* `More Usage <http://hydrofunctions.readthedocs.io/en/master/usage.html>`_
* A Jupyter Notebook tutorial: <Introduction to Hydrofunctions.ipynb>

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

Visit the `Installation Page <http://hydrofunctions.readthedocs.io/en/master/installation.html>`_ 
in the Users Guide to learn how to install
Anaconda, or if you have problems using the Easy Installation method above.


Credits
---------

Visit `Hydropy <https://github.com/stijnvanhoey/hydropy>`_, which builds upon Pandas for enhanced data selection and plotting of hydrology data.

`WellApplication <https://github.com/inkenbrandt/WellApplication>`_ provides functions for working with dataloggers and USGS well data.

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

MIT License

Copyright (c) 2016, Martin Roberge and contributors
