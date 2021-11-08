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

0.2.0 (2020-06-19 Juneteenth)
-----------------------------

* NWIS has a simpler interface and improved functionality:
    - No need to use .get_data(); data is fetched automatically.
    - NWIS.df() creates dataframes using only the parts you want
        - .df('discharge') returns a dataframe with only discharge data
        - .df('01585200') returns all of the data for just this site
        - .df('flags') returns a dataframe with the qualifier flags.
    - New and improved REPR: lists stations, parameters, and frequency for a dataset.
* Saving data to a file:
    - the 'file' parameter for NWIS allows you to save your data locally
    - If the file doesn't exist, NWIS requests the data and creates the file
    - Uses the parquet format for faster load times and smaller file sizes
* Improved parsing of data from NWIS:
    - missing observations are noted & can be replaced with interpolated values
    - duplicates found & removed
    - unsorted data found & cleaned.
    - different frequencies raise a warning when resampled
* parameterCd now accepts multiple parameters in request.
* If parameterCd is not specified, then all available parameters will be requested (default).
* hf.rating_curve(site) retrieves the current rating curve for a USGS site.
* hf.peaks(site) retrieves the annual peak discharges for a USGS site.
* hf.field_meas(site) retrieves the field data and notes used by the USGS to create a rating curve.
* hf.stats(site, statReportType) retrieves Annual, Monthly, or Daily reports from the USGS.
* hf.site_file(site) retrieves expanded site file.
* hf.data_catalog(site) retrieves history of data collected at site.
* Dropped Python 3.4 & 3.5 support, added 3.8.

0.2.1 (2021-05-28)
------------------

* Moved from TravisCI to Github Actions.
* Added Python 3.9 support.
* Created a verbose mode that is on by default.
* Added the flood stage service from the USGS waterwatch (iem)
* Save & read NWIS data in json.gzip files
* Added ability to read multiple instrument methods at the same time
* Bugfix: divide by zero error when you request data from many sites
* Bugfix: save_parquet

0.2.2 (2021-11-06)
------------------

* Added documentation for the `site_file` and `data_catalog` services
* Added "What is Hysteresis?" example to User's Guide
* Minor feature: URL message will print before & after requests are made
* Added verbose mode to USGS RDB functions
* Bugfix: `hf.df('q')` returned non-discharge data; fixed & added tests & fixture (dgk)
* Bugfix: renamed `typing.py` module to `validate.py` to prevent interference with typing
* Bugfix: HF will raise HydroNoDataError when non-200 response comes back from USGS
* Bugfix: logging off by default.
* Added hf._start_logging() to create a log & start logging.
* HydroExceptions will now create a log message when raised.
