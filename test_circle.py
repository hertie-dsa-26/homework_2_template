import math
import unittest
from circle import Circle


class TestCirclePerimeter(unittest.TestCase):

    def test_perimeter_unit_circle(self):
        self.assertAlmostEqual(Circle(1).perimeter(), 2 * math.pi)

    def test_perimeter_radius_5(self):
        self.assertAlmostEqual(Circle(5).perimeter(), 10 * math.pi)

    def test_perimeter_zero_radius(self):
        self.assertAlmostEqual(Circle(0).perimeter(), 0)


class TestCircleArea(unittest.TestCase):

    def test_area_unit_circle(self):
        self.assertAlmostEqual(Circle(1).area(), math.pi)

    def test_area_radius_5(self):
        self.assertAlmostEqual(Circle(5).area(), 25 * math.pi)

    def test_area_zero_radius(self):
        self.assertAlmostEqual(Circle(0).area(), 0)


if __name__ == '__main__':
    unittest.main()
