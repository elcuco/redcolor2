#! /usr/bin/python

import sys


def get_area_id(area_name):
	return "-12"

def get_lat_long(area_name):
	return "-1,-1"

def get_safe_time(area_name):
	return "180"

fname = 'cities.js';
lines = [line.strip() for line in open(fname)]

print "var cities = [\n" 

# name, cityID, "lat:long", areaID
count  = 0;
for line in lines:
	count += 1
	if not "{" in line: continue
	line2 = line
	line2 = line2.replace("{", "")
	line2 = line2.replace("}", "")
	v = line2.split(", ")

	v[0] = v[0].replace(":", ": ")
	v[1] = v[1].replace(":", ": ")

	sys.stdout.write( "        { " )
	sys.stdout.write( v[0] )
	sys.stdout.write( ", " )
	sys.stdout.write( v[1] )

	if (not v[1].endswith(",")):
		sys.stdout.write(",")
	sys.stdout.write( " " )
	
	sys.stdout.write( "latlong: '")
	sys.stdout.write( get_lat_long(v[1]) )
	sys.stdout.write( "', " )


	sys.stdout.write( "areaid: '" )
	sys.stdout.write( get_area_id(v[1]) )	
	sys.stdout.write( "', " )
	
	sys.stdout.write( "safetime: " )
	sys.stdout.write( get_safe_time(v[1]) )	
	sys.stdout.write( " }" )


	if count != len(lines)-1:
		sys.stdout.write(",")
	sys.stdout.write( "\n" )

print "    ];\n"