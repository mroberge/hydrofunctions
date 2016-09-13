=====
Usage
=====

To use HydroFunctions in a project::

    >>> from hydrofunctions import hydrofunctions as hf

    >>> site = '01582500'
    >>> start = '2015-05-10'
    >>> end = '2015-05-15'
    >>> response = hf.get_nwis(site, 'dv', start, end)

Use the response object::

    >>> response.ok
    True
    >>> response.status_code
    200
    >>> response.text
    '{"name":"ns1:timeSeriesResponseType","declaredType":"org.cuahsi.waterml.TimeSeriesResponseType" .... }

.. code-block:: python
    >>> dir(response)
will list the different attributes and methods.

Functions that use the response object

Extract a dict from the response::

    >>>my_dict = hf.extract_nwis_dict(response)
    >>>my_dict
    {'declaredType': 'org.cuahsi.waterml.TimeSeriesResponseType',
     'globalScope': True,
     ...
    }

Extract a Pandas dataframe from the response::

    >>>my_data_frame = hf.extract_nwis_df(response)
    >>>my_data_frame
                value
    datetime
    2015-05-10  133.0
    2015-05-11  131.0
    2015-05-12  131.0
    2015-05-13  129.0
    2015-05-14  114.0
    2015-05-15  109.0
