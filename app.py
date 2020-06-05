#!/usr/bin/python

import sys
from point import Point

def parseAllCoords(args):
   return [Point(1, 1), Point(1, 3), Point(4, 4), Point(6, 1)]

def determineMinimumOfArray(points):
   return 2.0

def determineMaximumOfArray(points):
   return 5.39



print("Start App...")

if len(sys.argv) > 1:
  points = parseAllCoords(sys.argv)
else:
  points = [Point(1, 1), Point(1, 3), Point(4, 4), Point(6, 1)]

minDistanceOfArray = determineMinimumOfArray(points)
maxDistanceOfArray = determineMaximumOfArray(points)

print("Minimum distance of all points = ", str(minDistanceOfArray))
print("Maximum distance of all points = ", str(maxDistanceOfArray))
