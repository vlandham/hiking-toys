import platform
import os
import sys
import subprocess

if not platform.system() == 'Darwin':
	print "\nSorry, this only works on Mac OS.\n"

elif len(sys.argv) != 2:
	print "\nUsage: python install-route.py <path/to/the-route.gpx>\n"

elif not os.path.isfile("/Volumes/GARMIN/Garmin/GarminDevice.xml"):
	print "\nPlease make sure your Garmin GPS is connected.\n"

elif not os.path.isfile(sys.argv[1]):
	print "\n{filename} is not a valid file.\n".format(filename=sys.argv[1])

else:
	gpsInputDir = "/Volumes/GARMIN/Garmin/gpx/"
	print "\nCopying {0} to {1}\n".format(sys.argv[1], gpsInputDir)
	subprocess.call(["cp", sys.argv[1], gpsInputDir])
