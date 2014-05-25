hiking-toys
===========

Python script for planning hiking trips with a Garmin Foretrex® 401 GPS.

Basically this just reads a list of CSV waypoints formatted like
```
latitude, longitude, short waypoint name, optional comment
```
and writes GPX and GeoJSON. The GPX output is specifically intended to work with a Foretrex 401, since that's what I use for navigating on foot. However, the GPX will probably work with lots of other stuff too.
