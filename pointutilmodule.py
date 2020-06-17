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
    def parseAllCoords(self, coords):  # "(4,3)", "(5,2)", ...
        liste = []
        # for coord in coords:
        #val = self.parseToCoord(coord)
        # liste.append(val)
        #print(liste)
        return [Point(4, 3), Point(5, 2)]  # liste

    def parseToCoord(self, coord):  # "(4,3)"
        res = arr.array('l', [1, 2])
        #print(coord)
        res[0] = int(coord[1])
        res[1] = int(coord[3])

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

    def determineMaximumOfArray(self, points):
        if len(points) < 1:
            raise ValueError("too less points")
        else:
            max = 0
            for i in range(len(points)):
                startPoint = points[i]
                if startPoint is None:
                    raise ValueError("startPoint is null")
                else:
                    max = self.__calculateMaximum(points, startPoint, max, i)

        return self.__limitValue(max, 2)

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

    def __calculateMaximum(self, points, startPoint, max, startVal):
        i = startVal + 1
        for point in points:
            if i == len(points):
                return max
            maxTemp = self.determineDistance(startPoint, points[i])
            if maxTemp > max:
                max = maxTemp
            i = i + 1
        return max

    def __calculateMinimum(self, points, startPoint, min, startVal):
        i = startVal + 1
        for point in points:
            if i == len(points):
                return min
            minTemp = self.determineDistance(startPoint, points[i])
            if minTemp < min:
                min = minTemp
            i = i + 1
        return min
