hiking-toys
===========

Python scripts for planning hiking trips with a Garmin [Foretrex® 401](https://buy.garmin.com/en-US/US/on-the-trail/wrist-worn/foretrex-401/prod30026.html) GPS.

Basically this just reads a list of CSV waypoints formatted like
```
decimal latitude, decimal longitude, waypoint name, comment
```
and writes GPX and GeoJSON. The GPX output is specifically intended to work with a Foretrex 401, since that's what I use for navigating on foot. However, the GPX will probably work with lots of other stuff too.
