hiking-toys
===========

Python scripts for planning hiking trips including:
 * Stuff for loading routes and waypoints onto a Garmin [Foretrex® 401](https://buy.garmin.com/en-US/US/on-the-trail/wrist-worn/foretrex-401/prod30026.html) GPS.
 * Stuff for making paper maps with TileMill

The gps stuff basically just reads a list of CSV waypoints formatted like
```
decimal latitude, decimal longitude, waypoint name, comment
```
and writes GPX and GeoJSON. The GPX output is specifically intended to work with a Foretrex 401, since I like using one of those for navigating on foot. However, as far as I know the GPX ought to work with other devices too.
