#! /bin/sh

wget -q http://www.oref.org.il/ -O - | grep '{label:' > cities.js
