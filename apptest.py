import unittest
from pointmodule import Point
from pointutilmodule import PointUtil


class TestApp(unittest.TestCase):

    pA = Point(1, 1)
    pB = Point(1, 3)
    pC = Point(4, 4)
    pD = Point(6, 1)

    def test_Point(self):
        p = Point(1, 2)

        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 2)

    def test_PointUtil_parseAllCoords(self):
        val = PointUtil().parseAllCoords(['(4,3)', '(5,2)'])

        self.assertEqual(val[0].x, 4)
        self.assertEqual(val[0].y, 3)
        self.assertEqual(val[1].x, 5)
        self.assertEqual(val[1].y, 2)

    def test_PointUtil_parseToCoord(self):
        val = PointUtil().parseToCoord("(4,3)")

        self.assertEqual(val[0], 4)
        self.assertEqual(val[1], 3)

    def test_PointUtil_parseToCoord2(self):
        val = PointUtil().parseToCoord("(1,2)")

        self.assertEqual(val[0], 1)
        self.assertEqual(val[1], 2)

    def test_PointUtil_determineDistance1(self):
        val = PointUtil().determineDistance(Point(1, 1), Point(2, 2))

        self.assertEqual(val, 1.4142135623730951)

    def test_PointUtil_determineDistance2(self):
        val = PointUtil().determineDistance(Point(1, 1), Point(3, 1))

        self.assertEqual(val, 2.0)

    def test_PointUtil_determineMaximumOfArray1(self):
        val = PointUtil().determineMaximumOfArray([self.pA, self.pB, self.pC])

        self.assertEqual(val, 4.24)

    def test_PointUtil_determineMaximumOfArray2(self):
        val = PointUtil().determineMaximumOfArray(
            [self.pA, self.pB, self.pC, self.pD])
        self.assertEqual(val, 5.39)

    def test_PointUtil_determineMaximumOfArray3(self):
        val = PointUtil().determineMaximumOfArray([self.pA, self.pC, self.pD])

        self.assertEqual(val, 5.00)

    def test_PointUtil_determineMaximumOfArray4(self):
        val = PointUtil().determineMaximumOfArray(
            [Point(1, 1), Point(9, 9)])
        self.assertEqual(val, 11.31)

    def test_PointUtil_determineMinimumOfArray1(self):
        val = PointUtil().determineMinimumOfArray([self.pA, self.pC, self.pD])

        self.assertEqual(val, 3.61)

    def test_PointUtil_determineMinimumOfArray2(self):
        val = PointUtil().determineMinimumOfArray(
            [self.pA, self.pB, self.pC, self.pD])

        self.assertEqual(val, 2.00) 


if __name__ == '__main__':
    unittest.main()
