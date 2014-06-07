import json

"""
This prints a geojson latitude and longitude graticule using hardcoded
bounding box coordinates and step sizes. The map(lambda...) stuff is because
range() only does integers and I want float steps (e.g. 0.05 degrees).
"""

north = 41.0
south = 39.0
west  = -106.0
east  = -105.0

latStep = 0.05
lonStep = -0.05
n = 100.0

model = { "type": "FeatureCollection", "features": [] }
for lon in map(lambda x: x/n, range(int(east*n),int(west*n),int(lonStep*n))):
	lineString = {
		"type": "Feature",
		"geometry": {
			"type": "LineString",
			"coordinates": [[lon, south], [lon, north]]
			},
		"properties": {
			"name": "{}".format(lon)
			}
		}
	model["features"].append(lineString)

for lat in map(lambda x: x/n, range(int(south*n),int(north*n),int(latStep*n))):
	lineString = {
		"type": "Feature",
		"geometry": {
			"type": "LineString",
			"coordinates": [[west, lat], [east, lat]]
			},
		"properties": {
			"name": "{}".format(lat)
			}
		}
	model["features"].append(lineString)
			
print json.dumps(model,indent=2)

