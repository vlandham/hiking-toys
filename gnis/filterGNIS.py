import gzip;
import string;

"""
This filters Geographic Names Information System (GNIS) extract files, which
contain official POI names from the United States Board on Geographic Names,
into a TileMill-friendly .csv format. 

For more information on GNIS, see:
  http://http://geonames.usgs.gov/domestic/download_data.htm

For my purposes, the interesting pipe-separated fields in the raw extract are:
   1: FEATURE_NAME
   2: FEATURE_CLASS
   3: STATE_ALPHA
   5: COUNTY_NAME
   9: PRIM_LAT_DEC
  10: PRIM_LONG_DEC
  13: SOURCE_LAT_DEC
  14: SOURCE_LONG_DEC
  16: ELEV_IN_FT
"""

rawGNIS = gzip.open('CO_Features_20140401.txt.gz','r')

classes = [
	'Summit',
	'Tower',
	'Pillar',
]

counties = [
	'Boulder',
	'Jefferson',
	'Broomfield',
	'Denver',
	'Gilpin',
	'Clear Creek',
	'Grand',
	'Larimer'
]

skipFeatures = [
	'Boulder Mountain',
	'Flagstaff Memorial',
	'Paiute Peak'
]


print 'featureName,featureClass,lat,lon,elevationFeet'

for line in rawGNIS:
	fields = string.split(line,'|')
	county = fields[5]
	featureName = fields[1]
	featureClass = fields[2]
	lat = fields[9]
	lon = fields[10]
	elevation = fields[16]

	if (featureClass in classes) and (county in counties) and not (featureName in skipFeatures):
		print "{},{},{},{},{}".format(featureName, featureClass, lat, lon, elevation)

rawGNIS.close()

