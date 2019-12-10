# -*- coding: utf-8 -*-
"""
hydrofunctions.nldi
~~~~~~~~~~~~~~~~~~~

This module holds functions that use the USGS Hydro Network-Linked Data Index.

The Hydro Network-Linked Data Index (NLDI) is a web service that utilizes the
National Hydrolography Dataset (NHD). The NHD, NHDplus V2, and the NHDplus High
Resolution are all spatial datasets that combine collections of points (stream
gauge locations, watershed outlets), lines (stream channels, canals), and
polygons (ponds, watersheds). The various forms of the NHD are usually
available only in formats for use in desktop GIS programs, like ArcMap. The
NLDI is a web service that makes some of the materials available in the NHD as
an online webservice.

For more information on the NLDI, visit:
    - NLDI blog post: https://owi.usgs.gov/blog/nldi-intro/
    - a second source: https://waterdata.usgs.gov/blog/nldi-intro/
    - a demo page: https://cida.usgs.gov/nldi/swagger-ui.html#!/lookup-controller/getRegisteredFeatureUsingGET

The NLDI can return all of the gauges upstream and downstream from a gauge, a
geojson file of the US & DS channel, and the watershed boundary.

"""
