#!/usr/bin/python

	# public static void main(String[] args) {
	# 	System.out.println("Start App...");

	# 	//String[] coords = { "(1,1)", "(1,3)", "(4,4)", "(6,1)" };
	# 	Point[] points;
	# 	if (args.length > 0) {
	# 		points = PointUtil.parseAllCoords(args);
	# 	} else {
	# 		Point[] pointsFixed = new Point[4];
	# 		pointsFixed[0] = new Point(1, 1);
	# 		pointsFixed[1] = new Point(1, 3);
	# 		pointsFixed[2] = new Point(4, 4);
	# 		pointsFixed[3] = new Point(6, 1);
	# 		points = pointsFixed;
	# 	}

	# 	double minDistanceOfArray = PointUtil.determineMinimumOfArray(points);
	# 	System.out.println("Minimum distance of all points = " + minDistanceOfArray);
	# 	double maxDistanceOfArray = PointUtil.determineMaximumOfArray(points);
	# 	System.out.println("Maximum distance of all points = " + maxDistanceOfArray);
	# }

# def printme( str ):
#    print (str)
#    return    

import sys

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))
print("Start App...")

minDistanceOfArray = 9
maxDistanceOfArray = 99
print ("Minimum distance of all points = ", str(minDistanceOfArray))
print ("Maximum distance of all points = ", str(maxDistanceOfArray))
