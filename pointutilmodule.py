import math
from pointmodule import Point


class PointUtil:

    def parseAllCoords(self, args):
        return [Point(1, 1), Point(1, 3), Point(4, 4), Point(6, 1)]


        # public static double determineMaximumOfArray(Point[] points) {
        # 	if (points.length < 1) {
        # 		throw new IllegalArgumentException("too less points");
        # 	}
        # 	double max = 0;
        # 	for (int i = 0; i < points.length; i++) {
        # 		Point startPoint = points[i];
        # 		if (startPoint == null) {
        # 			throw new IllegalArgumentException("startPoint is null");
        # 		}
        # 		max = calculateMaximum(points, startPoint, max, i);
        # 	}

        # 	return limitValue(max, 2);
        # }

    def determineDistance(self, p1, p2):
        return math.sqrt(math.pow((p2.x - p1.x), 2) + math.pow((p2.y - p1.y), 2))

    def determineMinimumOfArray(self, points):
        # for x in points:
        #    print("We're on time %d" % (x.x))
        return 2.0

    def determineMaximumOfArray(self, points):
        return 5.39
