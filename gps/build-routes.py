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
	jsonFile = open(jsonPath,"w")
	jsonFile.write(json.dumps(model))
	jsonFile.close()



def convertToGPX(csvPath,gpxPath):
	csvFile = open(csvPath,"r")
	waypoints = []

	skipHeader = True
	for line in csvFile:
		if skipHeader:
			skipHeader = False
		elif line.strip() == "":
			# ignore empty lines
			pass
		else:
			(lat,lon,waypoint,comment) = line.split(",")
			waypoints.append({"lon":float(lon), "lat": float(lat), "waypoint": waypoint.strip()})
	csvFile.close()

	gpxFile = open(gpxPath,"w")
	gpxFile.write("""<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
<gpx xmlns="http://www.topografix.com/GPX/1/1"
xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3"
xmlns:gpxtpx="http://www.garmin.com/xmlschemas/TrackPointExtension/v1"
creator="Foretrex 401"
version="1.1"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www.garmin.com/xmlschemas/GpxExtensions/v3/GpxExtensionsv3.xsd">\n""")

	for waypoint in waypoints:
		gpxFile.write("""<wpt lat="{:.6f}" lon="{:.6f}">""".format(waypoint["lat"], waypoint["lon"]))
		gpxFile.write("\n<ele>1828.00</ele><name>{}</name>\n".format(waypoint["waypoint"]))
		gpxFile.write("<sym>Waypoint</sym></wpt>\n")

	gpxFile.write("<rte><name>{}-{}</name>\n".format(waypoints[0]["waypoint"], waypoints[-1]["waypoint"]))
	for waypoint in waypoints:
		gpxFile.write("""<rtept lat="{:.6f}" lon="{:.6f}">""".format(waypoint["lat"], waypoint["lon"]))
		gpxFile.write("<name>{}</name></rtept>".format(waypoint["waypoint"]))
	gpxFile.write("</rte>\n")


	gpxFile.write("</gpx>\n");
	gpxFile.close()


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
