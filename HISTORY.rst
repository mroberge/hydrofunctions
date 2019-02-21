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

0.1.5 (2018-02-22)
----------------------

* Updated to support Python 3.6
* Updated docs, added notebooks (mcr jdh)
* Added parameterCd to allow requests for different datasets (thanks @jdhughes-usgs!)
* Added ability to query sites by state or county (jdh)
* Added ability to request lists of sites or counties (jdh)
* Improved column names: now includes site id & variable description (for example, '07228000 - Mean Discharge, cubic feet per second')(jdh)
* Added descriptive warnings to explain why queries fail (mcr)


0.1.6 (2018-03-07)
----------------------

* Added draw_map function for help selecting sites (mcr)
* Added ability to query sites by a bounding box (jdh)
* Revised pandas dataframe column names to be the name composed of the provider, site id, parameter, and statistic (for example. USGS:01638500:00060:0001). (jdh)
* Added qualifiers for each station as a column in the dataframe. (jdh)
* Added ability extract NWIS property data from the response object (for example, siteName). (jdh)

0.1.7 (2018-11-11)
----------------------

* Added a flow duration chart (mcr)
* Added the cycleplot chart (mcr)
* Added code coverage (mcr)
* Improved the build scripts for TravisCI (mcr)
* Updated to support Python 3.7

0.1.8 (in development)
----------------------

* Dropped Python 3.4 support.
* parameterCd now accepts multiple parameters in request.