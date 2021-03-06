#!/usr/bin/env python
'''
Find the bounding box coordinates that encompass a city
using the PlaceFinder API

Input: locs.txt
    A file that contains the cities we are interested in
    with each city on a separate line.

Output: boundbox.json
    A JSON file containing the northeast and southwest latitude and
    longitude values for the bounding box of each city.

Written by Amy X Zhang <amy.xian.zhang@gmail.com> - http://amyxzhang.wordpress.com
Updated by Jeff Chan <jefftchan@gmail.com> - http://jeffchan.net
'''

import json
import urllib

# Load city names
cities = []
nfile = open('locs.txt', 'r')
lines = nfile.readlines()
for line in lines:
    line = line.strip()
    cities.append(line)

api_key = '57I4wiLV34EjVWNCYuOFTqGNMtPGfy0xgczCCNI8yS6J7RLauyMcH9X8sLLa_NzC'
base = 'http://where.yahooapis.com/v1/places'

results = {}
for loc in cities:
    print "\nSearching for: " + loc

    first = '.q(' + str(loc) + ')?&format=json&appid='
    url = base + first + api_key
    raw = urllib.urlopen(url)
    if not raw:
        print 'BAD INPUT'
        continue

    result = json.load(raw)
    print result

    place = result['places']['place'][0]
    name = place['name']
    ne_pt = place['boundingBox']['northEast']
    sw_pt = place['boundingBox']['southWest']

    results[name] = {
        'ne_lat': str(ne_pt['latitude']),
        'ne_lon': str(ne_pt['longitude']),
        'sw_lat': str(sw_pt['latitude']),
        'sw_lon': str(sw_pt['longitude'])
    }

ff = open('boundbox.json', 'w')
ff.write(json.dumps(results, indent=4))

ff.close()
