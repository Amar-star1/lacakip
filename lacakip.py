#!/usr/bin/env python

from os import *
from urllib import *
from time import *
import sys
import json 
import requests

banner = """
\033[1;32m
_|_|_|_|  _|                  _|      _|_|_|
_|            _|_|_|      _|_|_|        _|    _|_|_|
_|_|_|    _|  _|    _|  _|    _|        _|    _|    _|
_|        _|  _|    _|  _|    _|        _|    _|    _|
_|        _|  _|    _|    _|_|_|      _|_|_|  _|_|_|
                                              _|
                                              _|
\033[0m        \t-={ \033[1;36mBy Mr.AMAR\033[0m }=-
\033[0m        \t-={ \033[1;36mBlackHole Security\033[0m }=-
"""

print banner
print
target = raw_input("Enter Your Ip Target :\033[1;32m ")
url = "http://ip-api.com/json/" +target
url2 = "https://tools.keycdn.com/geo.json?host=" +target
dat = urlopen(url, url2).read().decode("utf-8")
data = json.loads(dat)
print
print("\033[1;36m[ # ] \033[1;32mRESULT >>>\033[0m")
print
print "\033[1;36m[ $ ] \033[0mAS :\033[1;32m ", str(data["as"])
print "\033[1;36m[ $ ] \033[0mCOUNTRY :\033[1;36m ", str(data["country"])
print "\033[1;36m[ $ ] \033[0mCITY :\033[1;32m ", str(data["city"])
print "\033[1;36m[ $ ] \033[0mCOUNTRY CODE :\033[1;32m ", str(data["countryCode"])
print "\033[1;36m[ $ ] \033[0mISP :\033[1;32m ", str(data["isp"])
print "\033[1;36m[ $ ] \033[0mLATITUDE :\033[1;32m ", str(data["lat"])
print "\033[1;36m[ $ ] \033[0mLONGTITUDE :\033[1;32m ", str(data["lon"])
print "\033[1;36m[ $ ] \033[0mORG :\033[1;32m ", str(data["org"])
print "\033[1;36m[ $ ] \033[0mQUERY :\033[1;32m ", str(data["query"])
print "\033[1;36m[ $ ] \033[0mREGION :\033[1;32m ", str(data["region"])
print "\033[1;36m[ $ ] \033[0mREGION NAME :\033[1;32m ", str(data["regionName"])
print "\033[1;36m[ $ ] \033[0mTIME ZONE :\033[1;36m ", str(data["timezone"])
print "\033[1;36m[ $ ] \033[0mZIP :\033[1;32m ", str(data["zip"])
print "\033[1;36m[ $ ] \033[0mSTATUS :\033[1;32m ", str(data["status"])
lat = str(data["lat"])
lon = str(data["lon"])
print "\033[1;36m[ $ ] \033[0mWITH GOOGLE MAPS :\033[1;36m http://www.google.com/maps/place/%s,%s/@%s,%s,16z\033[0m" %(lat,lon,lat,lon)
print
if __name__=='__main__':
	print "\033[1;31m$ \033[0mThanks For Using This Script"
	print
	sys.exit()

