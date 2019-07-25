==============
Selecting Data
==============

After you successfully request a dataset from the USGS, Hydrofunctions will
process the data into a huge table and then make it available to you in several
formats.

Use the following dataset for the examples below:

.. code-block:: ipython

    In  [1]: import hydrofunctions as hf
    In  [2]: data = hf.NWIS(['01589330', '01581830'], 'iv', start_date='2014-01-01', end_date='2015-01-01', file='example.parquet')


This dataset has the following properties:

.. code-block:: ipython

    In  [3]: data
    Out [3]:


It includes two sites, with three different types of data being collected at
one site, and two at the other.

View the Entire Table
=====================

Let's start by viewing all of the columns in the first five rows of our table.
To view all of our data as a dataframe, we use the .df() method of NWIS.
The .head() method limits our table to just the first five rows.

.. code-block:: ipython

    In  [3]: data.df().head()


This is equivalent to `data.df('all')`.

We can now see that we have five different columns containing data, and each
data column has a twin column that contains 'qualifiers'.

Selecting Only the Data Columns
===============================

Selecting Only the Data Columns for One Site
============================================

Selecting Only One Parameter
============================

Viewing and Interpreting the Qualifier Flags
============================================


