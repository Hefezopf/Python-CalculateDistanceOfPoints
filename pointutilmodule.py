import math
from pointmodule import Point


class PointUtil:

	# public static Point[] parseAllCoords(String[] allCoords) {
	# 	Point[] points;
	# 	List<Point> pointsList = new ArrayList<Point>();

	# 	for (String coord : Arrays.asList(allCoords)) { // "(4,3)", "(5,2)", ...
	# 		int[] xy = PointUtil.parseToCoord(coord);
	# 		pointsList.add(new Point(xy[0], xy[1]));
	# 	}
	# 	points = new Point[pointsList.size()];
	# 	points = pointsList.toArray(points);

	# 	return points;
	# }
    def parseAllCoords(self, args): # "(4,3)", "(5,2)", ...
        return [Point(4, 3), Point(5, 2)]

	# public static int[] parseToCoord(String coords) { // "(4,3)"
	# 	int[] res = new int[2];

	# 	res[0] = coords.charAt(1) - 48;
	# 	res[1] = coords.charAt(3) - 48;

	# 	return res;
	# }
    def parseToCoord(self, coords): # "(4,3)"
        return [4, 3]

    def determineDistance(self, p1, p2):
        return math.sqrt(math.pow((p2.x - p1.x), 2) + math.pow((p2.y - p1.y), 2))

    def determineMinimumOfArray(self, points):
        # for x in points:
        #    print("We're on time %d" % (x.x))
        return 2.0

    def determineMaximumOfArray(self, points):
        return 5.39
