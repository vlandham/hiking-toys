from os import listdir
from os.path import join, isfile
import json

def convertToJSON(csvPath,jsonPath):
	csvFile = open(csvPath,"r")
	model = { "type": "FeatureCollection", "features": [] }
	lineString = {
		"type": "Feature",
		"geometry": {
			"type": "LineString",
			"coordinates": []
			},
		"properties": {}
		}
	model["features"].append(lineString)

	skipHeader = True
	for line in csvFile:
		if skipHeader:
			skipHeader = False
		else:
			(lat,lon,waypoint,comment) = line.split(",")
			lineString["geometry"]["coordinates"].append([float(lon), float(lat)]) 
			if comment.strip() != "":
				marker = {
					"type": "Feature",
					"geometry": {
						"type": "Point",
						"coordinates": [float(lon), float(lat)]
						},
					"properties": {
						"waypoint": waypoint.strip(),
						"comment": comment.strip()
						}
					}
				model["features"].append(marker)
				

	csvFile.close()
	#print json.dumps(model)
	jsonFile = open(jsonPath,"w")
	jsonFile.write(json.dumps(model))
	jsonFile.close()



def convertToGPX(csvPath,gpxPath):
	pass


# Traverse the CSV directory and convert the contents to JSON and GPX
print
csvDir  = "csv"
jsonDir = "json"
gpxDir  = "gpx"
for name in listdir(csvDir):
	path = join(csvDir,name)
	if isfile(path) and path.endswith(".csv"):
		baseName = name[:-4]
		csvPath  = join(csvDir,"{}.csv".format(baseName))
		jsonPath = join(jsonDir,"{}.geojson".format(baseName))
		gpxPath  = join(gpxDir,"{}.gpx".format(baseName))

		print "Converting '{}':".format(csvPath)
		print "  -> '{}'".format(jsonPath)
		print "  -> '{}'".format(gpxPath)
		convertToJSON(csvPath,jsonPath)
		convertToGPX(csvPath,gpxPath)
		print
