# -*- coding: utf-8 -*-
"""
fixtures_usgs_rdb.py

This file contains the following test fixtures:
    - field_fixture: a sample rdb file containing field measurements.
        - Header contains four 'messages'
        - dtypes contains one date column
        - 32 columns, 9 data rows (shortened from original)

    - rating_fixture: a sample rdb file containing an 'expanded shift-adjusted'
        rating curve.
        - Header has extra // marks to start every line. ???
        - Header has many different parameters embedded.
        - Two warning messages are in the header
        - 4 columns, 9 data rows (shortened from original)

    - peaks_fixture: a sample rdb file containing annual peak discharge data.
        - Header contains many 'messages', including two tables.
        - dtypes contain two date columns.
        13 columns, 18 data rows.
"""


# shortened response from this URL: https://waterdata.usgs.gov/pa/nwis/measurements?site_no=01541200&agency_cd=USGS&format=rdb_expanded
field_fixture = """#
# U.S. Geological Survey, National Water Information System
# Surface water measurements
#
# Retrieved: 2019-03-04 10:15:59 EST     (sdww01)
#
# Further descriptions of the columns and codes used can be found at:
# https://help.waterdata.usgs.gov/output-formats#streamflow_measurement_data
#
# Data for the following 1 site(s) are contained in this file
#  USGS 01541200 WB Susquehanna River near Curwensville, PA
# -----------------------------------------------------------------------------------
#
#
agency_cd	site_no	measurement_nu	measurement_dt	tz_cd	q_meas_used_fg	party_nm	site_visit_coll_agency_cd	gage_height_va	discharge_va	measured_rating_diff	gage_va_change	gage_va_time	control_type_cd	discharge_cd	chan_nu	chan_name	meas_type	streamflow_method	velocity_method	chan_discharge	chan_width	chan_area	chan_velocity	chan_stability	chan_material	chan_evenness	long_vel_desc	horz_vel_desc	vert_vel_desc	chan_loc_cd	chan_loc_dist
5s	15s	6s	19d	12s	1s	12s	5s	12s	12s	12s	7s	6s	21s	15s	11n	64s	4s	5s	5s	14s	14s	14s	14s	4s	4s	4s	12s	9s	12s	7s	14s
USGS	01541200	1	1955-09-29		Yes	EVA	USGS	3.66	299	Good	-0.02	0.80	Clear	MEAS	1	Imported Channel 1	UNSP	other		299				UNSP	UNSP	UNSP	unkn	UNSP	UNSP	UNSP
USGS	01541200	2	1955-10-10		Yes	SNA	USGS	3.46	202	Good	0.00	1.00	Clear	MEAS	1	Imported Channel 1	UNSP	other		202				UNSP	UNSP	UNSP	unkn	UNSP	UNSP	UNSP
USGS	01541200	3	1955-11-17		Yes	GAR	USGS	6.77	3490	Good	-0.17	1.30	Clear	MEAS	1	Imported Channel 1	UNSP	other		3490				UNSP	UNSP	UNSP	unkn	UNSP	UNSP	UNSP
USGS	01541200	4	1955-12-18		Yes	YEH	USGS	3.64	193	Unspecified	0.00	0.80	Clear	MEAS	1	Imported Channel 1	UNSP	other		193				UNSP	UNSP	UNSP	unkn	UNSP	UNSP	UNSP
USGS	01541200	5	1956-01-11		Yes	YEH	USGS	3.52	152	Unspecified	0.00	1.00	Clear	MEAS	1	Imported Channel 1	UNSP	other		152				UNSP	UNSP	UNSP	unkn	UNSP	UNSP	UNSP
USGS	01541200	6	1956-02-15		Yes	GAR	USGS	4.87	1280	Good	0.10	1.20	Clear	MEAS	1	Imported Channel 1	UNSP	other		1280				UNSP	UNSP	UNSP	unkn	UNSP	UNSP	UNSP
USGS	01541200	7	1956-03-08		Yes	EVA	USGS	8.94	6750	Good	0.62	1.40	Clear	MEAS	1	Imported Channel 1	CRAN	unspe	unkno	6750	218	1610	4.19	UNSP	UNSP	UNSP	unkn	UNSP	UNSP	UNSP
USGS	01541200	8	1956-03-27		Yes	YEH	USGS	5.05	1410	Good	0.02	1.70	Clear	MEAS	1	Imported Channel 1	UNSP	other		1410				UNSP	UNSP	UNSP	unkn	UNSP	UNSP	UNSP
USGS	01541200	9	1956-04-23		Yes	WHY	USGS	5.08	1380	Good	0.01	1.20	Clear	MEAS	1	Imported Channel 1	UNSP	other		1380				UNSP	UNSP	UNSP	unkn	UNSP	UNSP	UNSP
"""

