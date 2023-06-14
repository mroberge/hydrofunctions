"""
fixtures_daily_dupe.py

This file contains JSON from the NWIS

This json is from a site that has a duplicated record.
Also, it has an interesting flag, "Dis", for discontinued.
hf.NWIS('03107698', "dv", '2017-04-23', '2017-04-29')
"""

daily_dupe = {
    "name": "ns1:timeSeriesResponseType",
    "declaredType": "org.cuahsi.waterml.TimeSeriesResponseType",
    "scope": "javax.xml.bind.JAXBElement$GlobalScope",
    "value": {
        "queryInfo": {
            "queryURL": "http://waterservices.usgs.gov/nwis/dv/format=json%2C1.1&sites=03107698&startDT=2017-04-23&endDT=2017-04-29",
            "criteria": {
                "locationParam": "[ALL:03107698]",
                "variableParam": "ALL",
                "timeParam": {
                    "beginDateTime": "2017-04-23T00:00:00.000",
                    "endDateTime": "2017-04-29T00:00:00.000",
                },
                "parameter": [],
            },
            "note": [
                {"value": "[ALL:03107698]", "title": "filter:sites"},
                {
                    "value": "[mode=RANGE, modifiedSince=null] interval={INTERVAL[2017-04-23T00:00:00.000-04:00/2017-04-29T00:00:00.000-04:00]}",
                    "title": "filter:timeRange",
                },
                {"value": "methodIds=[ALL]", "title": "filter:methodId"},
                {"value": "2019-03-20T18:19:45.800Z", "title": "requestDT"},
                {"value": "bd536170-4b3c-11e9-9463-6cae8b6642f6", "title": "requestId"},
                {
                    "value": "Provisional data are subject to revision. Go to http://waterdata.usgs.gov/nwis/help/?provisional for more information.",
                    "title": "disclaimer",
                },
                {"value": "caas01", "title": "server"},
            ],
        },
        "timeSeries": [
            {
                "sourceInfo": {
                    "siteName": "Traverse Creek near Kendall, PA",
                    "siteCode": [
                        {"value": "03107698", "network": "NWIS", "agencyCode": "USGS"}
                    ],
                    "timeZoneInfo": {
                        "defaultTimeZone": {
                            "zoneOffset": "-05:00",
                            "zoneAbbreviation": "EST",
                        },
                        "daylightSavingsTimeZone": {
                            "zoneOffset": "-04:00",
                            "zoneAbbreviation": "EDT",
                        },
                        "siteUsesDaylightSavingsTime": True,
                    },
                    "geoLocation": {
                        "geogLocation": {
                            "srs": "EPSG:4326",
                            "latitude": 40.5261111,
                            "longitude": -80.45138889,
                        },
                        "localSiteXY": [],
                    },
                    "note": [],
                    "siteType": [],
                    "siteProperty": [
                        {"value": "ST", "name": "siteTypeCd"},
                        {"value": "05030101", "name": "hucCd"},
                        {"value": "42", "name": "stateCd"},
                        {"value": "42007", "name": "countyCd"},
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
                        "option": [
                            {
                                "value": "Mean",
                                "name": "Statistic",
                                "optionCode": "00003",
                            }
                        ]
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
                                "value": "6.82",
                                "qualifiers": ["A"],
                                "dateTime": "2017-04-23T00:00:00.000",
                            },
                            {
                                "value": "6.04",
                                "qualifiers": ["A"],
                                "dateTime": "2017-04-24T00:00:00.000",
                            },
                            {
                                "value": "5.62",
                                "qualifiers": ["A"],
                                "dateTime": "2017-04-25T00:00:00.000",
                            },
                            {
                                "value": "-999999",
                                "qualifiers": ["P", "Dis"],
                                "dateTime": "2017-04-26T00:00:00.000",
                            },
                            {
                                "value": "-999999",
                                "qualifiers": ["P", "Dis"],
                                "dateTime": "2017-04-26T00:00:00.000",
                            },
                            {
                                "value": "-999999",
                                "qualifiers": ["P", "Dis"],
                                "dateTime": "2017-04-27T00:00:00.000",
                            },
                            {
                                "value": "-999999",
                                "qualifiers": ["P", "Dis"],
                                "dateTime": "2017-04-28T00:00:00.000",
                            },
                            {
                                "value": "-999999",
                                "qualifiers": ["P", "Dis"],
                                "dateTime": "2017-04-29T00:00:00.000",
                            },
                        ],
                        "qualifier": [
                            {
                                "qualifierCode": "Dis",
                                "qualifierDescription": "Record has been discontinued at the measurement site.",
                                "qualifierID": 0,
                                "network": "NWIS",
                                "vocabulary": "uv_rmk_cd",
                            },
                            {
                                "qualifierCode": "A",
                                "qualifierDescription": "Approved for publication -- Processing and review completed.",
                                "qualifierID": 1,
                                "network": "NWIS",
                                "vocabulary": "uv_rmk_cd",
                            },
                            {
                                "qualifierCode": "P",
                                "qualifierDescription": "Provisional data subject to revision.",
                                "qualifierID": 2,
                                "network": "NWIS",
                                "vocabulary": "uv_rmk_cd",
                            },
                        ],
                        "qualityControlLevel": [],
                        "method": [{"methodDescription": "", "methodID": 120332}],
                        "source": [],
                        "offset": [],
                        "sample": [],
                        "censorCode": [],
                    }
                ],
                "name": "USGS:03107698:00060:00003",
            }
        ],
    },
    "nil": False,
    "globalScope": True,
    "typeSubstituted": False,
}

