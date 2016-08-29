=====
Usage
=====

To use HydroFunctions in a project::

    >>> from hydrofunctions import hydrofunctions as hf
    >>> site = '01582500'
    >>> start = '2015-05-10'
    >>> end = '2015-05-15'
    >>> response = hf.get_nwis(site, 'dv', start, end)
    >>> response.ok
    True
    >>> response.status_code
    200
    >>> response.text

.. code-block:: json

'{"name":"ns1:timeSeriesResponseType","declaredType":"org.cuahsi.waterml.TimeSeriesResponseType","scope":"javax.xml.bind.JAXBElement$GlobalScope","value":{"queryInfo":{"queryURL":"http://waterservices.usgs.gov/nwis/dv/format=json%2C1.1&sites=01582500&endDT=2015-05-15&parameterCd=00060&startDT=2015-05-10","criteria":{"locationParam":"[ALL:01582500]","variableParam":"[00060]","timeParam":{"beginDateTime":"2015-05-10T00:00:00.000","endDateTime":"2015-05-15T00:00:00.000"},"parameter":[]},"note":[{"value":"[ALL:01582500]","title":"filter:sites"},{"value":"[mode=RANGE, modifiedSince=null] interval={INTERVAL[2015-05-10T00:00:00.000-04:00/2015-05-15T00:00:00.000-04:00]}","title":"filter:timeRange"},{"value":"methodIds=[ALL]","title":"filter:methodId"},{"value":"2016-08-26T15:47:39.245Z","title":"requestDT"},{"value":"6ad39ac0-6ba4-11e6-951b-6cae8b663fb6","title":"requestId"},{"value":"Provisional data are subject to revision. Go to http://waterdata.usgs.gov/nwis/help/?provisional for more information.","title":"disclaimer"},{"value":"vaas01","title":"server"}]},"timeSeries":[{"sourceInfo":{"siteName":"GUNPOWDER FALLS AT GLENCOE, MD","siteCode":[{"value":"01582500","network":"NWIS","agencyCode":"USGS"}],"timeZoneInfo":{"defaultTimeZone":{"zoneOffset":"-05:00","zoneAbbreviation":"EST"},"daylightSavingsTimeZone":{"zoneOffset":"-04:00","zoneAbbreviation":"EDT"},"siteUsesDaylightSavingsTime":false},"geoLocation":{"geogLocation":{"srs":"EPSG:4326","latitude":39.54969444,"longitude":-76.6361111},"localSiteXY":[]},"note":[],"siteType":[],"siteProperty":[{"value":"ST","name":"siteTypeCd"},{"value":"02060003","name":"hucCd"},{"value":"24","name":"stateCd"},{"value":"24005","name":"countyCd"}]},"variable":{"variableCode":[{"value":"00060","network":"NWIS","vocabulary":"NWIS:UnitValues","variableID":45807197,"default":true}],"variableName":"Streamflow, ft&#179;/s","variableDescription":"Discharge, cubic feet per second","valueType":"Derived Value","unit":{"unitCode":"ft3/s"},"options":{"option":[{"value":"Mean","name":"Statistic","optionCode":"00003"}]},"note":[],"noDataValue":-999999.0,"variableProperty":[],"oid":"45807197"},"values":[{"value":[{"value":"133","qualifiers":["A"],"dateTime":"2015-05-10T00:00:00.000"},{"value":"131","qualifiers":["A"],"dateTime":"2015-05-11T00:00:00.000"},{"value":"131","qualifiers":["A"],"dateTime":"2015-05-12T00:00:00.000"},{"value":"129","qualifiers":["A"],"dateTime":"2015-05-13T00:00:00.000"},{"value":"114","qualifiers":["A"],"dateTime":"2015-05-14T00:00:00.000"},{"value":"109","qualifiers":["A"],"dateTime":"2015-05-15T00:00:00.000"}],"qualifier":[{"qualifierCode":"A","qualifierDescription":"Approved for publication -- Processing and review completed.","qualifierID":0,"network":"NWIS","vocabulary":"uv_rmk_cd"}],"qualityControlLevel":[],"method":[{"methodDescription":"","methodID":68173}],"source":[],"offset":[],"sample":[],"censorCode":[]}],"name":"USGS:01582500:00060:00003"}]},"nil":false,"globalScope":true,"typeSubstituted":false}'

.. code-block:: python
    >>> dir(response)
will list the different attributes and methods.

future versions will translate text into a dataframe.