# shortened response from this URL: https://waterdata.usgs.gov/nwisweb/data/ratings/exsa/USGS.01541303.exsa.rdb
rating_fixture = """# //UNITED STATES GEOLOGICAL SURVEY       http://water.usgs.gov/
# //NATIONAL WATER INFORMATION SYSTEM     http://water.usgs.gov/data.html
# //DATA ARE PROVISIONAL AND SUBJECT TO CHANGE UNTIL PUBLISHED BY USGS
# //RETRIEVED: 2018-09-06 10:25:03
# //WARNING
# //WARNING The stage-discharge rating provided in this file should be
# //WARNING considered provisional and subject to change. Stage-discharge
# //WARNING ratings change over time as the channel features that control
# //WARNING the relation between stage and discharge vary. Users are
# //WARNING cautioned to consider carefully the applicability of this
# //WARNING rating before using it for decisions that concern personal or
# //WARNING public safety or operational consequences.
# //WARNING
# //WARNING This rating does not include any shifts that may have been
# //WARNING used along with this base rating in converting stage to
# //WARNING discharge at this site. Stage data processed with the rating
# //WARNING thus may not match that displayed or published by the USGS.
# //WARNING
# //FILE TYPE="NWIS RATING"
# //DATABASE NUMBER=01 DESCRIPTION=" Standard data base for this site."
# //STATION AGENCY="USGS " NUMBER="01541303       " TIME_ZONE="EST" DST_FLAG=Y
# //STATION NAME="West Branch Susquehanna River at Hyde, PA"
# //LABEL="Discharge (ft^3/s)"
# //PARAMETER CODE="00060"
# //RATING SHIFTED="20180906102503 EST"
# //RATING ID="11.0" TYPE="STGQ" NAME="stage-discharge" AGING=????
# //RATING REMARKS=""
# //RATING EXPANSION="logarithmic"
# //RATING OFFSET1=2.000000E+00
# //RATING_INDEP ROUNDING="????" PARAMETER="Gage height (ft)"
# //RATING_DEP ROUNDING="????" PARAMETER="Discharge (ft^3/s)"
# //RATING_DATETIME BEGIN=20160204024500 BZONE=-05:00 END=20170118000000 EZONE=-05:00 AGING=1
# //RATING_DATETIME BEGIN=20170118000000 BZONE=-05:00 END=-------------- EZONE=--- AGING=1
# //SHIFT_NEXT BEGIN="--------------" BZONE="---" END="--------------" EZONE="---"
# //SHIFT_NEXT STAGE1="---" SHIFT1="---" STAGE2="---" SHIFT2="---" STAGE3="---" SHIFT3="---"
# //SHIFT_NEXT COMMENT=" "
INDEP	SHIFT	DEP	STOR
16N	16N	16N	1S
2.50	0.00	27.90	*
2.51	0.00	29.25
2.52	0.00	30.65
2.53	0.00	32.08
2.54	0.00	33.54
2.55	0.00	35.05
2.56	0.00	36.59
2.57	0.00	38.18
2.58	0.00	39.80
"""