# What happens if a scientist replaces an empty record with new
# estimated data, and forgets to discard the old data?
# This fixture simulates a substituted record that has been marked with 'e'
# in the qualifier tags. An entry has also been made in the qualifierCode
# list, but I had to fake that.
daily_dupe_altered = {
    "name": "ns1:timeSeriesResponseType",
    "declaredType": "org.cuahsi.waterml.TimeSeriesResponseType",
    "scope": "javax.xml.bind.JAXBElement$GlobalScope",
    "value": {
        "queryInfo": {
            "queryURL": "http://waterservices.usgs.gov/nwis/dv/format=json%2C1.1&sites=03107698&startDT=2017-04-23&endDT=2017-04-29",
            "criteria": {
                "locationParam": "[ALL:03107698]",
                "variableParam": "ALL",
                "timeParam": {
                    "beginDateTime": "2017-04-23T00:00:00.000",
                    "endDateTime": "2017-04-29T00:00:00.000",
                },
                "parameter": [],
            },
            "note": [
                {"value": "[ALL:03107698]", "title": "filter:sites"},
                {
                    "value": "[mode=RANGE, modifiedSince=null] interval={INTERVAL[2017-04-23T00:00:00.000-04:00/2017-04-29T00:00:00.000-04:00]}",
                    "title": "filter:timeRange",
                },
                {"value": "methodIds=[ALL]", "title": "filter:methodId"},
                {"value": "2019-03-20T18:19:45.800Z", "title": "requestDT"},
                {"value": "bd536170-4b3c-11e9-9463-6cae8b6642f6", "title": "requestId"},
                {
                    "value": "Provisional data are subject to revision. Go to http://waterdata.usgs.gov/nwis/help/?provisional for more information.",
                    "title": "disclaimer",
                },
                {"value": "caas01", "title": "server"},
            ],
        },
        "timeSeries": [
            {
                "sourceInfo": {
                    "siteName": "Traverse Creek near Kendall, PA",
                    "siteCode": [
                        {"value": "03107698", "network": "NWIS", "agencyCode": "USGS"}
                    ],
                    "timeZoneInfo": {
                        "defaultTimeZone": {
                            "zoneOffset": "-05:00",
                            "zoneAbbreviation": "EST",
                        },
                        "daylightSavingsTimeZone": {
                            "zoneOffset": "-04:00",
                            "zoneAbbreviation": "EDT",
                        },
                        "siteUsesDaylightSavingsTime": True,
                    },
                    "geoLocation": {
                        "geogLocation": {
                            "srs": "EPSG:4326",
                            "latitude": 40.5261111,
                            "longitude": -80.45138889,
                        },
                        "localSiteXY": [],
                    },
                    "note": [],
                    "siteType": [],
                    "siteProperty": [
                        {"value": "ST", "name": "siteTypeCd"},
                        {"value": "05030101", "name": "hucCd"},
                        {"value": "42", "name": "stateCd"},
                        {"value": "42007", "name": "countyCd"},
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
                        "option": [
                            {
                                "value": "Mean",
                                "name": "Statistic",
                                "optionCode": "00003",
                            }
                        ]
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
                                "value": "6.82",
                                "qualifiers": ["A"],
                                "dateTime": "2017-04-23T00:00:00.000",
                            },
                            {
                                "value": "6.04",
                                "qualifiers": ["A"],
                                "dateTime": "2017-04-24T00:00:00.000",
                            },
                            {
                                "value": "5.62",
                                "qualifiers": ["A"],
                                "dateTime": "2017-04-25T00:00:00.000",
                            },
                            {
                                "value": "-999999",
                                "qualifiers": ["P", "Dis"],
                                "dateTime": "2017-04-26T00:00:00.000",
                            },
                            {
                                "value": "-999999",
                                "qualifiers": ["P", "Dis"],
                                "dateTime": "2017-04-26T00:00:00.000",
                            },
                            {
                                "value": "01234",
                                "qualifiers": ["P", "e"],
                                "dateTime": "2017-04-27T00:00:00.000",
                            },
                            {
                                "value": "-999999",
                                "qualifiers": ["P", "Dis"],
                                "dateTime": "2017-04-28T00:00:00.000",
                            },
                            {
                                "value": "-999999",
                                "qualifiers": ["P", "Dis"],
                                "dateTime": "2017-04-29T00:00:00.000",
                            },
                        ],
                        "qualifier": [
                            {
                                "qualifierCode": "Dis",
                                "qualifierDescription": "Record has been discontinued at the measurement site.",
                                "qualifierID": 0,
                                "network": "NWIS",
                                "vocabulary": "uv_rmk_cd",
                            },
                            {
                                "qualifierCode": "A",
                                "qualifierDescription": "Approved for publication -- Processing and review completed.",
                                "qualifierID": 1,
                                "network": "NWIS",
                                "vocabulary": "uv_rmk_cd",
                            },
                            {
                                "qualifierCode": "P",
                                "qualifierDescription": "Provisional data subject to revision.",
                                "qualifierID": 2,
                                "network": "NWIS",
                                "vocabulary": "uv_rmk_cd",
                            },
                            {
                                "qualifierCode": "e",
                                "qualifierDescription": "Estimated value.",
                                "qualifierID": 3,
                                "network": "NWIS",
                                "vocabulary": "uv_rmk_cd",
                            },
                        ],
                        "qualityControlLevel": [],
                        "method": [{"methodDescription": "", "methodID": 120332}],
                        "source": [],
                        "offset": [],
                        "sample": [],
                        "censorCode": [],
                    }
                ],
                "name": "USGS:03107698:00060:00003",
            }
        ],
    },
    "nil": False,
    "globalScope": True,
    "typeSubstituted": False,
}
