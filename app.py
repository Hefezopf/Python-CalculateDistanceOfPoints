#!/usr/bin/python

import sys
import Point
import PointUtil
from Point import Point
from PointUtil import PointUtil

print("Start App...")

if len(sys.argv) > 1:
  points = PointUtil().parseAllCoords(sys.argv)
else:
  points = [Point(1, 1), Point(1, 3), Point(4, 4), Point(6, 1)]

minDistanceOfArray = PointUtil().determineMinimumOfArray(points)
maxDistanceOfArray = PointUtil().determineMaximumOfArray(points)

print("Minimum distance of all points = ", str(minDistanceOfArray))
print("Maximum distance of all points = ", str(maxDistanceOfArray))

