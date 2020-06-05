import unittest
from pointmodule import Point
from pointutilmodule import PointUtil


class TestApp(unittest.TestCase):

    def test_Point(self):
        p = Point(1, 2)
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 2)

    def test_PointUtil_determineDistance1(self):
        val = PointUtil().determineDistance(Point(1, 1), Point(2, 2))
        self.assertEqual(val, 1.4142135623730951)

    def test_PointUtil_determineDistance2(self):
        val = PointUtil().determineDistance(Point(1, 1), Point(3, 1))
        self.assertEqual(val, 2.0)


    def test_PointUtil_determineMinimumOfArray(self):
        val = PointUtil().determineMinimumOfArray(
            [Point(1, 1), Point(1, 3), Point(4, 4), Point(6, 1)])
        self.assertEqual(val, 2.0)

    def test_PointUtil_determineMaximumOfArray(self):
        val = PointUtil().determineMaximumOfArray(
            [Point(1, 1), Point(1, 3), Point(4, 4), Point(6, 1)])
        self.assertEqual(val, 5.39)


if __name__ == '__main__':
    unittest.main()
