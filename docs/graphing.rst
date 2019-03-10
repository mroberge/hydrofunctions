========
Graphing
========


Hydrofunctions provides several ways to plot your data in a Jupyter notebook.
Many of these methods use the graphing methods built-in to the Pandas
dataframe. Some of these methods are specific to Hydrofunctions. All of these
techniques use `matplotlib`_ under the hood to create the charts, so
Hydrofunctions includes it during installation.

.. _matplotlib: https://matplotlib.org/

First Step: Automatic Display of Charts in Jupyter
--------------------------------------------------

The first step for creating a graph is to import Hydrofunctions, and then
provide Jupyter with a directive to automatically display all charts from
matplotlib::

    >>> import hydrofunctions as hf
    >>> `%matplotlib inline`

Second Step: Preparing our data for plotting
--------------------------------------------

The next step is to request some data from the NWIS for us to plot:

    >>> request = hf.NWIS('01585200', 'dv', period='P999D').get_data()

Next, we create a dataframe called 'data' from our request:

    >> data = request.df()

    The rest of the examples will assume that we have a dataframe called data.


Accessing plotting functions through Hydrofunctions
---------------------------------------------------

Hydrofunctions includes a Flow Duration Chart, which you access as a function::

    >>> hf.flow_duration(data)

Options include the ability to change the following:

* xscale: default is 'logit'; may also be 'linear'
* yscale: default is 'log'; may also be 'linear'
* ylabel: default is 'Discharge'; may be any string.
* symbol: default is '.' for small points. May also be:
    - pixel point: ','
    - up triangle: '^'
    - circle: 'o'
    - plus: '+'


Accessing plotting functions through the dataframe
--------------------------------------------------

The Pandas dataframe comes with several different graphing methods associated
with the dataframe. To access these methods, use dot notation.

Plotting a hydrograph::

    >>> data.plot()

Plotting a Histogram::

    >>> data.hist()
    >>> data.plot.hist()

Box Plot::

    >>> data.plot.box()

Kernel Density Plot::

    >>> data.plot.kde()



Example Notebooks
-----------------

- `Graphing <https://github.com/mroberge/hydrofunctions/blob/master/notebooks/Graphing.ipynb>`_
- `Comparing Urban and Rural Streams <https://github.com/mroberge/hydrofunctions/blob/master/notebooks/Comparing_Urban_and_Rural_Streams.ipynb>`_
