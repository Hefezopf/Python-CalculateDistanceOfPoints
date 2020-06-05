import unittest
from Point import Point

class TestApp(unittest.TestCase):

    def test_Point(self):
        p = Point(1,2)
        self.assertEqual(p.x, 1)        
        self.assertEqual(p.y, 2)

if __name__ == '__main__':
    unittest.main()