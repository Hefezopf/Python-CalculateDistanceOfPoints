import math
import sys
import array as arr
from pointmodule import Point


class PointUtil:

    def parseAllCoords(self, coords):  # "(4,3)", "(5,2)", ...
        liste = []
        for coord in coords:
            val = self.parseToCoord(coord)
            liste.append(Point(val[0], val[1]))

        return liste

    def parseToCoord(self, coord):  # "(4,3)"
        res = arr.array('l', [1, 2])

        res[0] = int(coord[1])
        res[1] = int(coord[3])

        return res

    def determineDistance(self, p1, p2):
        return math.sqrt(math.pow((p2.x - p1.x), 2) + math.pow((p2.y - p1.y), 2))

    def determineMinimumOfArray(self, points):
        if len(points) < 1:
            raise ValueError("too less points")
        else:
            min = sys.maxsize
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

    def __limitValue(self, value, digits):
        return float("{:.{}f}".format(value, digits))

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
