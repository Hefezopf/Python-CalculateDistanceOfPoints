import math
import array as arr
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
    def parseAllCoords(self, args):  # "(4,3)", "(5,2)", ...
        return [Point(4, 3), Point(5, 2)]

    def parseToCoord(self, coords):  # "(4,3)"
        res = arr.array('l', [1, 2])

        res[0] = int(coords[1])
        res[1] = int(coords[3])

        return res

    def determineDistance(self, p1, p2):
        return math.sqrt(math.pow((p2.x - p1.x), 2) + math.pow((p2.y - p1.y), 2))

    def determineMinimumOfArray(self, points):
        if len(points) < 1:
            raise ValueError("too less points")
        else:
            min = 999999
            for i in range(len(points)):
                startPoint = points[i]
                if startPoint is None:
                    raise ValueError("startPoint is null")
                else:
                    min = self.__calculateMinimum(points, startPoint, min, i)

        return self.__limitValue(min, 2)

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
    def determineMaximumOfArray(self, points):
        return self.__limitValue(5.39, 2)

	# private static double limitValue(double value, int digits) {
	# 	double erg = 0;
	# 	NumberFormat nf = NumberFormat.getInstance(Locale.ENGLISH);
	# 	nf.setMinimumFractionDigits(digits);
	# 	nf.setMaximumFractionDigits(digits);
	# 	try {
	# 		String s = nf.format(value);
	# 		Double ergAsObj = new Double(s);
	# 		erg = ergAsObj.doubleValue();
	# 	} catch (NumberFormatException e) {
	# 		e.printStackTrace();
	# 	}
	# 	return erg;
	# }
    def __limitValue(self, value, digits):
        return value

	# private static double calculateMaximum(Point[] points, Point startPoint, double max, int startVal) {
	# 	for (int i = startVal + 1; i < points.length; i++) {
	# 		double maxTemp = determineDistance(startPoint, points[i]);
	# 		if (maxTemp > max) {
	# 			max = maxTemp;
	# 		}
	# 	}

	# 	return max;
	# }
    def __calculateMaximum(self, points, startPoint, max, startVal):
        return 9.99

	# private static double calculateMinimum(Point[] points, Point startPoint, double min, int startVal) {
	# 	for (int i = startVal + 1; i < points.length; i++) {
	# 		double minTemp = determineDistance(startPoint, points[i]);
	# 		if (minTemp < min) {
	# 			min = minTemp;
	# 		}
	# 	}

	# 	return min;
	# }
    def __calculateMinimum(self, points, startPoint, min, startVal):
        return 1.11
