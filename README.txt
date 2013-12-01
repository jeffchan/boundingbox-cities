Find the bounding box coordinates that encompass a city
using the PlaceFinder API

Input: locs.txt
    A file that contains the cities we are interested in
    with each city on a separate line.

Output: boundbox.json
    A JSON file containing the northeast and southwest latitude and
    longitude values for the bounding box of each city.

Input and output files have already been populated with 50 cities
as an example

This code could potentially also be used, with minor tweaking, to
find bounding box values for entities other than cities, depending
on what else is available on Yahoo! PlaceFinder, such as counties
and neighborhoods.

Yahoo! PlaceFinder
http://developer.yahoo.com/geo/placefinder/

Written by Amy X Zhang <amy.xian.zhang@gmail.com> - http://amyxzhang.wordpress.com
Updated by Jeff Chan <jefftchan@gmail.com> - http://jeffchan.net
