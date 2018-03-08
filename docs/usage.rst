====================
Using Hydrofunctions
====================


First, import hydrofunctions into your project::

    >>> import hydrofunctions as hf

Next, request data from the USGS National Water Information System (NWIS)::

    >>> site = '01582500'
    >>> start = '2015-05-10'
    >>> end = '2015-05-15'
    >>> response = hf.get_nwis(site, 'dv', start, end)

Examine the response object::

    >>> response.ok
    True

    >>> response.status_code
    200

    >>> response.json()
    {'name':'ns1:timeSeriesResponseType','declaredType':'org.cuahsi.waterml.TimeSeriesResponseType' .... }

List all of the different attributes and methods with dir()::

    >>> dir(response)


Functions that use the response object
--------------------------------------

Extract the full json response from the data provider::

    >>> my_dict = response.json()
    >>> my_dict
    {'declaredType': 'org.cuahsi.waterml.TimeSeriesResponseType',
     'globalScope': True,
     ...
    }

Extract a Pandas dataframe from the response::

    >>> my_data_frame = hf.extract_nwis_df(response)
    >>> my_data_frame
                value
    datetime
    2015-05-10  133.0
    2015-05-11  131.0
    2015-05-12  131.0
    2015-05-13  129.0
    2015-05-14  114.0
    2015-05-15  109.0


Using the NWIS object to request data
-------------------------------------

A second method for requesting data is to use the NWIS object to store your
response and the extracted data.

First, import hydrofunctions into your project and enable automatic chart 
display::

    >>> import hydrofunctions as hf
    >>> %matplotlib inline

Now set up the data request, much as we did with the `hf.get_nwis()` function,
but this time we'll use the hf.NWIS object, and we'll request the previous
20 days instead of between two dates::

    >>> myTime = 'P20D'
    >>> herring = hf.NWIS('01585200', 'dv', period=myTime)

We've set up our system, now we submit our request for data::

    >>> herring.get_data()
    <hydrofunctions.station.NWIS at 0x127506d6ac8>

Once you've requested your data, you don't need to request it again. Next,
we will create a Pandas dataframe using the `.df()` method, then we list the
first five items in our dataframe by dot chaining the `.head()` method::

    >>> herring.df().head()

--a table with our data appears--

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

Plot the data using Pandas and mathplotlib::

    >>> herring.df().plot()

.. image:: _static/HerringHydrograph.png
        :alt: a stream hydrograph for Herring Run

As long as you had `%matplotlib inline` enabled earlier, you will get a graph.

Example Notebooks
-----------------

- `Introduction to Hydrofunctions <https://github.com/mroberge/hydrofunctions/blob/master/Introduction%20to%20Hydrofunctions.ipynb>`_
- `Selecting Sites <https://github.com/mroberge/hydrofunctions/blob/master/Selecting_Sites.ipynb>`_
- `Writing Valid Requests for NWIS <https://github.com/mroberge/hydrofunctions/blob/master/Writing_Valid_Requests_for_NWIS.ipynb>`_
- `Draw Map Demo <https://github.com/mroberge/hydrofunctions/blob/master/Draw_Map_Demo.ipynb>`_
- `NWIS Trial Run <https://github.com/mroberge/hydrofunctions/blob/master/NWIS%20trial%20run.ipynb>`_
