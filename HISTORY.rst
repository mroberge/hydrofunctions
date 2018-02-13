=======
History
=======

0.1.0 (2016-08-11)
------------------

* Project set up.

0.1.1 (2016-08-11)
------------------

* Customized project boilerplate.

0.1.2 (2016-08-26)
------------------

* Set up template for custom exceptions
* Added get_nwis function

0.1.3 (2016-09-09)
-----------------------

* Check user inputs & raise explanatory exceptions
* Extract data from response into a dataframe.
* Stations object for managing data.

0.1.4 (2016-09-18)
----------------------

* Added tests & documentation.

0.1.5 (2018-02-13)
----------------------

* Added a parameter (parameterCd) for requesting different parameters from NWIS (thanks @jdhughes-usgs!)
* Added functionality to pass a either a string for the site id or a list of sites ids
* Added functionality to query NWIS for all data for a specified parameterCD for a specified state
* Added functionality to query NWIS for all data for a specified parameterCD for a specified county (a list of county ids can be provided)
* Revised pandas dataframe column names to include the site id, NWIS parameterCd statistic, and the NWIS parameterCD variable description (for example, '07228000 - Mean Discharge, cubic feet per second')