# A shortened version of this request: https://nwis.waterdata.usgs.gov/nwis/peak?site_no=01542500&agency_cd=USGS&format=rdb
peaks_fixture="""#
# U.S. Geological Survey
# National Water Information System
# Retrieved: 2019-10-28 22:35:01 EDT
#
# ---------------------------------- WARNING ----------------------------------------
# Some of the data that you have obtained from this U.S. Geological Survey database
# may not have received Director's approval. Any such data values are qualified
# as provisional and are subject to revision. Provisional data are released on the
# condition that neither the USGS nor the United States Government may be held liable
# for any damages resulting from its use.
#
# More data may be available offline.
# For more information on these data,  contact  USGS Water Data Inquiries.
# This file contains the annual peak streamflow data.
#
# This information includes the following fields:
#
#  agency_cd     Agency Code
#  site_no       USGS station number
#  peak_dt       Date of peak streamflow (format YYYY-MM-DD)
#  peak_tm       Time of peak streamflow (24 hour format, 00:00 - 23:59)
#  peak_va       Annual peak streamflow value in cfs
#  peak_cd       Peak Discharge-Qualification codes (see explanation below)
#  gage_ht       Gage height for the associated peak streamflow in feet
#  gage_ht_cd    Gage height qualification codes
#  year_last_pk  Peak streamflow reported is the highest since this year
#  ag_dt         Date of maximum gage-height for water year (if not concurrent with peak)
#  ag_tm         Time of maximum gage-height for water year (if not concurrent with peak
#  ag_gage_ht    maximum Gage height for water year in feet (if not concurrent with peak
#  ag_gage_ht_cd maximum Gage height code
#
# Sites in this file include:
#  USGS 01542500 WB Susquehanna River at Karthaus, PA
#
# Peak Streamflow-Qualification Codes(peak_cd):
#   1 ... Discharge is a Maximum Daily Average
#   2 ... Discharge is an Estimate
#   3 ... Discharge affected by Dam Failure
#   4 ... Discharge less than indicated value,
#           which is Minimum Recordable Discharge at this site
#   5 ... Discharge affected to unknown degree by
#           Regulation or Diversion
#   6 ... Discharge affected by Regulation or Diversion
#   7 ... Discharge is an Historic Peak
#   8 ... Discharge actually greater than indicated value
#   9 ... Discharge due to Snowmelt, Hurricane,
#           Ice-Jam or Debris Dam breakup
#   A ... Year of occurrence is unknown or not exact
#   Bd ... Day of occurrence is unknown or not exact
#   Bm ... Month of occurrence is unknown or not exact
#   C ... All or part of the record affected by Urbanization,
#            Mining, Agricultural changes, Channelization, or other
#   F ... Peak supplied by another agency
#   O ... Opportunistic value not from systematic data collection
#   R ... Revised
#
# Gage height qualification codes(gage_ht_cd,ag_gage_ht_cd):
#   1 ... Gage height affected by backwater
#   2 ... Gage height not the maximum for the year
#   3 ... Gage height at different site and(or) datum
#   4 ... Gage height below minimum recordable elevation
#   5 ... Gage height is an estimate
#   6 ... Gage datum changed during this year
#   7 ... Debris, mud, or hyper-concentrated flow
#   8 ... Gage height tidally affected
#   Bd ... Day of occurrence is unknown or not exact
#   Bm ... Month of occurrence is unknown or not exact
#   F ... Peak supplied by another agency
#   R ... Revised
#
#
agency_cd	site_no	peak_dt	peak_tm	peak_va	peak_cd	gage_ht	gage_ht_cd	year_last_pk	ag_dt	ag_tm	ag_gage_ht	ag_gage_ht_cd
5s	15s	10d	6s	8s	33s	8s	27s	4s	10d	6s	8s	27s
USGS	01542500	1936-03-18		135000	7	24.50
USGS	01542500	1940-04-01		50900		12.40	3
USGS	01542500	1941-04-06		19600		8.79	2		1941-03-05		8.95	1
USGS	01542500	1942-03-10		22600		9.38
USGS	01542500	1942-12-30		50200		13.82
USGS	01542500	1962-04-01		17000	6	8.35
USGS	01542500	1963-03-18		22700	6	9.63
USGS	01542500	1964-03-10		63500	6	15.98
USGS	01542500	1965-03-30		13600	6	7.54
USGS	01542500	1966-02-14		18900	6	8.88	2		1966-02-13		9.19	1
USGS	01542500	1967-03-16		17400	6	8.49
USGS	01542500	1968-05-25		11800	6	7.12	2		1968-01-31		7.12	1
USGS	01542500	1968-12-29		9500	6	6.35
USGS	01542500	1970-04-02		25800	6	10.29
USGS	01542500	1971-02-28		18400	6	8.79
USGS	01542500	2016-02-04		7880	6	6.05
USGS	01542500	2017-05-30		15700	6	8.43
USGS	01542500	2018-09-10	21:30	41000	6	13.22
"""
