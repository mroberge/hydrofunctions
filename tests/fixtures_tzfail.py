"""
fixtures_tzfail.py

This file contains JSON from the NWIS.

Daylight Savings Time started on 2019-03-10...
"""

tzfail = {
    "name": "ns1:timeSeriesResponseType",
    "declaredType": "org.cuahsi.waterml.TimeSeriesResponseType",
    "scope": "javax.xml.bind.JAXBElement$GlobalScope",
    "value": {
        "queryInfo": {
            "queryURL": "http://waterservices.usgs.gov/nwis/iv/format=json%2C1.1&sites=02489500%2C02492000&startDT=2019-02-25&endDT=2019-03-01",
            "criteria": {
                "locationParam": "[ALL:02489500, ALL:02492000]",
                "variableParam": "ALL",
                "timeParam": {
                    "beginDateTime": "2019-02-25T00:00:00.000",
                    "endDateTime": "2019-03-01T23:59:59.000",
                },
                "parameter": [],
            },
            "note": [
                {"value": "[ALL:02489500, ALL:02492000]", "title": "filter:sites"},
                {
                    "value": "[mode=RANGE, modifiedSince=null] interval={INTERVAL[2019-02-25T00:00:00.000-05:00/2019-03-01T23:59:59.000Z]}",
                    "title": "filter:timeRange",
                },
                {"value": "methodIds=[ALL]", "title": "filter:methodId"},
                {"value": "2019-03-10T19:37:18.864Z", "title": "requestDT"},
                {"value": "eaa319f0-436b-11e9-84d1-6cae8b6642ea", "title": "requestId"},
                {
                    "value": "Provisional data are subject to revision. Go to http://waterdata.usgs.gov/nwis/help/?provisional for more information.",
                    "title": "disclaimer",
                },
                {"value": "sdas01", "title": "server"},
            ],
        },
        "timeSeries": [
            {
                "sourceInfo": {
                    "siteName": "Pearl River near Bogalusa, LA",
                    "siteCode": [
                        {"value": "02489500", "network": "NWIS", "agencyCode": "USGS"}
                    ],
                    "timeZoneInfo": {
                        "defaultTimeZone": {
                            "zoneOffset": "-06:00",
                            "zoneAbbreviation": "CST",
                        },
                        "daylightSavingsTimeZone": {
                            "zoneOffset": "-05:00",
                            "zoneAbbreviation": "CDT",
                        },
                        "siteUsesDaylightSavingsTime": True,
                    },
                    "geoLocation": {
                        "geogLocation": {
                            "srs": "EPSG:4326",
                            "latitude": 30.79324276,
                            "longitude": -89.8209072,
                        },
                        "localSiteXY": [],
                    },
                    "note": [],
                    "siteType": [],
                    "siteProperty": [
                        {"value": "ST", "name": "siteTypeCd"},
                        {"value": "03180004", "name": "hucCd"},
                        {"value": "22", "name": "stateCd"},
                        {"value": "22117", "name": "countyCd"},
                    ],
                },
                "variable": {
                    "variableCode": [
                        {
                            "value": "00045",
                            "network": "NWIS",
                            "vocabulary": "NWIS:UnitValues",
                            "variableID": 45807140,
                            "default": True,
                        }
                    ],
                    "variableName": "Precipitation, total, in",
                    "variableDescription": "Precipitation, total, inches",
                    "valueType": "Derived Value",
                    "unit": {"unitCode": "in"},
                    "options": {
                        "option": [{"name": "Statistic", "optionCode": "00000"}]
                    },
                    "note": [],
                    "noDataValue": -999999.0,
                    "variableProperty": [],
                    "oid": "45807140",
                },
                "values": [
                    {
                        "value": [
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T00:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T00:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T01:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T01:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T02:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T02:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T03:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T03:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T04:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T04:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T05:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T05:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T06:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T06:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T07:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T07:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T08:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T08:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T09:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T09:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T10:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T10:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T11:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T11:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T12:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T12:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T13:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T13:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T14:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T14:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T15:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T15:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T16:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T16:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T17:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T17:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T18:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T18:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T19:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T19:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T20:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T20:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T21:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T21:30:00.000-06:00",
                            },
                            {
                                "value": "0.01",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T22:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T22:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T23:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T23:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T00:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T00:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T01:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T01:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T02:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T02:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T03:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T03:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T04:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T04:30:00.000-06:00",
                            },
                            {
                                "value": "0.01",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T05:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T05:30:00.000-06:00",
                            },
                            {
                                "value": "0.01",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T06:00:00.000-06:00",
                            },
                            {
                                "value": "0.01",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T06:30:00.000-06:00",
                            },
                            {
                                "value": "0.01",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T07:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T07:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T08:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T08:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T09:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T09:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T10:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T10:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T11:00:00.000-06:00",
                            },
                            {
                                "value": "0.02",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T11:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T12:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T12:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T13:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T13:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T14:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T14:30:00.000-06:00",
                            },
                            {
                                "value": "0.01",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T15:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T15:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T16:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T16:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T17:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T17:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T18:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T18:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T19:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T19:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T20:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T20:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T21:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T21:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T22:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T22:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T23:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T23:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T00:00:00.000-06:00",
                            },
                            {
                                "value": "0.20",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T00:30:00.000-06:00",
                            },
                            {
                                "value": "0.15",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T01:00:00.000-06:00",
                            },
                            {
                                "value": "0.14",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T01:30:00.000-06:00",
                            },
                            {
                                "value": "0.11",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T02:00:00.000-06:00",
                            },
                            {
                                "value": "0.06",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T02:30:00.000-06:00",
                            },
                            {
                                "value": "0.04",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T03:00:00.000-06:00",
                            },
                            {
                                "value": "0.04",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T03:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T04:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T04:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T05:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T05:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T06:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T06:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T07:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T07:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T08:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T08:30:00.000-06:00",
                            },
                            {
                                "value": "0.01",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T09:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T09:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T10:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T10:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T11:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T11:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T12:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T12:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T13:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T13:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T14:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T14:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T15:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T15:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T16:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T16:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T17:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T17:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T18:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T18:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T19:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T19:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T20:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T20:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T21:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T21:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T22:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T22:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T23:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T23:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T00:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T00:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T01:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T01:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T02:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T02:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T03:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T03:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T04:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T04:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T05:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T05:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T06:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T06:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T07:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T07:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T08:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T08:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T09:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T09:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T10:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T10:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T11:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T11:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T12:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T12:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T13:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T13:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T14:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T14:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T15:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T15:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T16:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T16:30:00.000-06:00",
                            },
                            {
                                "value": "0.21",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T17:00:00.000-06:00",
                            },
                            {
                                "value": "0.02",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T17:30:00.000-06:00",
                            },
                            {
                                "value": "0.15",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T18:00:00.000-06:00",
                            },
                            {
                                "value": "0.02",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T18:30:00.000-06:00",
                            },
                            {
                                "value": "0.01",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T19:00:00.000-06:00",
                            },
                            {
                                "value": "0.01",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T19:30:00.000-06:00",
                            },
                            {
                                "value": "0.01",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T20:00:00.000-06:00",
                            },
                            {
                                "value": "0.01",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T20:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T21:00:00.000-06:00",
                            },
                            {
                                "value": "0.01",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T21:30:00.000-06:00",
                            },
                            {
                                "value": "0.01",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T22:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T22:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T23:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T23:30:00.000-06:00",
                            },
                            {
                                "value": "0.03",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T00:00:00.000-06:00",
                            },
                            {
                                "value": "0.05",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T00:30:00.000-06:00",
                            },
                            {
                                "value": "0.03",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T01:00:00.000-06:00",
                            },
                            {
                                "value": "0.03",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T01:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T02:00:00.000-06:00",
                            },
                            {
                                "value": "0.01",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T02:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T03:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T03:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T04:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T04:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T05:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T05:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T06:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T06:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T07:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T07:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T08:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T08:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T09:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T09:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T10:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T10:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T11:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T11:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T12:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T12:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T13:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T13:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T14:00:00.000-06:00",
                            },
                            {
                                "value": "0.03",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T14:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T15:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T15:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T16:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T16:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T17:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T17:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T18:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T18:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T19:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T19:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T20:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T20:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T21:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T21:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T22:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T22:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T23:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T23:30:00.000-06:00",
                            },
                        ],
                        "qualifier": [
                            {
                                "qualifierCode": "P",
                                "qualifierDescription": "Provisional data subject to revision.",
                                "qualifierID": 0,
                                "network": "NWIS",
                                "vocabulary": "uv_rmk_cd",
                            }
                        ],
                        "qualityControlLevel": [],
                        "method": [{"methodDescription": "", "methodID": 62161}],
                        "source": [],
                        "offset": [],
                        "sample": [],
                        "censorCode": [],
                    }
                ],
                "name": "USGS:02489500:00045:00000",
            },
            {
                "sourceInfo": {
                    "siteName": "Pearl River near Bogalusa, LA",
                    "siteCode": [
                        {"value": "02489500", "network": "NWIS", "agencyCode": "USGS"}
                    ],
                    "timeZoneInfo": {
                        "defaultTimeZone": {
                            "zoneOffset": "-06:00",
                            "zoneAbbreviation": "CST",
                        },
                        "daylightSavingsTimeZone": {
                            "zoneOffset": "-05:00",
                            "zoneAbbreviation": "CDT",
                        },
                        "siteUsesDaylightSavingsTime": True,
                    },
                    "geoLocation": {
                        "geogLocation": {
                            "srs": "EPSG:4326",
                            "latitude": 30.79324276,
                            "longitude": -89.8209072,
                        },
                        "localSiteXY": [],
                    },
                    "note": [],
                    "siteType": [],
                    "siteProperty": [
                        {"value": "ST", "name": "siteTypeCd"},
                        {"value": "03180004", "name": "hucCd"},
                        {"value": "22", "name": "stateCd"},
                        {"value": "22117", "name": "countyCd"},
                    ],
                },
                "variable": {
                    "variableCode": [
                        {
                            "value": "00060",
                            "network": "NWIS",
                            "vocabulary": "NWIS:UnitValues",
                            "variableID": 45807197,
                            "default": True,
                        }
                    ],
                    "variableName": "Streamflow, ft&#179;/s",
                    "variableDescription": "Discharge, cubic feet per second",
                    "valueType": "Derived Value",
                    "unit": {"unitCode": "ft3/s"},
                    "options": {
                        "option": [{"name": "Statistic", "optionCode": "00000"}]
                    },
                    "note": [],
                    "noDataValue": -999999.0,
                    "variableProperty": [],
                    "oid": "45807197",
                },
                "values": [
                    {
                        "value": [
                            {
                                "value": "24400",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T00:00:00.000-06:00",
                            },
                            {
                                "value": "24400",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T00:30:00.000-06:00",
                            },
                            {
                                "value": "24500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T01:00:00.000-06:00",
                            },
                            {
                                "value": "24600",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T01:30:00.000-06:00",
                            },
                            {
                                "value": "24700",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T02:00:00.000-06:00",
                            },
                            {
                                "value": "24800",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T02:30:00.000-06:00",
                            },
                            {
                                "value": "24900",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T03:00:00.000-06:00",
                            },
                            {
                                "value": "24900",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T03:30:00.000-06:00",
                            },
                            {
                                "value": "25100",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T04:00:00.000-06:00",
                            },
                            {
                                "value": "24900",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T04:30:00.000-06:00",
                            },
                            {
                                "value": "25100",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T05:00:00.000-06:00",
                            },
                            {
                                "value": "25200",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T05:30:00.000-06:00",
                            },
                            {
                                "value": "25300",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T06:00:00.000-06:00",
                            },
                            {
                                "value": "25400",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T06:30:00.000-06:00",
                            },
                            {
                                "value": "25600",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T07:00:00.000-06:00",
                            },
                            {
                                "value": "25600",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T07:30:00.000-06:00",
                            },
                            {
                                "value": "25600",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T08:00:00.000-06:00",
                            },
                            {
                                "value": "25500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T08:30:00.000-06:00",
                            },
                            {
                                "value": "25700",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T09:00:00.000-06:00",
                            },
                            {
                                "value": "25700",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T09:30:00.000-06:00",
                            },
                            {
                                "value": "25700",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T10:00:00.000-06:00",
                            },
                            {
                                "value": "25800",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T10:30:00.000-06:00",
                            },
                            {
                                "value": "25800",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T11:00:00.000-06:00",
                            },
                            {
                                "value": "25800",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T11:30:00.000-06:00",
                            },
                            {
                                "value": "25900",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T12:00:00.000-06:00",
                            },
                            {
                                "value": "26000",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T12:30:00.000-06:00",
                            },
                            {
                                "value": "26000",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T13:00:00.000-06:00",
                            },
                            {
                                "value": "26000",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T13:30:00.000-06:00",
                            },
                            {
                                "value": "26000",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T14:00:00.000-06:00",
                            },
                            {
                                "value": "26200",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T14:30:00.000-06:00",
                            },
                            {
                                "value": "26200",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T15:00:00.000-06:00",
                            },
                            {
                                "value": "26200",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T15:30:00.000-06:00",
                            },
                            {
                                "value": "26300",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T16:00:00.000-06:00",
                            },
                            {
                                "value": "26300",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T16:30:00.000-06:00",
                            },
                            {
                                "value": "26300",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T17:00:00.000-06:00",
                            },
                            {
                                "value": "26400",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T17:30:00.000-06:00",
                            },
                            {
                                "value": "26500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T18:00:00.000-06:00",
                            },
                            {
                                "value": "26600",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T18:30:00.000-06:00",
                            },
                            {
                                "value": "26600",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T19:00:00.000-06:00",
                            },
                            {
                                "value": "26500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T19:30:00.000-06:00",
                            },
                            {
                                "value": "26700",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T20:00:00.000-06:00",
                            },
                            {
                                "value": "26700",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T20:30:00.000-06:00",
                            },
                            {
                                "value": "26700",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T21:00:00.000-06:00",
                            },
                            {
                                "value": "26700",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T21:30:00.000-06:00",
                            },
                            {
                                "value": "26900",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T22:00:00.000-06:00",
                            },
                            {
                                "value": "26800",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T22:30:00.000-06:00",
                            },
                            {
                                "value": "27000",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T23:00:00.000-06:00",
                            },
                            {
                                "value": "27000",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T23:30:00.000-06:00",
                            },
                            {
                                "value": "27000",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T00:00:00.000-06:00",
                            },
                            {
                                "value": "27300",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T00:30:00.000-06:00",
                            },
                            {
                                "value": "27300",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T01:00:00.000-06:00",
                            },
                            {
                                "value": "27300",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T01:30:00.000-06:00",
                            },
                            {
                                "value": "27400",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T02:00:00.000-06:00",
                            },
                            {
                                "value": "27500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T02:30:00.000-06:00",
                            },
                            {
                                "value": "27700",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T03:00:00.000-06:00",
                            },
                            {
                                "value": "27400",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T03:30:00.000-06:00",
                            },
                            {
                                "value": "27500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T04:00:00.000-06:00",
                            },
                            {
                                "value": "27500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T04:30:00.000-06:00",
                            },
                            {
                                "value": "27800",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T05:00:00.000-06:00",
                            },
                            {
                                "value": "27500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T05:30:00.000-06:00",
                            },
                            {
                                "value": "27800",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T06:00:00.000-06:00",
                            },
                            {
                                "value": "27800",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T06:30:00.000-06:00",
                            },
                            {
                                "value": "27700",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T07:00:00.000-06:00",
                            },
                            {
                                "value": "27800",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T07:30:00.000-06:00",
                            },
                            {
                                "value": "27800",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T08:00:00.000-06:00",
                            },
                            {
                                "value": "27900",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T08:30:00.000-06:00",
                            },
                            {
                                "value": "27900",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T09:00:00.000-06:00",
                            },
                            {
                                "value": "27800",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T09:30:00.000-06:00",
                            },
                            {
                                "value": "28000",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T10:00:00.000-06:00",
                            },
                            {
                                "value": "27900",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T10:30:00.000-06:00",
                            },
                            {
                                "value": "27900",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T11:00:00.000-06:00",
                            },
                            {
                                "value": "28000",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T11:30:00.000-06:00",
                            },
                            {
                                "value": "28000",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T12:00:00.000-06:00",
                            },
                            {
                                "value": "28000",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T12:30:00.000-06:00",
                            },
                            {
                                "value": "28000",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T13:00:00.000-06:00",
                            },
                            {
                                "value": "28000",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T13:30:00.000-06:00",
                            },
                            {
                                "value": "28200",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T14:00:00.000-06:00",
                            },
                            {
                                "value": "28000",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T14:30:00.000-06:00",
                            },
                            {
                                "value": "28300",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T15:00:00.000-06:00",
                            },
                            {
                                "value": "28300",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T15:30:00.000-06:00",
                            },
                            {
                                "value": "28300",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T16:00:00.000-06:00",
                            },
                            {
                                "value": "28300",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T16:30:00.000-06:00",
                            },
                            {
                                "value": "28200",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T17:00:00.000-06:00",
                            },
                            {
                                "value": "28300",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T17:30:00.000-06:00",
                            },
                            {
                                "value": "28300",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T18:00:00.000-06:00",
                            },
                            {
                                "value": "28600",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T18:30:00.000-06:00",
                            },
                            {
                                "value": "28300",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T19:00:00.000-06:00",
                            },
                            {
                                "value": "28400",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T19:30:00.000-06:00",
                            },
                            {
                                "value": "28300",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T20:00:00.000-06:00",
                            },
                            {
                                "value": "28300",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T20:30:00.000-06:00",
                            },
                            {
                                "value": "28400",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T21:00:00.000-06:00",
                            },
                            {
                                "value": "28600",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T21:30:00.000-06:00",
                            },
                            {
                                "value": "28600",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T22:00:00.000-06:00",
                            },
                            {
                                "value": "28700",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T22:30:00.000-06:00",
                            },
                            {
                                "value": "28700",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T23:00:00.000-06:00",
                            },
                            {
                                "value": "28600",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T23:30:00.000-06:00",
                            },
                            {
                                "value": "28700",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T00:00:00.000-06:00",
                            },
                            {
                                "value": "28700",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T00:30:00.000-06:00",
                            },
                            {
                                "value": "28700",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T01:00:00.000-06:00",
                            },
                            {
                                "value": "29000",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T01:30:00.000-06:00",
                            },
                            {
                                "value": "29000",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T02:00:00.000-06:00",
                            },
                            {
                                "value": "29100",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T02:30:00.000-06:00",
                            },
                            {
                                "value": "29000",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T03:00:00.000-06:00",
                            },
                            {
                                "value": "29000",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T03:30:00.000-06:00",
                            },
                            {
                                "value": "29400",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T04:00:00.000-06:00",
                            },
                            {
                                "value": "29200",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T04:30:00.000-06:00",
                            },
                            {
                                "value": "29400",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T05:00:00.000-06:00",
                            },
                            {
                                "value": "29200",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T05:30:00.000-06:00",
                            },
                            {
                                "value": "29400",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T06:00:00.000-06:00",
                            },
                            {
                                "value": "29400",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T06:30:00.000-06:00",
                            },
                            {
                                "value": "29200",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T07:00:00.000-06:00",
                            },
                            {
                                "value": "29200",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T07:30:00.000-06:00",
                            },
                            {
                                "value": "29200",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T08:00:00.000-06:00",
                            },
                            {
                                "value": "29200",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T08:30:00.000-06:00",
                            },
                            {
                                "value": "29400",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T09:00:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T09:30:00.000-06:00",
                            },
                            {
                                "value": "29100",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T10:00:00.000-06:00",
                            },
                            {
                                "value": "29200",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T10:30:00.000-06:00",
                            },
                            {
                                "value": "29400",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T11:00:00.000-06:00",
                            },
                            {
                                "value": "29200",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T11:30:00.000-06:00",
                            },
                            {
                                "value": "29100",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T12:00:00.000-06:00",
                            },
                            {
                                "value": "29200",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T12:30:00.000-06:00",
                            },
                            {
                                "value": "29000",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T13:00:00.000-06:00",
                            },
                            {
                                "value": "29200",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T13:30:00.000-06:00",
                            },
                            {
                                "value": "29200",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T14:00:00.000-06:00",
                            },
                            {
                                "value": "29100",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T14:30:00.000-06:00",
                            },
                            {
                                "value": "29200",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T15:00:00.000-06:00",
                            },
                            {
                                "value": "29200",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T15:30:00.000-06:00",
                            },
                            {
                                "value": "29200",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T16:00:00.000-06:00",
                            },
                            {
                                "value": "29100",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T16:30:00.000-06:00",
                            },
                            {
                                "value": "29200",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T17:00:00.000-06:00",
                            },
                            {
                                "value": "29200",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T17:30:00.000-06:00",
                            },
                            {
                                "value": "29200",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T18:00:00.000-06:00",
                            },
                            {
                                "value": "29200",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T18:30:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T19:00:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T19:30:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T20:00:00.000-06:00",
                            },
                            {
                                "value": "29400",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T20:30:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T21:00:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T21:30:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T22:00:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T22:30:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T23:00:00.000-06:00",
                            },
                            {
                                "value": "29600",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T23:30:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T00:00:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T00:30:00.000-06:00",
                            },
                            {
                                "value": "29400",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T01:00:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T01:30:00.000-06:00",
                            },
                            {
                                "value": "29600",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T02:00:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T02:30:00.000-06:00",
                            },
                            {
                                "value": "29600",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T03:00:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T03:30:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T04:00:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T04:30:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T05:00:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T05:30:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T06:00:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T06:30:00.000-06:00",
                            },
                            {
                                "value": "29600",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T07:00:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T07:30:00.000-06:00",
                            },
                            {
                                "value": "29400",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T08:00:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T08:30:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T09:00:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T09:30:00.000-06:00",
                            },
                            {
                                "value": "29400",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T10:00:00.000-06:00",
                            },
                            {
                                "value": "29400",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T10:30:00.000-06:00",
                            },
                            {
                                "value": "29200",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T11:00:00.000-06:00",
                            },
                            {
                                "value": "29400",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T11:30:00.000-06:00",
                            },
                            {
                                "value": "29400",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T12:00:00.000-06:00",
                            },
                            {
                                "value": "29200",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T12:30:00.000-06:00",
                            },
                            {
                                "value": "29200",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T13:00:00.000-06:00",
                            },
                            {
                                "value": "29100",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T13:30:00.000-06:00",
                            },
                            {
                                "value": "29200",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T14:00:00.000-06:00",
                            },
                            {
                                "value": "29200",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T14:30:00.000-06:00",
                            },
                            {
                                "value": "29200",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T15:00:00.000-06:00",
                            },
                            {
                                "value": "29200",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T15:30:00.000-06:00",
                            },
                            {
                                "value": "29200",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T16:00:00.000-06:00",
                            },
                            {
                                "value": "29400",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T16:30:00.000-06:00",
                            },
                            {
                                "value": "29800",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T17:00:00.000-06:00",
                            },
                            {
                                "value": "29600",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T17:30:00.000-06:00",
                            },
                            {
                                "value": "29600",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T18:00:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T18:30:00.000-06:00",
                            },
                            {
                                "value": "29800",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T19:00:00.000-06:00",
                            },
                            {
                                "value": "29800",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T19:30:00.000-06:00",
                            },
                            {
                                "value": "29600",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T20:00:00.000-06:00",
                            },
                            {
                                "value": "29600",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T20:30:00.000-06:00",
                            },
                            {
                                "value": "29600",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T21:00:00.000-06:00",
                            },
                            {
                                "value": "29600",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T21:30:00.000-06:00",
                            },
                            {
                                "value": "29800",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T22:00:00.000-06:00",
                            },
                            {
                                "value": "29800",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T22:30:00.000-06:00",
                            },
                            {
                                "value": "29600",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T23:00:00.000-06:00",
                            },
                            {
                                "value": "29600",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T23:30:00.000-06:00",
                            },
                            {
                                "value": "29600",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T00:00:00.000-06:00",
                            },
                            {
                                "value": "29800",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T00:30:00.000-06:00",
                            },
                            {
                                "value": "29800",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T01:00:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T01:30:00.000-06:00",
                            },
                            {
                                "value": "29600",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T02:00:00.000-06:00",
                            },
                            {
                                "value": "29600",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T02:30:00.000-06:00",
                            },
                            {
                                "value": "29600",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T03:00:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T03:30:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T04:00:00.000-06:00",
                            },
                            {
                                "value": "29600",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T04:30:00.000-06:00",
                            },
                            {
                                "value": "29900",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T05:00:00.000-06:00",
                            },
                            {
                                "value": "29600",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T05:30:00.000-06:00",
                            },
                            {
                                "value": "29600",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T06:00:00.000-06:00",
                            },
                            {
                                "value": "29900",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T06:30:00.000-06:00",
                            },
                            {
                                "value": "29800",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T07:00:00.000-06:00",
                            },
                            {
                                "value": "29800",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T07:30:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T08:00:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T08:30:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T09:00:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T09:30:00.000-06:00",
                            },
                            {
                                "value": "29400",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T10:00:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T10:30:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T11:00:00.000-06:00",
                            },
                            {
                                "value": "29400",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T11:30:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T12:00:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T12:30:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T13:00:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T13:30:00.000-06:00",
                            },
                            {
                                "value": "29400",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T14:00:00.000-06:00",
                            },
                            {
                                "value": "29400",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T14:30:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T15:00:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T15:30:00.000-06:00",
                            },
                            {
                                "value": "29600",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T16:00:00.000-06:00",
                            },
                            {
                                "value": "29400",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T16:30:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T17:00:00.000-06:00",
                            },
                            {
                                "value": "29400",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T17:30:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T18:00:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T18:30:00.000-06:00",
                            },
                            {
                                "value": "29600",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T19:00:00.000-06:00",
                            },
                            {
                                "value": "29800",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T19:30:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T20:00:00.000-06:00",
                            },
                            {
                                "value": "29600",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T20:30:00.000-06:00",
                            },
                            {
                                "value": "29800",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T21:00:00.000-06:00",
                            },
                            {
                                "value": "29600",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T21:30:00.000-06:00",
                            },
                            {
                                "value": "29500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T22:00:00.000-06:00",
                            },
                            {
                                "value": "29600",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T22:30:00.000-06:00",
                            },
                            {
                                "value": "29600",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T23:00:00.000-06:00",
                            },
                            {
                                "value": "29600",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T23:30:00.000-06:00",
                            },
                        ],
                        "qualifier": [
                            {
                                "qualifierCode": "P",
                                "qualifierDescription": "Provisional data subject to revision.",
                                "qualifierID": 0,
                                "network": "NWIS",
                                "vocabulary": "uv_rmk_cd",
                            }
                        ],
                        "qualityControlLevel": [],
                        "method": [{"methodDescription": "", "methodID": 62159}],
                        "source": [],
                        "offset": [],
                        "sample": [],
                        "censorCode": [],
                    }
                ],
                "name": "USGS:02489500:00060:00000",
            },
            {
                "sourceInfo": {
                    "siteName": "Pearl River near Bogalusa, LA",
                    "siteCode": [
                        {"value": "02489500", "network": "NWIS", "agencyCode": "USGS"}
                    ],
                    "timeZoneInfo": {
                        "defaultTimeZone": {
                            "zoneOffset": "-06:00",
                            "zoneAbbreviation": "CST",
                        },
                        "daylightSavingsTimeZone": {
                            "zoneOffset": "-05:00",
                            "zoneAbbreviation": "CDT",
                        },
                        "siteUsesDaylightSavingsTime": True,
                    },
                    "geoLocation": {
                        "geogLocation": {
                            "srs": "EPSG:4326",
                            "latitude": 30.79324276,
                            "longitude": -89.8209072,
                        },
                        "localSiteXY": [],
                    },
                    "note": [],
                    "siteType": [],
                    "siteProperty": [
                        {"value": "ST", "name": "siteTypeCd"},
                        {"value": "03180004", "name": "hucCd"},
                        {"value": "22", "name": "stateCd"},
                        {"value": "22117", "name": "countyCd"},
                    ],
                },
                "variable": {
                    "variableCode": [
                        {
                            "value": "00065",
                            "network": "NWIS",
                            "vocabulary": "NWIS:UnitValues",
                            "variableID": 45807202,
                            "default": True,
                        }
                    ],
                    "variableName": "Gage height, ft",
                    "variableDescription": "Gage height, feet",
                    "valueType": "Derived Value",
                    "unit": {"unitCode": "ft"},
                    "options": {
                        "option": [{"name": "Statistic", "optionCode": "00000"}]
                    },
                    "note": [],
                    "noDataValue": -999999.0,
                    "variableProperty": [],
                    "oid": "45807202",
                },
                "values": [
                    {
                        "value": [
                            {
                                "value": "19.86",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T00:00:00.000-06:00",
                            },
                            {
                                "value": "19.86",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T00:30:00.000-06:00",
                            },
                            {
                                "value": "19.88",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T01:00:00.000-06:00",
                            },
                            {
                                "value": "19.89",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T01:30:00.000-06:00",
                            },
                            {
                                "value": "19.90",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T02:00:00.000-06:00",
                            },
                            {
                                "value": "19.91",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T02:30:00.000-06:00",
                            },
                            {
                                "value": "19.92",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T03:00:00.000-06:00",
                            },
                            {
                                "value": "19.93",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T03:30:00.000-06:00",
                            },
                            {
                                "value": "19.95",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T04:00:00.000-06:00",
                            },
                            {
                                "value": "19.93",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T04:30:00.000-06:00",
                            },
                            {
                                "value": "19.95",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T05:00:00.000-06:00",
                            },
                            {
                                "value": "19.96",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T05:30:00.000-06:00",
                            },
                            {
                                "value": "19.97",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T06:00:00.000-06:00",
                            },
                            {
                                "value": "19.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T06:30:00.000-06:00",
                            },
                            {
                                "value": "20.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T07:00:00.000-06:00",
                            },
                            {
                                "value": "20.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T07:30:00.000-06:00",
                            },
                            {
                                "value": "20.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T08:00:00.000-06:00",
                            },
                            {
                                "value": "19.99",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T08:30:00.000-06:00",
                            },
                            {
                                "value": "20.01",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T09:00:00.000-06:00",
                            },
                            {
                                "value": "20.01",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T09:30:00.000-06:00",
                            },
                            {
                                "value": "20.01",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T10:00:00.000-06:00",
                            },
                            {
                                "value": "20.03",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T10:30:00.000-06:00",
                            },
                            {
                                "value": "20.03",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T11:00:00.000-06:00",
                            },
                            {
                                "value": "20.03",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T11:30:00.000-06:00",
                            },
                            {
                                "value": "20.04",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T12:00:00.000-06:00",
                            },
                            {
                                "value": "20.05",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T12:30:00.000-06:00",
                            },
                            {
                                "value": "20.05",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T13:00:00.000-06:00",
                            },
                            {
                                "value": "20.05",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T13:30:00.000-06:00",
                            },
                            {
                                "value": "20.05",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T14:00:00.000-06:00",
                            },
                            {
                                "value": "20.07",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T14:30:00.000-06:00",
                            },
                            {
                                "value": "20.07",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T15:00:00.000-06:00",
                            },
                            {
                                "value": "20.07",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T15:30:00.000-06:00",
                            },
                            {
                                "value": "20.08",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T16:00:00.000-06:00",
                            },
                            {
                                "value": "20.08",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T16:30:00.000-06:00",
                            },
                            {
                                "value": "20.08",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T17:00:00.000-06:00",
                            },
                            {
                                "value": "20.09",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T17:30:00.000-06:00",
                            },
                            {
                                "value": "20.10",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T18:00:00.000-06:00",
                            },
                            {
                                "value": "20.11",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T18:30:00.000-06:00",
                            },
                            {
                                "value": "20.11",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T19:00:00.000-06:00",
                            },
                            {
                                "value": "20.10",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T19:30:00.000-06:00",
                            },
                            {
                                "value": "20.12",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T20:00:00.000-06:00",
                            },
                            {
                                "value": "20.12",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T20:30:00.000-06:00",
                            },
                            {
                                "value": "20.12",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T21:00:00.000-06:00",
                            },
                            {
                                "value": "20.12",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T21:30:00.000-06:00",
                            },
                            {
                                "value": "20.14",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T22:00:00.000-06:00",
                            },
                            {
                                "value": "20.13",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T22:30:00.000-06:00",
                            },
                            {
                                "value": "20.15",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T23:00:00.000-06:00",
                            },
                            {
                                "value": "20.15",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T23:30:00.000-06:00",
                            },
                            {
                                "value": "20.15",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T00:00:00.000-06:00",
                            },
                            {
                                "value": "20.17",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T00:30:00.000-06:00",
                            },
                            {
                                "value": "20.17",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T01:00:00.000-06:00",
                            },
                            {
                                "value": "20.17",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T01:30:00.000-06:00",
                            },
                            {
                                "value": "20.18",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T02:00:00.000-06:00",
                            },
                            {
                                "value": "20.19",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T02:30:00.000-06:00",
                            },
                            {
                                "value": "20.20",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T03:00:00.000-06:00",
                            },
                            {
                                "value": "20.18",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T03:30:00.000-06:00",
                            },
                            {
                                "value": "20.19",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T04:00:00.000-06:00",
                            },
                            {
                                "value": "20.19",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T04:30:00.000-06:00",
                            },
                            {
                                "value": "20.21",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T05:00:00.000-06:00",
                            },
                            {
                                "value": "20.19",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T05:30:00.000-06:00",
                            },
                            {
                                "value": "20.21",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T06:00:00.000-06:00",
                            },
                            {
                                "value": "20.21",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T06:30:00.000-06:00",
                            },
                            {
                                "value": "20.20",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T07:00:00.000-06:00",
                            },
                            {
                                "value": "20.21",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T07:30:00.000-06:00",
                            },
                            {
                                "value": "20.21",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T08:00:00.000-06:00",
                            },
                            {
                                "value": "20.22",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T08:30:00.000-06:00",
                            },
                            {
                                "value": "20.22",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T09:00:00.000-06:00",
                            },
                            {
                                "value": "20.21",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T09:30:00.000-06:00",
                            },
                            {
                                "value": "20.23",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T10:00:00.000-06:00",
                            },
                            {
                                "value": "20.22",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T10:30:00.000-06:00",
                            },
                            {
                                "value": "20.22",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T11:00:00.000-06:00",
                            },
                            {
                                "value": "20.23",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T11:30:00.000-06:00",
                            },
                            {
                                "value": "20.23",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T12:00:00.000-06:00",
                            },
                            {
                                "value": "20.23",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T12:30:00.000-06:00",
                            },
                            {
                                "value": "20.23",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T13:00:00.000-06:00",
                            },
                            {
                                "value": "20.23",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T13:30:00.000-06:00",
                            },
                            {
                                "value": "20.24",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T14:00:00.000-06:00",
                            },
                            {
                                "value": "20.23",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T14:30:00.000-06:00",
                            },
                            {
                                "value": "20.25",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T15:00:00.000-06:00",
                            },
                            {
                                "value": "20.25",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T15:30:00.000-06:00",
                            },
                            {
                                "value": "20.25",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T16:00:00.000-06:00",
                            },
                            {
                                "value": "20.25",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T16:30:00.000-06:00",
                            },
                            {
                                "value": "20.24",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T17:00:00.000-06:00",
                            },
                            {
                                "value": "20.25",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T17:30:00.000-06:00",
                            },
                            {
                                "value": "20.25",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T18:00:00.000-06:00",
                            },
                            {
                                "value": "20.27",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T18:30:00.000-06:00",
                            },
                            {
                                "value": "20.25",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T19:00:00.000-06:00",
                            },
                            {
                                "value": "20.26",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T19:30:00.000-06:00",
                            },
                            {
                                "value": "20.25",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T20:00:00.000-06:00",
                            },
                            {
                                "value": "20.25",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T20:30:00.000-06:00",
                            },
                            {
                                "value": "20.26",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T21:00:00.000-06:00",
                            },
                            {
                                "value": "20.27",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T21:30:00.000-06:00",
                            },
                            {
                                "value": "20.27",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T22:00:00.000-06:00",
                            },
                            {
                                "value": "20.28",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T22:30:00.000-06:00",
                            },
                            {
                                "value": "20.28",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T23:00:00.000-06:00",
                            },
                            {
                                "value": "20.27",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T23:30:00.000-06:00",
                            },
                            {
                                "value": "20.28",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T00:00:00.000-06:00",
                            },
                            {
                                "value": "20.28",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T00:30:00.000-06:00",
                            },
                            {
                                "value": "20.28",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T01:00:00.000-06:00",
                            },
                            {
                                "value": "20.30",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T01:30:00.000-06:00",
                            },
                            {
                                "value": "20.30",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T02:00:00.000-06:00",
                            },
                            {
                                "value": "20.31",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T02:30:00.000-06:00",
                            },
                            {
                                "value": "20.30",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T03:00:00.000-06:00",
                            },
                            {
                                "value": "20.30",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T03:30:00.000-06:00",
                            },
                            {
                                "value": "20.33",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T04:00:00.000-06:00",
                            },
                            {
                                "value": "20.32",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T04:30:00.000-06:00",
                            },
                            {
                                "value": "20.33",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T05:00:00.000-06:00",
                            },
                            {
                                "value": "20.32",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T05:30:00.000-06:00",
                            },
                            {
                                "value": "20.33",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T06:00:00.000-06:00",
                            },
                            {
                                "value": "20.33",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T06:30:00.000-06:00",
                            },
                            {
                                "value": "20.32",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T07:00:00.000-06:00",
                            },
                            {
                                "value": "20.32",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T07:30:00.000-06:00",
                            },
                            {
                                "value": "20.32",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T08:00:00.000-06:00",
                            },
                            {
                                "value": "20.32",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T08:30:00.000-06:00",
                            },
                            {
                                "value": "20.33",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T09:00:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T09:30:00.000-06:00",
                            },
                            {
                                "value": "20.31",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T10:00:00.000-06:00",
                            },
                            {
                                "value": "20.32",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T10:30:00.000-06:00",
                            },
                            {
                                "value": "20.33",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T11:00:00.000-06:00",
                            },
                            {
                                "value": "20.32",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T11:30:00.000-06:00",
                            },
                            {
                                "value": "20.31",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T12:00:00.000-06:00",
                            },
                            {
                                "value": "20.32",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T12:30:00.000-06:00",
                            },
                            {
                                "value": "20.30",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T13:00:00.000-06:00",
                            },
                            {
                                "value": "20.32",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T13:30:00.000-06:00",
                            },
                            {
                                "value": "20.32",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T14:00:00.000-06:00",
                            },
                            {
                                "value": "20.31",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T14:30:00.000-06:00",
                            },
                            {
                                "value": "20.32",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T15:00:00.000-06:00",
                            },
                            {
                                "value": "20.32",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T15:30:00.000-06:00",
                            },
                            {
                                "value": "20.32",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T16:00:00.000-06:00",
                            },
                            {
                                "value": "20.31",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T16:30:00.000-06:00",
                            },
                            {
                                "value": "20.32",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T17:00:00.000-06:00",
                            },
                            {
                                "value": "20.32",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T17:30:00.000-06:00",
                            },
                            {
                                "value": "20.32",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T18:00:00.000-06:00",
                            },
                            {
                                "value": "20.32",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T18:30:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T19:00:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T19:30:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T20:00:00.000-06:00",
                            },
                            {
                                "value": "20.33",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T20:30:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T21:00:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T21:30:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T22:00:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T22:30:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T23:00:00.000-06:00",
                            },
                            {
                                "value": "20.35",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T23:30:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T00:00:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T00:30:00.000-06:00",
                            },
                            {
                                "value": "20.33",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T01:00:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T01:30:00.000-06:00",
                            },
                            {
                                "value": "20.35",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T02:00:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T02:30:00.000-06:00",
                            },
                            {
                                "value": "20.35",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T03:00:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T03:30:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T04:00:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T04:30:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T05:00:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T05:30:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T06:00:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T06:30:00.000-06:00",
                            },
                            {
                                "value": "20.35",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T07:00:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T07:30:00.000-06:00",
                            },
                            {
                                "value": "20.33",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T08:00:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T08:30:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T09:00:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T09:30:00.000-06:00",
                            },
                            {
                                "value": "20.33",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T10:00:00.000-06:00",
                            },
                            {
                                "value": "20.33",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T10:30:00.000-06:00",
                            },
                            {
                                "value": "20.32",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T11:00:00.000-06:00",
                            },
                            {
                                "value": "20.33",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T11:30:00.000-06:00",
                            },
                            {
                                "value": "20.33",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T12:00:00.000-06:00",
                            },
                            {
                                "value": "20.32",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T12:30:00.000-06:00",
                            },
                            {
                                "value": "20.32",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T13:00:00.000-06:00",
                            },
                            {
                                "value": "20.31",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T13:30:00.000-06:00",
                            },
                            {
                                "value": "20.32",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T14:00:00.000-06:00",
                            },
                            {
                                "value": "20.32",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T14:30:00.000-06:00",
                            },
                            {
                                "value": "20.32",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T15:00:00.000-06:00",
                            },
                            {
                                "value": "20.32",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T15:30:00.000-06:00",
                            },
                            {
                                "value": "20.32",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T16:00:00.000-06:00",
                            },
                            {
                                "value": "20.33",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T16:30:00.000-06:00",
                            },
                            {
                                "value": "20.36",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T17:00:00.000-06:00",
                            },
                            {
                                "value": "20.35",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T17:30:00.000-06:00",
                            },
                            {
                                "value": "20.35",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T18:00:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T18:30:00.000-06:00",
                            },
                            {
                                "value": "20.36",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T19:00:00.000-06:00",
                            },
                            {
                                "value": "20.36",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T19:30:00.000-06:00",
                            },
                            {
                                "value": "20.35",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T20:00:00.000-06:00",
                            },
                            {
                                "value": "20.35",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T20:30:00.000-06:00",
                            },
                            {
                                "value": "20.35",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T21:00:00.000-06:00",
                            },
                            {
                                "value": "20.35",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T21:30:00.000-06:00",
                            },
                            {
                                "value": "20.36",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T22:00:00.000-06:00",
                            },
                            {
                                "value": "20.36",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T22:30:00.000-06:00",
                            },
                            {
                                "value": "20.35",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T23:00:00.000-06:00",
                            },
                            {
                                "value": "20.35",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T23:30:00.000-06:00",
                            },
                            {
                                "value": "20.35",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T00:00:00.000-06:00",
                            },
                            {
                                "value": "20.36",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T00:30:00.000-06:00",
                            },
                            {
                                "value": "20.36",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T01:00:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T01:30:00.000-06:00",
                            },
                            {
                                "value": "20.35",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T02:00:00.000-06:00",
                            },
                            {
                                "value": "20.35",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T02:30:00.000-06:00",
                            },
                            {
                                "value": "20.35",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T03:00:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T03:30:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T04:00:00.000-06:00",
                            },
                            {
                                "value": "20.35",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T04:30:00.000-06:00",
                            },
                            {
                                "value": "20.37",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T05:00:00.000-06:00",
                            },
                            {
                                "value": "20.35",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T05:30:00.000-06:00",
                            },
                            {
                                "value": "20.35",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T06:00:00.000-06:00",
                            },
                            {
                                "value": "20.37",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T06:30:00.000-06:00",
                            },
                            {
                                "value": "20.36",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T07:00:00.000-06:00",
                            },
                            {
                                "value": "20.36",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T07:30:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T08:00:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T08:30:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T09:00:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T09:30:00.000-06:00",
                            },
                            {
                                "value": "20.33",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T10:00:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T10:30:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T11:00:00.000-06:00",
                            },
                            {
                                "value": "20.33",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T11:30:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T12:00:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T12:30:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T13:00:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T13:30:00.000-06:00",
                            },
                            {
                                "value": "20.33",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T14:00:00.000-06:00",
                            },
                            {
                                "value": "20.33",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T14:30:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T15:00:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T15:30:00.000-06:00",
                            },
                            {
                                "value": "20.35",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T16:00:00.000-06:00",
                            },
                            {
                                "value": "20.33",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T16:30:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T17:00:00.000-06:00",
                            },
                            {
                                "value": "20.33",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T17:30:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T18:00:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T18:30:00.000-06:00",
                            },
                            {
                                "value": "20.35",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T19:00:00.000-06:00",
                            },
                            {
                                "value": "20.36",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T19:30:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T20:00:00.000-06:00",
                            },
                            {
                                "value": "20.35",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T20:30:00.000-06:00",
                            },
                            {
                                "value": "20.36",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T21:00:00.000-06:00",
                            },
                            {
                                "value": "20.35",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T21:30:00.000-06:00",
                            },
                            {
                                "value": "20.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T22:00:00.000-06:00",
                            },
                            {
                                "value": "20.35",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T22:30:00.000-06:00",
                            },
                            {
                                "value": "20.35",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T23:00:00.000-06:00",
                            },
                            {
                                "value": "20.35",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T23:30:00.000-06:00",
                            },
                        ],
                        "qualifier": [
                            {
                                "qualifierCode": "P",
                                "qualifierDescription": "Provisional data subject to revision.",
                                "qualifierID": 0,
                                "network": "NWIS",
                                "vocabulary": "uv_rmk_cd",
                            }
                        ],
                        "qualityControlLevel": [],
                        "method": [{"methodDescription": "", "methodID": 62160}],
                        "source": [],
                        "offset": [],
                        "sample": [],
                        "censorCode": [],
                    }
                ],
                "name": "USGS:02489500:00065:00000",
            },
            {
                "sourceInfo": {
                    "siteName": "Pearl River near Bogalusa, LA",
                    "siteCode": [
                        {"value": "02489500", "network": "NWIS", "agencyCode": "USGS"}
                    ],
                    "timeZoneInfo": {
                        "defaultTimeZone": {
                            "zoneOffset": "-06:00",
                            "zoneAbbreviation": "CST",
                        },
                        "daylightSavingsTimeZone": {
                            "zoneOffset": "-05:00",
                            "zoneAbbreviation": "CDT",
                        },
                        "siteUsesDaylightSavingsTime": True,
                    },
                    "geoLocation": {
                        "geogLocation": {
                            "srs": "EPSG:4326",
                            "latitude": 30.79324276,
                            "longitude": -89.8209072,
                        },
                        "localSiteXY": [],
                    },
                    "note": [],
                    "siteType": [],
                    "siteProperty": [
                        {"value": "ST", "name": "siteTypeCd"},
                        {"value": "03180004", "name": "hucCd"},
                        {"value": "22", "name": "stateCd"},
                        {"value": "22117", "name": "countyCd"},
                    ],
                },
                "variable": {
                    "variableCode": [
                        {
                            "value": "63160",
                            "network": "NWIS",
                            "vocabulary": "NWIS:UnitValues",
                            "variableID": 51438657,
                            "default": True,
                        }
                    ],
                    "variableName": "Stream water level elevation above NAVD 1988, in ft",
                    "variableDescription": "Stream water level elevation above NAVD 1988, in feet",
                    "valueType": "Derived Value",
                    "unit": {"unitCode": "ft"},
                    "options": {
                        "option": [{"name": "Statistic", "optionCode": "00000"}]
                    },
                    "note": [],
                    "noDataValue": -999999.0,
                    "variableProperty": [],
                    "oid": "51438657",
                },
                "values": [
                    {
                        "value": [
                            {
                                "value": "74.50",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T00:00:00.000-06:00",
                            },
                            {
                                "value": "74.50",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T00:30:00.000-06:00",
                            },
                            {
                                "value": "74.52",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T01:00:00.000-06:00",
                            },
                            {
                                "value": "74.53",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T01:30:00.000-06:00",
                            },
                            {
                                "value": "74.54",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T02:00:00.000-06:00",
                            },
                            {
                                "value": "74.55",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T02:30:00.000-06:00",
                            },
                            {
                                "value": "74.56",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T03:00:00.000-06:00",
                            },
                            {
                                "value": "74.57",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T03:30:00.000-06:00",
                            },
                            {
                                "value": "74.59",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T04:00:00.000-06:00",
                            },
                            {
                                "value": "74.57",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T04:30:00.000-06:00",
                            },
                            {
                                "value": "74.59",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T05:00:00.000-06:00",
                            },
                            {
                                "value": "74.60",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T05:30:00.000-06:00",
                            },
                            {
                                "value": "74.61",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T06:00:00.000-06:00",
                            },
                            {
                                "value": "74.62",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T06:30:00.000-06:00",
                            },
                            {
                                "value": "74.64",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T07:00:00.000-06:00",
                            },
                            {
                                "value": "74.64",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T07:30:00.000-06:00",
                            },
                            {
                                "value": "74.64",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T08:00:00.000-06:00",
                            },
                            {
                                "value": "74.63",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T08:30:00.000-06:00",
                            },
                            {
                                "value": "74.65",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T09:00:00.000-06:00",
                            },
                            {
                                "value": "74.65",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T09:30:00.000-06:00",
                            },
                            {
                                "value": "74.65",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T10:00:00.000-06:00",
                            },
                            {
                                "value": "74.67",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T10:30:00.000-06:00",
                            },
                            {
                                "value": "74.67",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T11:00:00.000-06:00",
                            },
                            {
                                "value": "74.67",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T11:30:00.000-06:00",
                            },
                            {
                                "value": "74.68",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T12:00:00.000-06:00",
                            },
                            {
                                "value": "74.69",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T12:30:00.000-06:00",
                            },
                            {
                                "value": "74.69",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T13:00:00.000-06:00",
                            },
                            {
                                "value": "74.69",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T13:30:00.000-06:00",
                            },
                            {
                                "value": "74.69",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T14:00:00.000-06:00",
                            },
                            {
                                "value": "74.71",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T14:30:00.000-06:00",
                            },
                            {
                                "value": "74.71",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T15:00:00.000-06:00",
                            },
                            {
                                "value": "74.71",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T15:30:00.000-06:00",
                            },
                            {
                                "value": "74.72",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T16:00:00.000-06:00",
                            },
                            {
                                "value": "74.72",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T16:30:00.000-06:00",
                            },
                            {
                                "value": "74.72",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T17:00:00.000-06:00",
                            },
                            {
                                "value": "74.73",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T17:30:00.000-06:00",
                            },
                            {
                                "value": "74.74",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T18:00:00.000-06:00",
                            },
                            {
                                "value": "74.75",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T18:30:00.000-06:00",
                            },
                            {
                                "value": "74.75",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T19:00:00.000-06:00",
                            },
                            {
                                "value": "74.74",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T19:30:00.000-06:00",
                            },
                            {
                                "value": "74.76",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T20:00:00.000-06:00",
                            },
                            {
                                "value": "74.76",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T20:30:00.000-06:00",
                            },
                            {
                                "value": "74.76",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T21:00:00.000-06:00",
                            },
                            {
                                "value": "74.76",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T21:30:00.000-06:00",
                            },
                            {
                                "value": "74.78",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T22:00:00.000-06:00",
                            },
                            {
                                "value": "74.77",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T22:30:00.000-06:00",
                            },
                            {
                                "value": "74.79",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T23:00:00.000-06:00",
                            },
                            {
                                "value": "74.79",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T23:30:00.000-06:00",
                            },
                            {
                                "value": "74.79",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T00:00:00.000-06:00",
                            },
                            {
                                "value": "74.81",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T00:30:00.000-06:00",
                            },
                            {
                                "value": "74.81",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T01:00:00.000-06:00",
                            },
                            {
                                "value": "74.81",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T01:30:00.000-06:00",
                            },
                            {
                                "value": "74.82",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T02:00:00.000-06:00",
                            },
                            {
                                "value": "74.83",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T02:30:00.000-06:00",
                            },
                            {
                                "value": "74.84",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T03:00:00.000-06:00",
                            },
                            {
                                "value": "74.82",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T03:30:00.000-06:00",
                            },
                            {
                                "value": "74.83",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T04:00:00.000-06:00",
                            },
                            {
                                "value": "74.83",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T04:30:00.000-06:00",
                            },
                            {
                                "value": "74.85",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T05:00:00.000-06:00",
                            },
                            {
                                "value": "74.83",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T05:30:00.000-06:00",
                            },
                            {
                                "value": "74.85",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T06:00:00.000-06:00",
                            },
                            {
                                "value": "74.85",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T06:30:00.000-06:00",
                            },
                            {
                                "value": "74.84",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T07:00:00.000-06:00",
                            },
                            {
                                "value": "74.85",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T07:30:00.000-06:00",
                            },
                            {
                                "value": "74.85",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T08:00:00.000-06:00",
                            },
                            {
                                "value": "74.86",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T08:30:00.000-06:00",
                            },
                            {
                                "value": "74.86",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T09:00:00.000-06:00",
                            },
                            {
                                "value": "74.85",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T09:30:00.000-06:00",
                            },
                            {
                                "value": "74.87",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T10:00:00.000-06:00",
                            },
                            {
                                "value": "74.86",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T10:30:00.000-06:00",
                            },
                            {
                                "value": "74.86",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T11:00:00.000-06:00",
                            },
                            {
                                "value": "74.87",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T11:30:00.000-06:00",
                            },
                            {
                                "value": "74.87",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T12:00:00.000-06:00",
                            },
                            {
                                "value": "74.87",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T12:30:00.000-06:00",
                            },
                            {
                                "value": "74.87",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T13:00:00.000-06:00",
                            },
                            {
                                "value": "74.87",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T13:30:00.000-06:00",
                            },
                            {
                                "value": "74.88",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T14:00:00.000-06:00",
                            },
                            {
                                "value": "74.87",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T14:30:00.000-06:00",
                            },
                            {
                                "value": "74.89",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T15:00:00.000-06:00",
                            },
                            {
                                "value": "74.89",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T15:30:00.000-06:00",
                            },
                            {
                                "value": "74.89",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T16:00:00.000-06:00",
                            },
                            {
                                "value": "74.89",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T16:30:00.000-06:00",
                            },
                            {
                                "value": "74.88",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T17:00:00.000-06:00",
                            },
                            {
                                "value": "74.89",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T17:30:00.000-06:00",
                            },
                            {
                                "value": "74.89",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T18:00:00.000-06:00",
                            },
                            {
                                "value": "74.91",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T18:30:00.000-06:00",
                            },
                            {
                                "value": "74.89",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T19:00:00.000-06:00",
                            },
                            {
                                "value": "74.90",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T19:30:00.000-06:00",
                            },
                            {
                                "value": "74.89",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T20:00:00.000-06:00",
                            },
                            {
                                "value": "74.89",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T20:30:00.000-06:00",
                            },
                            {
                                "value": "74.90",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T21:00:00.000-06:00",
                            },
                            {
                                "value": "74.91",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T21:30:00.000-06:00",
                            },
                            {
                                "value": "74.91",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T22:00:00.000-06:00",
                            },
                            {
                                "value": "74.92",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T22:30:00.000-06:00",
                            },
                            {
                                "value": "74.92",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T23:00:00.000-06:00",
                            },
                            {
                                "value": "74.91",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T23:30:00.000-06:00",
                            },
                            {
                                "value": "74.92",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T00:00:00.000-06:00",
                            },
                            {
                                "value": "74.92",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T00:30:00.000-06:00",
                            },
                            {
                                "value": "74.92",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T01:00:00.000-06:00",
                            },
                            {
                                "value": "74.94",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T01:30:00.000-06:00",
                            },
                            {
                                "value": "74.94",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T02:00:00.000-06:00",
                            },
                            {
                                "value": "74.95",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T02:30:00.000-06:00",
                            },
                            {
                                "value": "74.94",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T03:00:00.000-06:00",
                            },
                            {
                                "value": "74.94",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T03:30:00.000-06:00",
                            },
                            {
                                "value": "74.97",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T04:00:00.000-06:00",
                            },
                            {
                                "value": "74.96",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T04:30:00.000-06:00",
                            },
                            {
                                "value": "74.97",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T05:00:00.000-06:00",
                            },
                            {
                                "value": "74.96",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T05:30:00.000-06:00",
                            },
                            {
                                "value": "74.97",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T06:00:00.000-06:00",
                            },
                            {
                                "value": "74.97",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T06:30:00.000-06:00",
                            },
                            {
                                "value": "74.96",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T07:00:00.000-06:00",
                            },
                            {
                                "value": "74.96",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T07:30:00.000-06:00",
                            },
                            {
                                "value": "74.96",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T08:00:00.000-06:00",
                            },
                            {
                                "value": "74.96",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T08:30:00.000-06:00",
                            },
                            {
                                "value": "74.97",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T09:00:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T09:30:00.000-06:00",
                            },
                            {
                                "value": "74.95",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T10:00:00.000-06:00",
                            },
                            {
                                "value": "74.96",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T10:30:00.000-06:00",
                            },
                            {
                                "value": "74.97",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T11:00:00.000-06:00",
                            },
                            {
                                "value": "74.96",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T11:30:00.000-06:00",
                            },
                            {
                                "value": "74.95",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T12:00:00.000-06:00",
                            },
                            {
                                "value": "74.96",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T12:30:00.000-06:00",
                            },
                            {
                                "value": "74.94",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T13:00:00.000-06:00",
                            },
                            {
                                "value": "74.96",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T13:30:00.000-06:00",
                            },
                            {
                                "value": "74.96",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T14:00:00.000-06:00",
                            },
                            {
                                "value": "74.95",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T14:30:00.000-06:00",
                            },
                            {
                                "value": "74.96",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T15:00:00.000-06:00",
                            },
                            {
                                "value": "74.96",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T15:30:00.000-06:00",
                            },
                            {
                                "value": "74.96",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T16:00:00.000-06:00",
                            },
                            {
                                "value": "74.95",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T16:30:00.000-06:00",
                            },
                            {
                                "value": "74.96",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T17:00:00.000-06:00",
                            },
                            {
                                "value": "74.96",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T17:30:00.000-06:00",
                            },
                            {
                                "value": "74.96",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T18:00:00.000-06:00",
                            },
                            {
                                "value": "74.96",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T18:30:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T19:00:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T19:30:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T20:00:00.000-06:00",
                            },
                            {
                                "value": "74.97",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T20:30:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T21:00:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T21:30:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T22:00:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T22:30:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T23:00:00.000-06:00",
                            },
                            {
                                "value": "74.99",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T23:30:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T00:00:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T00:30:00.000-06:00",
                            },
                            {
                                "value": "74.97",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T01:00:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T01:30:00.000-06:00",
                            },
                            {
                                "value": "74.99",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T02:00:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T02:30:00.000-06:00",
                            },
                            {
                                "value": "74.99",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T03:00:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T03:30:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T04:00:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T04:30:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T05:00:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T05:30:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T06:00:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T06:30:00.000-06:00",
                            },
                            {
                                "value": "74.99",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T07:00:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T07:30:00.000-06:00",
                            },
                            {
                                "value": "74.97",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T08:00:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T08:30:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T09:00:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T09:30:00.000-06:00",
                            },
                            {
                                "value": "74.97",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T10:00:00.000-06:00",
                            },
                            {
                                "value": "74.97",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T10:30:00.000-06:00",
                            },
                            {
                                "value": "74.96",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T11:00:00.000-06:00",
                            },
                            {
                                "value": "74.97",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T11:30:00.000-06:00",
                            },
                            {
                                "value": "74.97",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T12:00:00.000-06:00",
                            },
                            {
                                "value": "74.96",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T12:30:00.000-06:00",
                            },
                            {
                                "value": "74.96",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T13:00:00.000-06:00",
                            },
                            {
                                "value": "74.95",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T13:30:00.000-06:00",
                            },
                            {
                                "value": "74.96",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T14:00:00.000-06:00",
                            },
                            {
                                "value": "74.96",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T14:30:00.000-06:00",
                            },
                            {
                                "value": "74.96",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T15:00:00.000-06:00",
                            },
                            {
                                "value": "74.96",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T15:30:00.000-06:00",
                            },
                            {
                                "value": "74.96",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T16:00:00.000-06:00",
                            },
                            {
                                "value": "74.97",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T16:30:00.000-06:00",
                            },
                            {
                                "value": "75.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T17:00:00.000-06:00",
                            },
                            {
                                "value": "74.99",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T17:30:00.000-06:00",
                            },
                            {
                                "value": "74.99",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T18:00:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T18:30:00.000-06:00",
                            },
                            {
                                "value": "75.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T19:00:00.000-06:00",
                            },
                            {
                                "value": "75.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T19:30:00.000-06:00",
                            },
                            {
                                "value": "74.99",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T20:00:00.000-06:00",
                            },
                            {
                                "value": "74.99",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T20:30:00.000-06:00",
                            },
                            {
                                "value": "74.99",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T21:00:00.000-06:00",
                            },
                            {
                                "value": "74.99",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T21:30:00.000-06:00",
                            },
                            {
                                "value": "75.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T22:00:00.000-06:00",
                            },
                            {
                                "value": "75.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T22:30:00.000-06:00",
                            },
                            {
                                "value": "74.99",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T23:00:00.000-06:00",
                            },
                            {
                                "value": "74.99",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T23:30:00.000-06:00",
                            },
                            {
                                "value": "74.99",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T00:00:00.000-06:00",
                            },
                            {
                                "value": "75.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T00:30:00.000-06:00",
                            },
                            {
                                "value": "75.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T01:00:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T01:30:00.000-06:00",
                            },
                            {
                                "value": "74.99",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T02:00:00.000-06:00",
                            },
                            {
                                "value": "74.99",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T02:30:00.000-06:00",
                            },
                            {
                                "value": "74.99",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T03:00:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T03:30:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T04:00:00.000-06:00",
                            },
                            {
                                "value": "74.99",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T04:30:00.000-06:00",
                            },
                            {
                                "value": "75.01",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T05:00:00.000-06:00",
                            },
                            {
                                "value": "74.99",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T05:30:00.000-06:00",
                            },
                            {
                                "value": "74.99",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T06:00:00.000-06:00",
                            },
                            {
                                "value": "75.01",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T06:30:00.000-06:00",
                            },
                            {
                                "value": "75.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T07:00:00.000-06:00",
                            },
                            {
                                "value": "75.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T07:30:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T08:00:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T08:30:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T09:00:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T09:30:00.000-06:00",
                            },
                            {
                                "value": "74.97",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T10:00:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T10:30:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T11:00:00.000-06:00",
                            },
                            {
                                "value": "74.97",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T11:30:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T12:00:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T12:30:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T13:00:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T13:30:00.000-06:00",
                            },
                            {
                                "value": "74.97",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T14:00:00.000-06:00",
                            },
                            {
                                "value": "74.97",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T14:30:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T15:00:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T15:30:00.000-06:00",
                            },
                            {
                                "value": "74.99",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T16:00:00.000-06:00",
                            },
                            {
                                "value": "74.97",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T16:30:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T17:00:00.000-06:00",
                            },
                            {
                                "value": "74.97",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T17:30:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T18:00:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T18:30:00.000-06:00",
                            },
                            {
                                "value": "74.99",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T19:00:00.000-06:00",
                            },
                            {
                                "value": "75.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T19:30:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T20:00:00.000-06:00",
                            },
                            {
                                "value": "74.99",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T20:30:00.000-06:00",
                            },
                            {
                                "value": "75.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T21:00:00.000-06:00",
                            },
                            {
                                "value": "74.99",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T21:30:00.000-06:00",
                            },
                            {
                                "value": "74.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T22:00:00.000-06:00",
                            },
                            {
                                "value": "74.99",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T22:30:00.000-06:00",
                            },
                            {
                                "value": "74.99",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T23:00:00.000-06:00",
                            },
                            {
                                "value": "74.99",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T23:30:00.000-06:00",
                            },
                        ],
                        "qualifier": [
                            {
                                "qualifierCode": "P",
                                "qualifierDescription": "Provisional data subject to revision.",
                                "qualifierID": 0,
                                "network": "NWIS",
                                "vocabulary": "uv_rmk_cd",
                            }
                        ],
                        "qualityControlLevel": [],
                        "method": [{"methodDescription": "", "methodID": 62163}],
                        "source": [],
                        "offset": [],
                        "sample": [],
                        "censorCode": [],
                    }
                ],
                "name": "USGS:02489500:63160:00000",
            },
            {
                "sourceInfo": {
                    "siteName": "Bogue Chitto River near Bush, LA",
                    "siteCode": [
                        {"value": "02492000", "network": "NWIS", "agencyCode": "USGS"}
                    ],
                    "timeZoneInfo": {
                        "defaultTimeZone": {
                            "zoneOffset": "-06:00",
                            "zoneAbbreviation": "CST",
                        },
                        "daylightSavingsTimeZone": {
                            "zoneOffset": "-05:00",
                            "zoneAbbreviation": "CDT",
                        },
                        "siteUsesDaylightSavingsTime": True,
                    },
                    "geoLocation": {
                        "geogLocation": {
                            "srs": "EPSG:4326",
                            "latitude": 30.62935636,
                            "longitude": -89.8972956,
                        },
                        "localSiteXY": [],
                    },
                    "note": [],
                    "siteType": [],
                    "siteProperty": [
                        {"value": "ST", "name": "siteTypeCd"},
                        {"value": "03180005", "name": "hucCd"},
                        {"value": "22", "name": "stateCd"},
                        {"value": "22103", "name": "countyCd"},
                    ],
                },
                "variable": {
                    "variableCode": [
                        {
                            "value": "00035",
                            "network": "NWIS",
                            "vocabulary": "NWIS:UnitValues",
                            "variableID": 45807109,
                            "default": True,
                        }
                    ],
                    "variableName": "Wind speed, mph",
                    "variableDescription": "Wind speed, miles per hour",
                    "valueType": "Derived Value",
                    "unit": {"unitCode": "mph"},
                    "options": {
                        "option": [{"name": "Statistic", "optionCode": "00000"}]
                    },
                    "note": [],
                    "noDataValue": -999999.0,
                    "variableProperty": [],
                    "oid": "45807109",
                },
                "values": [
                    {
                        "value": [
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T00:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T00:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T01:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T01:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T02:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T02:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T03:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T03:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T04:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T04:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T05:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T05:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T06:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T06:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T07:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T07:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T08:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T08:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T09:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T09:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T10:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T10:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T11:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T11:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T12:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T12:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T13:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T13:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T14:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T14:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T15:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T15:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T16:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T16:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T17:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T17:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T18:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T18:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T19:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T19:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T20:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T20:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T21:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T21:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T22:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T22:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T23:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T23:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T00:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T00:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T01:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T01:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T02:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T02:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T03:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T03:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T04:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T04:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T05:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T05:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T06:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T06:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T07:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T07:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T08:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T08:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T09:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T09:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T10:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T10:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T11:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T11:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T12:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T12:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T13:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T13:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T14:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T14:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T15:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T15:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T16:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T16:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T17:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T17:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T18:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T18:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T19:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T19:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T20:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T20:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T21:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T21:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T22:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T22:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T23:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T23:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T00:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T00:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T01:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T01:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T02:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T02:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T03:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T03:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T04:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T04:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T05:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T05:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T06:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T06:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T07:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T07:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T08:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T08:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T09:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T09:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T10:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T10:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T11:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T11:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T12:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T12:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T13:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T13:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T14:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T14:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T15:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T15:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T16:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T16:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T17:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T17:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T18:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T18:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T19:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T19:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T20:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T20:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T21:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T21:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T22:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T22:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T23:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T23:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T00:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T00:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T01:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T01:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T02:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T02:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T03:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T03:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T04:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T04:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T05:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T05:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T06:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T06:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T07:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T07:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T08:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T08:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T09:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T09:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T10:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T10:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T11:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T11:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T12:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T12:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T13:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T13:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T14:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T14:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T15:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T15:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T16:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T16:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T17:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T17:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T18:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T18:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T19:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T19:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T20:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T20:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T21:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T21:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T22:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T22:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T23:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T23:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T00:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T00:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T01:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T01:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T02:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T02:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T03:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T03:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T04:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T04:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T05:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T05:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T06:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T06:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T07:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T07:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T08:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T08:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T09:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T09:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T10:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T10:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T11:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T11:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T12:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T12:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T13:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T13:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T14:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T14:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T15:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T15:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T16:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T16:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T17:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T17:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T18:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T18:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T19:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T19:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T20:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T20:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T21:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T21:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T22:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T22:30:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T23:00:00.000-06:00",
                            },
                            {
                                "value": "-5.0",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T23:30:00.000-06:00",
                            },
                        ],
                        "qualifier": [
                            {
                                "qualifierCode": "P",
                                "qualifierDescription": "Provisional data subject to revision.",
                                "qualifierID": 0,
                                "network": "NWIS",
                                "vocabulary": "uv_rmk_cd",
                            }
                        ],
                        "qualityControlLevel": [],
                        "method": [{"methodDescription": "", "methodID": 242211}],
                        "source": [],
                        "offset": [],
                        "sample": [],
                        "censorCode": [],
                    }
                ],
                "name": "USGS:02492000:00035:00000",
            },
            {
                "sourceInfo": {
                    "siteName": "Bogue Chitto River near Bush, LA",
                    "siteCode": [
                        {"value": "02492000", "network": "NWIS", "agencyCode": "USGS"}
                    ],
                    "timeZoneInfo": {
                        "defaultTimeZone": {
                            "zoneOffset": "-06:00",
                            "zoneAbbreviation": "CST",
                        },
                        "daylightSavingsTimeZone": {
                            "zoneOffset": "-05:00",
                            "zoneAbbreviation": "CDT",
                        },
                        "siteUsesDaylightSavingsTime": True,
                    },
                    "geoLocation": {
                        "geogLocation": {
                            "srs": "EPSG:4326",
                            "latitude": 30.62935636,
                            "longitude": -89.8972956,
                        },
                        "localSiteXY": [],
                    },
                    "note": [],
                    "siteType": [],
                    "siteProperty": [
                        {"value": "ST", "name": "siteTypeCd"},
                        {"value": "03180005", "name": "hucCd"},
                        {"value": "22", "name": "stateCd"},
                        {"value": "22103", "name": "countyCd"},
                    ],
                },
                "variable": {
                    "variableCode": [
                        {
                            "value": "00036",
                            "network": "NWIS",
                            "vocabulary": "NWIS:UnitValues",
                            "variableID": 45807110,
                            "default": True,
                        }
                    ],
                    "variableName": "Wind direction, degrees clockwise from north",
                    "variableDescription": "Wind direction, degrees clockwise from true north",
                    "valueType": "Derived Value",
                    "unit": {"unitCode": "Deg"},
                    "options": {
                        "option": [{"name": "Statistic", "optionCode": "00000"}]
                    },
                    "note": [],
                    "noDataValue": -999999.0,
                    "variableProperty": [],
                    "oid": "45807110",
                },
                "values": [
                    {
                        "value": [
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T00:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T00:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T01:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T01:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T02:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T02:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T03:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T03:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T04:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T04:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T05:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T05:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T06:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T06:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T07:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T07:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T08:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T08:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T09:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T09:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T10:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T10:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T11:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T11:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T12:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T12:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T13:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T13:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T14:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T14:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T15:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T15:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T16:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T16:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T17:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T17:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T18:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T18:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T19:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T19:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T20:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T20:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T21:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T21:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T22:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T22:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T23:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T23:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T00:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T00:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T01:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T01:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T02:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T02:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T03:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T03:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T04:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T04:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T05:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T05:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T06:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T06:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T07:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T07:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T08:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T08:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T09:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T09:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T10:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T10:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T11:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T11:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T12:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T12:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T13:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T13:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T14:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T14:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T15:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T15:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T16:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T16:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T17:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T17:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T18:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T18:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T19:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T19:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T20:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T20:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T21:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T21:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T22:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T22:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T23:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T23:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T00:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T00:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T01:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T01:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T02:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T02:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T03:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T03:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T04:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T04:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T05:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T05:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T06:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T06:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T07:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T07:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T08:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T08:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T09:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T09:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T10:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T10:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T11:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T11:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T12:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T12:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T13:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T13:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T14:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T14:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T15:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T15:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T16:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T16:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T17:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T17:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T18:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T18:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T19:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T19:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T20:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T20:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T21:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T21:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T22:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T22:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T23:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T23:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T00:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T00:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T01:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T01:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T02:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T02:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T03:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T03:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T04:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T04:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T05:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T05:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T06:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T06:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T07:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T07:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T08:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T08:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T09:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T09:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T10:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T10:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T11:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T11:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T12:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T12:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T13:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T13:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T14:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T14:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T15:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T15:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T16:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T16:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T17:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T17:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T18:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T18:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T19:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T19:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T20:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T20:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T21:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T21:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T22:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T22:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T23:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T23:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T00:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T00:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T01:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T01:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T02:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T02:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T03:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T03:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T04:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T04:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T05:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T05:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T06:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T06:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T07:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T07:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T08:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T08:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T09:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T09:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T10:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T10:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T11:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T11:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T12:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T12:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T13:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T13:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T14:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T14:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T15:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T15:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T16:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T16:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T17:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T17:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T18:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T18:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T19:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T19:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T20:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T20:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T21:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T21:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T22:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T22:30:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T23:00:00.000-06:00",
                            },
                            {
                                "value": "-5",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T23:30:00.000-06:00",
                            },
                        ],
                        "qualifier": [
                            {
                                "qualifierCode": "P",
                                "qualifierDescription": "Provisional data subject to revision.",
                                "qualifierID": 0,
                                "network": "NWIS",
                                "vocabulary": "uv_rmk_cd",
                            }
                        ],
                        "qualityControlLevel": [],
                        "method": [{"methodDescription": "", "methodID": 242210}],
                        "source": [],
                        "offset": [],
                        "sample": [],
                        "censorCode": [],
                    }
                ],
                "name": "USGS:02492000:00036:00000",
            },
            {
                "sourceInfo": {
                    "siteName": "Bogue Chitto River near Bush, LA",
                    "siteCode": [
                        {"value": "02492000", "network": "NWIS", "agencyCode": "USGS"}
                    ],
                    "timeZoneInfo": {
                        "defaultTimeZone": {
                            "zoneOffset": "-06:00",
                            "zoneAbbreviation": "CST",
                        },
                        "daylightSavingsTimeZone": {
                            "zoneOffset": "-05:00",
                            "zoneAbbreviation": "CDT",
                        },
                        "siteUsesDaylightSavingsTime": True,
                    },
                    "geoLocation": {
                        "geogLocation": {
                            "srs": "EPSG:4326",
                            "latitude": 30.62935636,
                            "longitude": -89.8972956,
                        },
                        "localSiteXY": [],
                    },
                    "note": [],
                    "siteType": [],
                    "siteProperty": [
                        {"value": "ST", "name": "siteTypeCd"},
                        {"value": "03180005", "name": "hucCd"},
                        {"value": "22", "name": "stateCd"},
                        {"value": "22103", "name": "countyCd"},
                    ],
                },
                "variable": {
                    "variableCode": [
                        {
                            "value": "00045",
                            "network": "NWIS",
                            "vocabulary": "NWIS:UnitValues",
                            "variableID": 45807140,
                            "default": True,
                        }
                    ],
                    "variableName": "Precipitation, total, in",
                    "variableDescription": "Precipitation, total, inches",
                    "valueType": "Derived Value",
                    "unit": {"unitCode": "in"},
                    "options": {
                        "option": [{"name": "Statistic", "optionCode": "00000"}]
                    },
                    "note": [],
                    "noDataValue": -999999.0,
                    "variableProperty": [],
                    "oid": "45807140",
                },
                "values": [
                    {
                        "value": [
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T00:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T00:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T01:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T01:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T02:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T02:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T03:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T03:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T04:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T04:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T05:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T05:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T06:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T06:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T07:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T19:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T20:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T20:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T21:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T21:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T22:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T22:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T23:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T23:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T00:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T00:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T01:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T01:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T02:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T02:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T03:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T03:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T04:00:00.000-06:00",
                            },
                            {
                                "value": "0.01",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T04:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T05:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T05:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T06:00:00.000-06:00",
                            },
                            {
                                "value": "0.01",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T06:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T07:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T07:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T08:00:00.000-06:00",
                            },
                            {
                                "value": "0.06",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T11:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T12:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T12:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T13:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T13:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T14:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T14:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T15:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T15:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T16:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T16:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T17:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T17:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T18:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T18:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T19:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T19:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T20:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T20:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T21:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T21:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T22:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T22:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T23:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T23:30:00.000-06:00",
                            },
                            {
                                "value": "0.08",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T00:00:00.000-06:00",
                            },
                            {
                                "value": "0.23",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T00:30:00.000-06:00",
                            },
                            {
                                "value": "0.10",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T01:00:00.000-06:00",
                            },
                            {
                                "value": "0.27",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T01:30:00.000-06:00",
                            },
                            {
                                "value": "0.07",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T02:00:00.000-06:00",
                            },
                            {
                                "value": "0.10",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T02:30:00.000-06:00",
                            },
                            {
                                "value": "0.06",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T03:00:00.000-06:00",
                            },
                            {
                                "value": "0.01",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T03:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T04:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T04:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T05:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T05:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T06:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T06:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T07:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T07:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T08:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T08:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T09:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T09:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T10:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T10:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T11:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T11:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T12:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T12:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T13:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T13:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T14:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T14:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T15:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T15:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T16:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T16:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T17:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T17:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T18:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T18:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T19:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T19:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T20:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T20:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T21:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T21:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T22:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T22:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T23:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T23:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T00:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T00:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T01:00:00.000-06:00",
                            },
                            {
                                "value": "0.01",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T01:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T02:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T02:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T03:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T03:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T04:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T04:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T05:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T05:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T06:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T06:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T07:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T07:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T08:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T08:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T09:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T09:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T10:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T10:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T11:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T11:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T12:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T12:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T13:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T13:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T14:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T14:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T15:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T15:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T16:00:00.000-06:00",
                            },
                            {
                                "value": "0.02",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T16:30:00.000-06:00",
                            },
                            {
                                "value": "0.01",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T17:00:00.000-06:00",
                            },
                            {
                                "value": "0.05",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T17:30:00.000-06:00",
                            },
                            {
                                "value": "0.02",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T18:00:00.000-06:00",
                            },
                            {
                                "value": "0.08",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T18:30:00.000-06:00",
                            },
                            {
                                "value": "0.02",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T19:00:00.000-06:00",
                            },
                            {
                                "value": "0.03",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T19:30:00.000-06:00",
                            },
                            {
                                "value": "0.01",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T20:00:00.000-06:00",
                            },
                            {
                                "value": "0.02",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T20:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T21:00:00.000-06:00",
                            },
                            {
                                "value": "0.01",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T21:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T22:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T22:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T23:00:00.000-06:00",
                            },
                            {
                                "value": "0.15",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T23:30:00.000-06:00",
                            },
                            {
                                "value": "0.03",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T00:00:00.000-06:00",
                            },
                            {
                                "value": "0.18",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T00:30:00.000-06:00",
                            },
                            {
                                "value": "0.01",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T01:00:00.000-06:00",
                            },
                            {
                                "value": "0.01",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T01:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T02:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T02:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T03:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T03:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T04:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T04:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T05:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T05:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T06:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T06:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T07:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T07:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T08:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T08:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T09:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T09:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T10:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T10:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T11:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T11:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T12:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T12:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T13:00:00.000-06:00",
                            },
                            {
                                "value": "0.03",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T13:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T14:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T14:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T15:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T15:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T16:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T16:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T17:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T17:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T18:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T18:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T19:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T19:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T20:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T20:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T21:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T21:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T22:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T22:30:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T23:00:00.000-06:00",
                            },
                            {
                                "value": "0.00",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T23:30:00.000-06:00",
                            },
                        ],
                        "qualifier": [
                            {
                                "qualifierCode": "P",
                                "qualifierDescription": "Provisional data subject to revision.",
                                "qualifierID": 0,
                                "network": "NWIS",
                                "vocabulary": "uv_rmk_cd",
                            }
                        ],
                        "qualityControlLevel": [],
                        "method": [{"methodDescription": "", "methodID": 62176}],
                        "source": [],
                        "offset": [],
                        "sample": [],
                        "censorCode": [],
                    }
                ],
                "name": "USGS:02492000:00045:00000",
            },
            {
                "sourceInfo": {
                    "siteName": "Bogue Chitto River near Bush, LA",
                    "siteCode": [
                        {"value": "02492000", "network": "NWIS", "agencyCode": "USGS"}
                    ],
                    "timeZoneInfo": {
                        "defaultTimeZone": {
                            "zoneOffset": "-06:00",
                            "zoneAbbreviation": "CST",
                        },
                        "daylightSavingsTimeZone": {
                            "zoneOffset": "-05:00",
                            "zoneAbbreviation": "CDT",
                        },
                        "siteUsesDaylightSavingsTime": True,
                    },
                    "geoLocation": {
                        "geogLocation": {
                            "srs": "EPSG:4326",
                            "latitude": 30.62935636,
                            "longitude": -89.8972956,
                        },
                        "localSiteXY": [],
                    },
                    "note": [],
                    "siteType": [],
                    "siteProperty": [
                        {"value": "ST", "name": "siteTypeCd"},
                        {"value": "03180005", "name": "hucCd"},
                        {"value": "22", "name": "stateCd"},
                        {"value": "22103", "name": "countyCd"},
                    ],
                },
                "variable": {
                    "variableCode": [
                        {
                            "value": "00060",
                            "network": "NWIS",
                            "vocabulary": "NWIS:UnitValues",
                            "variableID": 45807197,
                            "default": True,
                        }
                    ],
                    "variableName": "Streamflow, ft&#179;/s",
                    "variableDescription": "Discharge, cubic feet per second",
                    "valueType": "Derived Value",
                    "unit": {"unitCode": "ft3/s"},
                    "options": {
                        "option": [{"name": "Statistic", "optionCode": "00000"}]
                    },
                    "note": [],
                    "noDataValue": -999999.0,
                    "variableProperty": [],
                    "oid": "45807197",
                },
                "values": [
                    {
                        "value": [
                            {
                                "value": "6420",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T00:00:00.000-06:00",
                            },
                            {
                                "value": "6420",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T00:30:00.000-06:00",
                            },
                            {
                                "value": "6420",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T01:00:00.000-06:00",
                            },
                            {
                                "value": "6420",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T01:30:00.000-06:00",
                            },
                            {
                                "value": "6390",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T02:00:00.000-06:00",
                            },
                            {
                                "value": "6390",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T02:30:00.000-06:00",
                            },
                            {
                                "value": "6390",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T03:00:00.000-06:00",
                            },
                            {
                                "value": "6350",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T03:30:00.000-06:00",
                            },
                            {
                                "value": "6320",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T04:00:00.000-06:00",
                            },
                            {
                                "value": "6320",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T04:30:00.000-06:00",
                            },
                            {
                                "value": "6290",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T05:00:00.000-06:00",
                            },
                            {
                                "value": "6260",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T05:30:00.000-06:00",
                            },
                            {
                                "value": "6290",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T06:00:00.000-06:00",
                            },
                            {
                                "value": "6230",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T06:30:00.000-06:00",
                            },
                            {
                                "value": "6200",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T07:00:00.000-06:00",
                            },
                            {
                                "value": "6130",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T07:30:00.000-06:00",
                            },
                            {
                                "value": "6130",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T08:00:00.000-06:00",
                            },
                            {
                                "value": "6100",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T08:30:00.000-06:00",
                            },
                            {
                                "value": "6070",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T09:00:00.000-06:00",
                            },
                            {
                                "value": "6040",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T09:30:00.000-06:00",
                            },
                            {
                                "value": "5980",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T10:00:00.000-06:00",
                            },
                            {
                                "value": "5980",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T10:30:00.000-06:00",
                            },
                            {
                                "value": "5980",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T11:00:00.000-06:00",
                            },
                            {
                                "value": "5880",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T11:30:00.000-06:00",
                            },
                            {
                                "value": "5880",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T12:00:00.000-06:00",
                            },
                            {
                                "value": "5820",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T12:30:00.000-06:00",
                            },
                            {
                                "value": "5820",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T13:00:00.000-06:00",
                            },
                            {
                                "value": "5700",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T13:30:00.000-06:00",
                            },
                            {
                                "value": "5730",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T14:00:00.000-06:00",
                            },
                            {
                                "value": "5640",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T14:30:00.000-06:00",
                            },
                            {
                                "value": "5610",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T15:00:00.000-06:00",
                            },
                            {
                                "value": "5550",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T15:30:00.000-06:00",
                            },
                            {
                                "value": "5520",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T16:00:00.000-06:00",
                            },
                            {
                                "value": "5430",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T16:30:00.000-06:00",
                            },
                            {
                                "value": "5430",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T17:00:00.000-06:00",
                            },
                            {
                                "value": "5310",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T17:30:00.000-06:00",
                            },
                            {
                                "value": "5280",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T18:00:00.000-06:00",
                            },
                            {
                                "value": "5220",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T18:30:00.000-06:00",
                            },
                            {
                                "value": "5160",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T19:00:00.000-06:00",
                            },
                            {
                                "value": "5110",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T19:30:00.000-06:00",
                            },
                            {
                                "value": "5090",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T20:00:00.000-06:00",
                            },
                            {
                                "value": "5010",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T20:30:00.000-06:00",
                            },
                            {
                                "value": "4990",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T21:00:00.000-06:00",
                            },
                            {
                                "value": "4920",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T21:30:00.000-06:00",
                            },
                            {
                                "value": "4900",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T22:00:00.000-06:00",
                            },
                            {
                                "value": "4850",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T22:30:00.000-06:00",
                            },
                            {
                                "value": "4840",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T23:00:00.000-06:00",
                            },
                            {
                                "value": "4790",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T23:30:00.000-06:00",
                            },
                            {
                                "value": "4780",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T00:00:00.000-06:00",
                            },
                            {
                                "value": "4730",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T00:30:00.000-06:00",
                            },
                            {
                                "value": "4700",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T01:00:00.000-06:00",
                            },
                            {
                                "value": "4650",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T01:30:00.000-06:00",
                            },
                            {
                                "value": "4630",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T02:00:00.000-06:00",
                            },
                            {
                                "value": "4580",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T02:30:00.000-06:00",
                            },
                            {
                                "value": "4560",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T03:00:00.000-06:00",
                            },
                            {
                                "value": "4520",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T03:30:00.000-06:00",
                            },
                            {
                                "value": "4500",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T04:00:00.000-06:00",
                            },
                            {
                                "value": "4450",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T04:30:00.000-06:00",
                            },
                            {
                                "value": "4440",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T05:00:00.000-06:00",
                            },
                            {
                                "value": "4390",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T05:30:00.000-06:00",
                            },
                            {
                                "value": "4370",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T06:00:00.000-06:00",
                            },
                            {
                                "value": "4330",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T06:30:00.000-06:00",
                            },
                            {
                                "value": "4310",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T07:00:00.000-06:00",
                            },
                            {
                                "value": "4270",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T07:30:00.000-06:00",
                            },
                            {
                                "value": "4250",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T08:00:00.000-06:00",
                            },
                            {
                                "value": "4210",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T08:30:00.000-06:00",
                            },
                            {
                                "value": "4170",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T09:00:00.000-06:00",
                            },
                            {
                                "value": "4140",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T09:30:00.000-06:00",
                            },
                            {
                                "value": "4130",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T10:00:00.000-06:00",
                            },
                            {
                                "value": "4080",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T10:30:00.000-06:00",
                            },
                            {
                                "value": "4070",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T11:00:00.000-06:00",
                            },
                            {
                                "value": "4020",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T11:30:00.000-06:00",
                            },
                            {
                                "value": "4010",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T12:00:00.000-06:00",
                            },
                            {
                                "value": "3970",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T12:30:00.000-06:00",
                            },
                            {
                                "value": "3960",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T13:00:00.000-06:00",
                            },
                            {
                                "value": "3920",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T13:30:00.000-06:00",
                            },
                            {
                                "value": "3900",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T14:00:00.000-06:00",
                            },
                            {
                                "value": "3870",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T14:30:00.000-06:00",
                            },
                            {
                                "value": "3840",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T15:00:00.000-06:00",
                            },
                            {
                                "value": "3810",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T15:30:00.000-06:00",
                            },
                            {
                                "value": "3800",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T16:00:00.000-06:00",
                            },
                            {
                                "value": "3750",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T16:30:00.000-06:00",
                            },
                            {
                                "value": "3750",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T17:00:00.000-06:00",
                            },
                            {
                                "value": "3700",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T17:30:00.000-06:00",
                            },
                            {
                                "value": "3690",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T18:00:00.000-06:00",
                            },
                            {
                                "value": "3640",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T18:30:00.000-06:00",
                            },
                            {
                                "value": "3630",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T19:00:00.000-06:00",
                            },
                            {
                                "value": "3590",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T19:30:00.000-06:00",
                            },
                            {
                                "value": "3580",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T20:00:00.000-06:00",
                            },
                            {
                                "value": "3540",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T20:30:00.000-06:00",
                            },
                            {
                                "value": "3520",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T21:00:00.000-06:00",
                            },
                            {
                                "value": "3490",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T21:30:00.000-06:00",
                            },
                            {
                                "value": "3470",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T22:00:00.000-06:00",
                            },
                            {
                                "value": "3430",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T22:30:00.000-06:00",
                            },
                            {
                                "value": "3420",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T23:00:00.000-06:00",
                            },
                            {
                                "value": "3390",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T23:30:00.000-06:00",
                            },
                            {
                                "value": "3350",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T00:00:00.000-06:00",
                            },
                            {
                                "value": "3320",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T00:30:00.000-06:00",
                            },
                            {
                                "value": "3320",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T01:00:00.000-06:00",
                            },
                            {
                                "value": "3310",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T01:30:00.000-06:00",
                            },
                            {
                                "value": "3310",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T02:00:00.000-06:00",
                            },
                            {
                                "value": "3300",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T02:30:00.000-06:00",
                            },
                            {
                                "value": "3280",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T03:00:00.000-06:00",
                            },
                            {
                                "value": "3270",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T03:30:00.000-06:00",
                            },
                            {
                                "value": "3270",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T04:00:00.000-06:00",
                            },
                            {
                                "value": "3250",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T04:30:00.000-06:00",
                            },
                            {
                                "value": "3240",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T05:00:00.000-06:00",
                            },
                            {
                                "value": "3210",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T05:30:00.000-06:00",
                            },
                            {
                                "value": "3210",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T06:00:00.000-06:00",
                            },
                            {
                                "value": "3180",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T06:30:00.000-06:00",
                            },
                            {
                                "value": "3180",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T07:00:00.000-06:00",
                            },
                            {
                                "value": "3150",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T07:30:00.000-06:00",
                            },
                            {
                                "value": "3150",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T08:00:00.000-06:00",
                            },
                            {
                                "value": "3120",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T08:30:00.000-06:00",
                            },
                            {
                                "value": "3120",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T09:00:00.000-06:00",
                            },
                            {
                                "value": "3090",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T09:30:00.000-06:00",
                            },
                            {
                                "value": "3080",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T10:00:00.000-06:00",
                            },
                            {
                                "value": "3060",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T10:30:00.000-06:00",
                            },
                            {
                                "value": "3060",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T11:00:00.000-06:00",
                            },
                            {
                                "value": "3040",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T11:30:00.000-06:00",
                            },
                            {
                                "value": "3030",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T12:00:00.000-06:00",
                            },
                            {
                                "value": "3010",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T12:30:00.000-06:00",
                            },
                            {
                                "value": "3010",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T13:00:00.000-06:00",
                            },
                            {
                                "value": "3010",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T13:30:00.000-06:00",
                            },
                            {
                                "value": "3010",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T14:00:00.000-06:00",
                            },
                            {
                                "value": "2980",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T14:30:00.000-06:00",
                            },
                            {
                                "value": "2980",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T15:00:00.000-06:00",
                            },
                            {
                                "value": "2970",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T15:30:00.000-06:00",
                            },
                            {
                                "value": "2960",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T16:00:00.000-06:00",
                            },
                            {
                                "value": "2960",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T16:30:00.000-06:00",
                            },
                            {
                                "value": "2950",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T17:00:00.000-06:00",
                            },
                            {
                                "value": "2940",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T17:30:00.000-06:00",
                            },
                            {
                                "value": "2930",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T18:00:00.000-06:00",
                            },
                            {
                                "value": "2940",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T18:30:00.000-06:00",
                            },
                            {
                                "value": "2930",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T19:00:00.000-06:00",
                            },
                            {
                                "value": "2920",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T19:30:00.000-06:00",
                            },
                            {
                                "value": "2920",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T20:00:00.000-06:00",
                            },
                            {
                                "value": "2910",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T20:30:00.000-06:00",
                            },
                            {
                                "value": "2910",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T21:00:00.000-06:00",
                            },
                            {
                                "value": "2900",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T21:30:00.000-06:00",
                            },
                            {
                                "value": "2900",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T22:00:00.000-06:00",
                            },
                            {
                                "value": "2890",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T22:30:00.000-06:00",
                            },
                            {
                                "value": "2890",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T23:00:00.000-06:00",
                            },
                            {
                                "value": "2890",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T23:30:00.000-06:00",
                            },
                            {
                                "value": "2890",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T00:00:00.000-06:00",
                            },
                            {
                                "value": "2880",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T00:30:00.000-06:00",
                            },
                            {
                                "value": "2890",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T01:00:00.000-06:00",
                            },
                            {
                                "value": "2880",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T01:30:00.000-06:00",
                            },
                            {
                                "value": "2880",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T02:00:00.000-06:00",
                            },
                            {
                                "value": "2880",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T02:30:00.000-06:00",
                            },
                            {
                                "value": "2880",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T03:00:00.000-06:00",
                            },
                            {
                                "value": "2880",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T03:30:00.000-06:00",
                            },
                            {
                                "value": "2880",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T04:00:00.000-06:00",
                            },
                            {
                                "value": "2880",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T04:30:00.000-06:00",
                            },
                            {
                                "value": "2880",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T05:00:00.000-06:00",
                            },
                            {
                                "value": "2880",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T05:30:00.000-06:00",
                            },
                            {
                                "value": "2880",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T06:00:00.000-06:00",
                            },
                            {
                                "value": "2880",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T06:30:00.000-06:00",
                            },
                            {
                                "value": "2880",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T07:00:00.000-06:00",
                            },
                            {
                                "value": "2880",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T07:30:00.000-06:00",
                            },
                            {
                                "value": "2880",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T08:00:00.000-06:00",
                            },
                            {
                                "value": "2870",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T08:30:00.000-06:00",
                            },
                            {
                                "value": "2870",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T09:00:00.000-06:00",
                            },
                            {
                                "value": "2870",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T09:30:00.000-06:00",
                            },
                            {
                                "value": "2870",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T10:00:00.000-06:00",
                            },
                            {
                                "value": "2870",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T10:30:00.000-06:00",
                            },
                            {
                                "value": "2870",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T11:00:00.000-06:00",
                            },
                            {
                                "value": "2870",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T11:30:00.000-06:00",
                            },
                            {
                                "value": "2860",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T12:00:00.000-06:00",
                            },
                            {
                                "value": "2850",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T12:30:00.000-06:00",
                            },
                            {
                                "value": "2850",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T13:00:00.000-06:00",
                            },
                            {
                                "value": "2840",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T13:30:00.000-06:00",
                            },
                            {
                                "value": "2840",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T14:00:00.000-06:00",
                            },
                            {
                                "value": "2830",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T14:30:00.000-06:00",
                            },
                            {
                                "value": "2830",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T15:00:00.000-06:00",
                            },
                            {
                                "value": "2820",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T15:30:00.000-06:00",
                            },
                            {
                                "value": "2820",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T16:00:00.000-06:00",
                            },
                            {
                                "value": "2810",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T16:30:00.000-06:00",
                            },
                            {
                                "value": "2800",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T17:00:00.000-06:00",
                            },
                            {
                                "value": "2790",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T17:30:00.000-06:00",
                            },
                            {
                                "value": "2790",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T18:00:00.000-06:00",
                            },
                            {
                                "value": "2770",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T18:30:00.000-06:00",
                            },
                            {
                                "value": "2770",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T19:00:00.000-06:00",
                            },
                            {
                                "value": "2760",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T19:30:00.000-06:00",
                            },
                            {
                                "value": "2750",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T20:00:00.000-06:00",
                            },
                            {
                                "value": "2740",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T20:30:00.000-06:00",
                            },
                            {
                                "value": "2740",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T21:00:00.000-06:00",
                            },
                            {
                                "value": "2730",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T21:30:00.000-06:00",
                            },
                            {
                                "value": "2730",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T22:00:00.000-06:00",
                            },
                            {
                                "value": "2710",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T22:30:00.000-06:00",
                            },
                            {
                                "value": "2710",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T23:00:00.000-06:00",
                            },
                            {
                                "value": "2680",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T23:30:00.000-06:00",
                            },
                            {
                                "value": "2690",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T00:00:00.000-06:00",
                            },
                            {
                                "value": "2680",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T00:30:00.000-06:00",
                            },
                            {
                                "value": "2680",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T01:00:00.000-06:00",
                            },
                            {
                                "value": "2690",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T01:30:00.000-06:00",
                            },
                            {
                                "value": "2680",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T02:00:00.000-06:00",
                            },
                            {
                                "value": "2680",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T02:30:00.000-06:00",
                            },
                            {
                                "value": "2680",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T03:00:00.000-06:00",
                            },
                            {
                                "value": "2670",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T03:30:00.000-06:00",
                            },
                            {
                                "value": "2660",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T04:00:00.000-06:00",
                            },
                            {
                                "value": "2660",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T04:30:00.000-06:00",
                            },
                            {
                                "value": "2660",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T05:00:00.000-06:00",
                            },
                            {
                                "value": "2650",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T05:30:00.000-06:00",
                            },
                            {
                                "value": "2660",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T06:00:00.000-06:00",
                            },
                            {
                                "value": "2650",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T06:30:00.000-06:00",
                            },
                            {
                                "value": "2650",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T07:00:00.000-06:00",
                            },
                            {
                                "value": "2650",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T07:30:00.000-06:00",
                            },
                            {
                                "value": "2650",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T08:00:00.000-06:00",
                            },
                            {
                                "value": "2650",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T08:30:00.000-06:00",
                            },
                            {
                                "value": "2650",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T09:00:00.000-06:00",
                            },
                            {
                                "value": "2650",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T09:30:00.000-06:00",
                            },
                            {
                                "value": "2660",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T10:00:00.000-06:00",
                            },
                            {
                                "value": "2660",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T10:30:00.000-06:00",
                            },
                            {
                                "value": "2660",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T11:00:00.000-06:00",
                            },
                            {
                                "value": "2660",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T11:30:00.000-06:00",
                            },
                            {
                                "value": "2660",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T12:00:00.000-06:00",
                            },
                            {
                                "value": "2670",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T12:30:00.000-06:00",
                            },
                            {
                                "value": "2670",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T13:00:00.000-06:00",
                            },
                            {
                                "value": "2680",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T13:30:00.000-06:00",
                            },
                            {
                                "value": "2670",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T14:00:00.000-06:00",
                            },
                            {
                                "value": "2680",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T14:30:00.000-06:00",
                            },
                            {
                                "value": "2690",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T15:00:00.000-06:00",
                            },
                            {
                                "value": "2710",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T15:30:00.000-06:00",
                            },
                            {
                                "value": "2710",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T16:00:00.000-06:00",
                            },
                            {
                                "value": "2720",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T16:30:00.000-06:00",
                            },
                            {
                                "value": "2730",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T17:00:00.000-06:00",
                            },
                            {
                                "value": "2730",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T17:30:00.000-06:00",
                            },
                            {
                                "value": "2740",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T18:00:00.000-06:00",
                            },
                            {
                                "value": "2760",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T18:30:00.000-06:00",
                            },
                            {
                                "value": "2760",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T19:00:00.000-06:00",
                            },
                            {
                                "value": "2770",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T19:30:00.000-06:00",
                            },
                            {
                                "value": "2780",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T20:00:00.000-06:00",
                            },
                            {
                                "value": "2780",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T20:30:00.000-06:00",
                            },
                            {
                                "value": "2800",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T21:00:00.000-06:00",
                            },
                            {
                                "value": "2820",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T21:30:00.000-06:00",
                            },
                            {
                                "value": "2820",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T22:00:00.000-06:00",
                            },
                            {
                                "value": "2840",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T22:30:00.000-06:00",
                            },
                            {
                                "value": "2850",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T23:00:00.000-06:00",
                            },
                            {
                                "value": "2860",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T23:30:00.000-06:00",
                            },
                        ],
                        "qualifier": [
                            {
                                "qualifierCode": "P",
                                "qualifierDescription": "Provisional data subject to revision.",
                                "qualifierID": 0,
                                "network": "NWIS",
                                "vocabulary": "uv_rmk_cd",
                            }
                        ],
                        "qualityControlLevel": [],
                        "method": [{"methodDescription": "", "methodID": 62174}],
                        "source": [],
                        "offset": [],
                        "sample": [],
                        "censorCode": [],
                    }
                ],
                "name": "USGS:02492000:00060:00000",
            },
            {
                "sourceInfo": {
                    "siteName": "Bogue Chitto River near Bush, LA",
                    "siteCode": [
                        {"value": "02492000", "network": "NWIS", "agencyCode": "USGS"}
                    ],
                    "timeZoneInfo": {
                        "defaultTimeZone": {
                            "zoneOffset": "-06:00",
                            "zoneAbbreviation": "CST",
                        },
                        "daylightSavingsTimeZone": {
                            "zoneOffset": "-05:00",
                            "zoneAbbreviation": "CDT",
                        },
                        "siteUsesDaylightSavingsTime": True,
                    },
                    "geoLocation": {
                        "geogLocation": {
                            "srs": "EPSG:4326",
                            "latitude": 30.62935636,
                            "longitude": -89.8972956,
                        },
                        "localSiteXY": [],
                    },
                    "note": [],
                    "siteType": [],
                    "siteProperty": [
                        {"value": "ST", "name": "siteTypeCd"},
                        {"value": "03180005", "name": "hucCd"},
                        {"value": "22", "name": "stateCd"},
                        {"value": "22103", "name": "countyCd"},
                    ],
                },
                "variable": {
                    "variableCode": [
                        {
                            "value": "00065",
                            "network": "NWIS",
                            "vocabulary": "NWIS:UnitValues",
                            "variableID": 45807202,
                            "default": True,
                        }
                    ],
                    "variableName": "Gage height, ft",
                    "variableDescription": "Gage height, feet",
                    "valueType": "Derived Value",
                    "unit": {"unitCode": "ft"},
                    "options": {
                        "option": [{"name": "Statistic", "optionCode": "00000"}]
                    },
                    "note": [],
                    "noDataValue": -999999.0,
                    "variableProperty": [],
                    "oid": "45807202",
                },
                "values": [
                    {
                        "value": [
                            {
                                "value": "10.47",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T00:00:00.000-06:00",
                            },
                            {
                                "value": "10.47",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T00:30:00.000-06:00",
                            },
                            {
                                "value": "10.47",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T01:00:00.000-06:00",
                            },
                            {
                                "value": "10.47",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T01:30:00.000-06:00",
                            },
                            {
                                "value": "10.46",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T02:00:00.000-06:00",
                            },
                            {
                                "value": "10.46",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T02:30:00.000-06:00",
                            },
                            {
                                "value": "10.46",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T03:00:00.000-06:00",
                            },
                            {
                                "value": "10.45",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T03:30:00.000-06:00",
                            },
                            {
                                "value": "10.44",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T04:00:00.000-06:00",
                            },
                            {
                                "value": "10.44",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T04:30:00.000-06:00",
                            },
                            {
                                "value": "10.43",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T05:00:00.000-06:00",
                            },
                            {
                                "value": "10.42",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T05:30:00.000-06:00",
                            },
                            {
                                "value": "10.43",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T06:00:00.000-06:00",
                            },
                            {
                                "value": "10.41",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T06:30:00.000-06:00",
                            },
                            {
                                "value": "10.40",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T07:00:00.000-06:00",
                            },
                            {
                                "value": "10.38",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T07:30:00.000-06:00",
                            },
                            {
                                "value": "10.38",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T08:00:00.000-06:00",
                            },
                            {
                                "value": "10.37",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T08:30:00.000-06:00",
                            },
                            {
                                "value": "10.36",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T09:00:00.000-06:00",
                            },
                            {
                                "value": "10.35",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T09:30:00.000-06:00",
                            },
                            {
                                "value": "10.33",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T10:00:00.000-06:00",
                            },
                            {
                                "value": "10.33",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T10:30:00.000-06:00",
                            },
                            {
                                "value": "10.33",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T11:00:00.000-06:00",
                            },
                            {
                                "value": "10.30",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T11:30:00.000-06:00",
                            },
                            {
                                "value": "10.30",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T12:00:00.000-06:00",
                            },
                            {
                                "value": "10.28",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T12:30:00.000-06:00",
                            },
                            {
                                "value": "10.28",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T13:00:00.000-06:00",
                            },
                            {
                                "value": "10.24",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T13:30:00.000-06:00",
                            },
                            {
                                "value": "10.25",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T14:00:00.000-06:00",
                            },
                            {
                                "value": "10.22",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T14:30:00.000-06:00",
                            },
                            {
                                "value": "10.21",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T15:00:00.000-06:00",
                            },
                            {
                                "value": "10.19",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T15:30:00.000-06:00",
                            },
                            {
                                "value": "10.18",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T16:00:00.000-06:00",
                            },
                            {
                                "value": "10.15",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T16:30:00.000-06:00",
                            },
                            {
                                "value": "10.15",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T17:00:00.000-06:00",
                            },
                            {
                                "value": "10.11",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T17:30:00.000-06:00",
                            },
                            {
                                "value": "10.10",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T18:00:00.000-06:00",
                            },
                            {
                                "value": "10.08",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T18:30:00.000-06:00",
                            },
                            {
                                "value": "10.06",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T19:00:00.000-06:00",
                            },
                            {
                                "value": "10.03",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T19:30:00.000-06:00",
                            },
                            {
                                "value": "10.02",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T20:00:00.000-06:00",
                            },
                            {
                                "value": "9.98",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T20:30:00.000-06:00",
                            },
                            {
                                "value": "9.97",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T21:00:00.000-06:00",
                            },
                            {
                                "value": "9.93",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T21:30:00.000-06:00",
                            },
                            {
                                "value": "9.92",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T22:00:00.000-06:00",
                            },
                            {
                                "value": "9.89",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T22:30:00.000-06:00",
                            },
                            {
                                "value": "9.88",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T23:00:00.000-06:00",
                            },
                            {
                                "value": "9.84",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-25T23:30:00.000-06:00",
                            },
                            {
                                "value": "9.83",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T00:00:00.000-06:00",
                            },
                            {
                                "value": "9.79",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T00:30:00.000-06:00",
                            },
                            {
                                "value": "9.77",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T01:00:00.000-06:00",
                            },
                            {
                                "value": "9.73",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T01:30:00.000-06:00",
                            },
                            {
                                "value": "9.72",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T02:00:00.000-06:00",
                            },
                            {
                                "value": "9.68",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T02:30:00.000-06:00",
                            },
                            {
                                "value": "9.66",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T03:00:00.000-06:00",
                            },
                            {
                                "value": "9.62",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T03:30:00.000-06:00",
                            },
                            {
                                "value": "9.60",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T04:00:00.000-06:00",
                            },
                            {
                                "value": "9.56",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T04:30:00.000-06:00",
                            },
                            {
                                "value": "9.55",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T05:00:00.000-06:00",
                            },
                            {
                                "value": "9.50",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T05:30:00.000-06:00",
                            },
                            {
                                "value": "9.48",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T06:00:00.000-06:00",
                            },
                            {
                                "value": "9.44",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T06:30:00.000-06:00",
                            },
                            {
                                "value": "9.42",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T07:00:00.000-06:00",
                            },
                            {
                                "value": "9.38",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T07:30:00.000-06:00",
                            },
                            {
                                "value": "9.36",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T08:00:00.000-06:00",
                            },
                            {
                                "value": "9.31",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T08:30:00.000-06:00",
                            },
                            {
                                "value": "9.27",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T09:00:00.000-06:00",
                            },
                            {
                                "value": "9.24",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T09:30:00.000-06:00",
                            },
                            {
                                "value": "9.23",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T10:00:00.000-06:00",
                            },
                            {
                                "value": "9.18",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T10:30:00.000-06:00",
                            },
                            {
                                "value": "9.16",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T11:00:00.000-06:00",
                            },
                            {
                                "value": "9.11",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T11:30:00.000-06:00",
                            },
                            {
                                "value": "9.10",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T12:00:00.000-06:00",
                            },
                            {
                                "value": "9.05",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T12:30:00.000-06:00",
                            },
                            {
                                "value": "9.04",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T13:00:00.000-06:00",
                            },
                            {
                                "value": "8.99",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T13:30:00.000-06:00",
                            },
                            {
                                "value": "8.97",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T14:00:00.000-06:00",
                            },
                            {
                                "value": "8.93",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T14:30:00.000-06:00",
                            },
                            {
                                "value": "8.90",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T15:00:00.000-06:00",
                            },
                            {
                                "value": "8.86",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T15:30:00.000-06:00",
                            },
                            {
                                "value": "8.85",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T16:00:00.000-06:00",
                            },
                            {
                                "value": "8.80",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T16:30:00.000-06:00",
                            },
                            {
                                "value": "8.79",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T17:00:00.000-06:00",
                            },
                            {
                                "value": "8.74",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T17:30:00.000-06:00",
                            },
                            {
                                "value": "8.72",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T18:00:00.000-06:00",
                            },
                            {
                                "value": "8.67",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T18:30:00.000-06:00",
                            },
                            {
                                "value": "8.66",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T19:00:00.000-06:00",
                            },
                            {
                                "value": "8.61",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T19:30:00.000-06:00",
                            },
                            {
                                "value": "8.60",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T20:00:00.000-06:00",
                            },
                            {
                                "value": "8.55",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T20:30:00.000-06:00",
                            },
                            {
                                "value": "8.53",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T21:00:00.000-06:00",
                            },
                            {
                                "value": "8.49",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T21:30:00.000-06:00",
                            },
                            {
                                "value": "8.47",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T22:00:00.000-06:00",
                            },
                            {
                                "value": "8.42",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T22:30:00.000-06:00",
                            },
                            {
                                "value": "8.41",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T23:00:00.000-06:00",
                            },
                            {
                                "value": "8.37",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-26T23:30:00.000-06:00",
                            },
                            {
                                "value": "8.32",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T00:00:00.000-06:00",
                            },
                            {
                                "value": "8.29",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T00:30:00.000-06:00",
                            },
                            {
                                "value": "8.29",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T01:00:00.000-06:00",
                            },
                            {
                                "value": "8.28",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T01:30:00.000-06:00",
                            },
                            {
                                "value": "8.27",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T02:00:00.000-06:00",
                            },
                            {
                                "value": "8.26",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T02:30:00.000-06:00",
                            },
                            {
                                "value": "8.24",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T03:00:00.000-06:00",
                            },
                            {
                                "value": "8.23",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T03:30:00.000-06:00",
                            },
                            {
                                "value": "8.22",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T04:00:00.000-06:00",
                            },
                            {
                                "value": "8.20",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T04:30:00.000-06:00",
                            },
                            {
                                "value": "8.18",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T05:00:00.000-06:00",
                            },
                            {
                                "value": "8.15",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T05:30:00.000-06:00",
                            },
                            {
                                "value": "8.14",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T06:00:00.000-06:00",
                            },
                            {
                                "value": "8.11",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T06:30:00.000-06:00",
                            },
                            {
                                "value": "8.10",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T07:00:00.000-06:00",
                            },
                            {
                                "value": "8.06",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T07:30:00.000-06:00",
                            },
                            {
                                "value": "8.06",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T08:00:00.000-06:00",
                            },
                            {
                                "value": "8.02",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T08:30:00.000-06:00",
                            },
                            {
                                "value": "8.02",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T09:00:00.000-06:00",
                            },
                            {
                                "value": "7.99",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T09:30:00.000-06:00",
                            },
                            {
                                "value": "7.97",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T10:00:00.000-06:00",
                            },
                            {
                                "value": "7.95",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T10:30:00.000-06:00",
                            },
                            {
                                "value": "7.94",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T11:00:00.000-06:00",
                            },
                            {
                                "value": "7.92",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T11:30:00.000-06:00",
                            },
                            {
                                "value": "7.91",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T12:00:00.000-06:00",
                            },
                            {
                                "value": "7.88",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T12:30:00.000-06:00",
                            },
                            {
                                "value": "7.87",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T13:00:00.000-06:00",
                            },
                            {
                                "value": "7.87",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T13:30:00.000-06:00",
                            },
                            {
                                "value": "7.87",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T14:00:00.000-06:00",
                            },
                            {
                                "value": "7.84",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T14:30:00.000-06:00",
                            },
                            {
                                "value": "7.84",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T15:00:00.000-06:00",
                            },
                            {
                                "value": "7.82",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T15:30:00.000-06:00",
                            },
                            {
                                "value": "7.81",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T16:00:00.000-06:00",
                            },
                            {
                                "value": "7.80",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T16:30:00.000-06:00",
                            },
                            {
                                "value": "7.79",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T17:00:00.000-06:00",
                            },
                            {
                                "value": "7.78",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T17:30:00.000-06:00",
                            },
                            {
                                "value": "7.76",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T18:00:00.000-06:00",
                            },
                            {
                                "value": "7.77",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T18:30:00.000-06:00",
                            },
                            {
                                "value": "7.76",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T19:00:00.000-06:00",
                            },
                            {
                                "value": "7.75",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T19:30:00.000-06:00",
                            },
                            {
                                "value": "7.75",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T20:00:00.000-06:00",
                            },
                            {
                                "value": "7.73",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T20:30:00.000-06:00",
                            },
                            {
                                "value": "7.73",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T21:00:00.000-06:00",
                            },
                            {
                                "value": "7.72",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T21:30:00.000-06:00",
                            },
                            {
                                "value": "7.72",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T22:00:00.000-06:00",
                            },
                            {
                                "value": "7.71",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T22:30:00.000-06:00",
                            },
                            {
                                "value": "7.71",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T23:00:00.000-06:00",
                            },
                            {
                                "value": "7.70",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-27T23:30:00.000-06:00",
                            },
                            {
                                "value": "7.70",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T00:00:00.000-06:00",
                            },
                            {
                                "value": "7.69",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T00:30:00.000-06:00",
                            },
                            {
                                "value": "7.70",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T01:00:00.000-06:00",
                            },
                            {
                                "value": "7.69",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T01:30:00.000-06:00",
                            },
                            {
                                "value": "7.69",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T02:00:00.000-06:00",
                            },
                            {
                                "value": "7.69",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T02:30:00.000-06:00",
                            },
                            {
                                "value": "7.69",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T03:00:00.000-06:00",
                            },
                            {
                                "value": "7.69",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T03:30:00.000-06:00",
                            },
                            {
                                "value": "7.69",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T04:00:00.000-06:00",
                            },
                            {
                                "value": "7.69",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T04:30:00.000-06:00",
                            },
                            {
                                "value": "7.69",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T05:00:00.000-06:00",
                            },
                            {
                                "value": "7.69",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T05:30:00.000-06:00",
                            },
                            {
                                "value": "7.69",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T06:00:00.000-06:00",
                            },
                            {
                                "value": "7.69",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T06:30:00.000-06:00",
                            },
                            {
                                "value": "7.69",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T07:00:00.000-06:00",
                            },
                            {
                                "value": "7.69",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T07:30:00.000-06:00",
                            },
                            {
                                "value": "7.69",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T08:00:00.000-06:00",
                            },
                            {
                                "value": "7.68",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T08:30:00.000-06:00",
                            },
                            {
                                "value": "7.68",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T09:00:00.000-06:00",
                            },
                            {
                                "value": "7.68",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T09:30:00.000-06:00",
                            },
                            {
                                "value": "7.67",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T10:00:00.000-06:00",
                            },
                            {
                                "value": "7.67",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T10:30:00.000-06:00",
                            },
                            {
                                "value": "7.67",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T11:00:00.000-06:00",
                            },
                            {
                                "value": "7.67",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T11:30:00.000-06:00",
                            },
                            {
                                "value": "7.66",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T12:00:00.000-06:00",
                            },
                            {
                                "value": "7.64",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T12:30:00.000-06:00",
                            },
                            {
                                "value": "7.64",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T13:00:00.000-06:00",
                            },
                            {
                                "value": "7.63",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T13:30:00.000-06:00",
                            },
                            {
                                "value": "7.63",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T14:00:00.000-06:00",
                            },
                            {
                                "value": "7.62",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T14:30:00.000-06:00",
                            },
                            {
                                "value": "7.62",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T15:00:00.000-06:00",
                            },
                            {
                                "value": "7.60",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T15:30:00.000-06:00",
                            },
                            {
                                "value": "7.60",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T16:00:00.000-06:00",
                            },
                            {
                                "value": "7.58",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T16:30:00.000-06:00",
                            },
                            {
                                "value": "7.57",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T17:00:00.000-06:00",
                            },
                            {
                                "value": "7.56",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T17:30:00.000-06:00",
                            },
                            {
                                "value": "7.55",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T18:00:00.000-06:00",
                            },
                            {
                                "value": "7.53",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T18:30:00.000-06:00",
                            },
                            {
                                "value": "7.53",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T19:00:00.000-06:00",
                            },
                            {
                                "value": "7.51",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T19:30:00.000-06:00",
                            },
                            {
                                "value": "7.50",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T20:00:00.000-06:00",
                            },
                            {
                                "value": "7.48",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T20:30:00.000-06:00",
                            },
                            {
                                "value": "7.48",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T21:00:00.000-06:00",
                            },
                            {
                                "value": "7.47",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T21:30:00.000-06:00",
                            },
                            {
                                "value": "7.46",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T22:00:00.000-06:00",
                            },
                            {
                                "value": "7.43",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T22:30:00.000-06:00",
                            },
                            {
                                "value": "7.44",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T23:00:00.000-06:00",
                            },
                            {
                                "value": "7.39",
                                "qualifiers": ["P"],
                                "dateTime": "2019-02-28T23:30:00.000-06:00",
                            },
                            {
                                "value": "7.40",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T00:00:00.000-06:00",
                            },
                            {
                                "value": "7.39",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T00:30:00.000-06:00",
                            },
                            {
                                "value": "7.39",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T01:00:00.000-06:00",
                            },
                            {
                                "value": "7.40",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T01:30:00.000-06:00",
                            },
                            {
                                "value": "7.39",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T02:00:00.000-06:00",
                            },
                            {
                                "value": "7.38",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T02:30:00.000-06:00",
                            },
                            {
                                "value": "7.38",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T03:00:00.000-06:00",
                            },
                            {
                                "value": "7.37",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T03:30:00.000-06:00",
                            },
                            {
                                "value": "7.36",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T04:00:00.000-06:00",
                            },
                            {
                                "value": "7.36",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T04:30:00.000-06:00",
                            },
                            {
                                "value": "7.35",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T05:00:00.000-06:00",
                            },
                            {
                                "value": "7.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T05:30:00.000-06:00",
                            },
                            {
                                "value": "7.35",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T06:00:00.000-06:00",
                            },
                            {
                                "value": "7.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T06:30:00.000-06:00",
                            },
                            {
                                "value": "7.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T07:00:00.000-06:00",
                            },
                            {
                                "value": "7.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T07:30:00.000-06:00",
                            },
                            {
                                "value": "7.33",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T08:00:00.000-06:00",
                            },
                            {
                                "value": "7.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T08:30:00.000-06:00",
                            },
                            {
                                "value": "7.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T09:00:00.000-06:00",
                            },
                            {
                                "value": "7.34",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T09:30:00.000-06:00",
                            },
                            {
                                "value": "7.35",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T10:00:00.000-06:00",
                            },
                            {
                                "value": "7.35",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T10:30:00.000-06:00",
                            },
                            {
                                "value": "7.35",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T11:00:00.000-06:00",
                            },
                            {
                                "value": "7.36",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T11:30:00.000-06:00",
                            },
                            {
                                "value": "7.36",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T12:00:00.000-06:00",
                            },
                            {
                                "value": "7.37",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T12:30:00.000-06:00",
                            },
                            {
                                "value": "7.37",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T13:00:00.000-06:00",
                            },
                            {
                                "value": "7.38",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T13:30:00.000-06:00",
                            },
                            {
                                "value": "7.37",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T14:00:00.000-06:00",
                            },
                            {
                                "value": "7.39",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T14:30:00.000-06:00",
                            },
                            {
                                "value": "7.40",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T15:00:00.000-06:00",
                            },
                            {
                                "value": "7.43",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T15:30:00.000-06:00",
                            },
                            {
                                "value": "7.44",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T16:00:00.000-06:00",
                            },
                            {
                                "value": "7.45",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T16:30:00.000-06:00",
                            },
                            {
                                "value": "7.46",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T17:00:00.000-06:00",
                            },
                            {
                                "value": "7.47",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T17:30:00.000-06:00",
                            },
                            {
                                "value": "7.48",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T18:00:00.000-06:00",
                            },
                            {
                                "value": "7.51",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T18:30:00.000-06:00",
                            },
                            {
                                "value": "7.51",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T19:00:00.000-06:00",
                            },
                            {
                                "value": "7.53",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T19:30:00.000-06:00",
                            },
                            {
                                "value": "7.54",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T20:00:00.000-06:00",
                            },
                            {
                                "value": "7.54",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T20:30:00.000-06:00",
                            },
                            {
                                "value": "7.57",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T21:00:00.000-06:00",
                            },
                            {
                                "value": "7.60",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T21:30:00.000-06:00",
                            },
                            {
                                "value": "7.60",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T22:00:00.000-06:00",
                            },
                            {
                                "value": "7.63",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T22:30:00.000-06:00",
                            },
                            {
                                "value": "7.64",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T23:00:00.000-06:00",
                            },
                            {
                                "value": "7.66",
                                "qualifiers": ["P"],
                                "dateTime": "2019-03-01T23:30:00.000-06:00",
                            },
                        ],
                        "qualifier": [
                            {
                                "qualifierCode": "P",
                                "qualifierDescription": "Provisional data subject to revision.",
                                "qualifierID": 0,
                                "network": "NWIS",
                                "vocabulary": "uv_rmk_cd",
                            }
                        ],
                        "qualityControlLevel": [],
                        "method": [{"methodDescription": "", "methodID": 62175}],
                        "source": [],
                        "offset": [],
                        "sample": [],
                        "censorCode": [],
                    }
                ],
                "name": "USGS:02492000:00065:00000",
            },
        ],
    },
    "nil": False,
    "globalScope": True,
    "typeSubstituted": False,
}
