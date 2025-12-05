import unittest

import math

from lib import rectangle, triangle, circle, square

class RectangleTestCase(unittest.TestCase):
    def test_area_1(self):
        result = rectangle.area(10, 5)
        self.assertEqual(result, 50)
    
    def test_area_2(self):
        result = rectangle.area(0, 15)
        self.assertEqual(result, 0)
    
    def test_area_3(self):
        result = rectangle.area(7, 7)
        self.assertEqual(result, 49)
    
    def test_area_4(self):
        result = rectangle.area(5.5, 3.2)
        self.assertAlmostEqual(result, 17.6, places=2)
    
    def test_area_5(self):
        result = rectangle.area(1000, 500)
        self.assertEqual(result, 500000)

    def test_area_6(self):
        with self.assertRaises(ValueError):
            rectangle.area(-1, 10)
    
    def test_perimeter_1(self):
        result = rectangle.perimeter(10, 5)
        self.assertEqual(result, 30)
    
    def test_perimeter_2(self):
        result = rectangle.perimeter(4, 4)
        self.assertEqual(result, 16)
    
    def test_perimeter_3(self):
        result = rectangle.perimeter(3.5, 2.5)
        self.assertAlmostEqual(result, 12.0, places=2)
    
    def test_perimeter_4(self):
        result = rectangle.perimeter(150, 75)
        self.assertEqual(result, 450)
    
    def test_perimeter_5(self):
        result = rectangle.perimeter(20, 0)
        self.assertEqual(result, 40)
    
    def test_perimeter_6(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(-1, 10)

class CircleTestCase(unittest.TestCase):
    def test_area_1(self):
        result = circle.area(5)
        expected = math.pi * 25
        self.assertAlmostEqual(result, expected, places=5)
    
    def test_area_2(self):
        result = circle.area(1)
        expected = math.pi
        self.assertAlmostEqual(result, expected, places=5)
    
    def test_area_3(self):
        result = circle.area(0)
        self.assertEqual(result, 0)
    
    def test_area_4(self):
        result = circle.area(2.5)
        expected = math.pi * 6.25
        self.assertAlmostEqual(result, expected, places=5)
    
    def test_area_5(self):
        result = circle.area(100)
        expected = math.pi * 10000
        self.assertAlmostEqual(result, expected, places=5)

    def test_area_6(self):
        with self.assertRaises(ValueError):
            circle.area(-1)
    
    def test_perimeter_1(self):
        result = circle.perimeter(5)
        expected = 2 * math.pi * 5
        self.assertAlmostEqual(result, expected, places=5)
    
    def test_perimeter_2(self):
        result = circle.perimeter(1)
        expected = 2 * math.pi
        self.assertAlmostEqual(result, expected, places=5)
    
    def test_perimeter_3(self):
        result = circle.perimeter(0)
        self.assertEqual(result, 0)
    
    def test_perimeter_4(self):
        result = circle.perimeter(2.5)
        expected = 2 * math.pi * 2.5
        self.assertAlmostEqual(result, expected, places=5)
    
    def test_perimeter_5(self):
        result = circle.perimeter(100)
        expected = 2 * math.pi * 100
        self.assertAlmostEqual(result, expected, places=5)

    def test_perimeter_6(self):
        with self.assertRaises(ValueError):
            circle.perimeter(-1)

class SquareTestCase(unittest.TestCase):
    def test_area_1(self):
        result = square.area(5)
        self.assertEqual(result, 25)
    
    def test_area_2(self):
        result = square.area(1)
        self.assertEqual(result, 1)
    
    def test_area_3(self):
        result = square.area(0)
        self.assertEqual(result, 0)
    
    def test_area_4(self):
        result = square.area(3.5)
        self.assertAlmostEqual(result, 12.25, places=2)
    
    def test_area_5(self):
        result = square.area(100)
        self.assertEqual(result, 10000)

    def test_area_6(self):
        with self.assertRaises(ValueError):
            square.area(-10)
    
    def test_perimeter_1(self):
        result = square.perimeter(5)
        self.assertEqual(result, 20)
    
    def test_perimeter_2(self):
        result = square.perimeter(1)
        self.assertEqual(result, 4)
    
    def test_perimeter_3(self):
        result = square.perimeter(0)
        self.assertEqual(result, 0)
    
    def test_perimeter_4(self):
        result = square.perimeter(3.5)
        self.assertAlmostEqual(result, 14.0, places=2)
    
    def test_perimeter_5(self):
        result = square.perimeter(100)
        self.assertEqual(result, 400)

    def test_perimeter_6(self):
        with self.assertRaises(ValueError):
            square.perimeter(-10)

class TriangleTestCase(unittest.TestCase):
    def test_area_1(self):
        result = triangle.area(3, 4)
        self.assertEqual(result, 6)
    
    def test_area_2(self):
        result = triangle.area(0, 10)
        self.assertEqual(result, 0)
    
    def test_area_3(self):
        result = triangle.area(10, 0)
        self.assertEqual(result, 0)
    
    def test_area_4(self):
        result = triangle.area(4.5, 3.2)
        self.assertAlmostEqual(result, 7.2, places=2)
    
    def test_area_5(self):
        result = triangle.area(500, 300)
        self.assertEqual(result, 75000)

    def test_area_6(self):
        with self.assertRaises(ValueError):
            triangle.area(-10, 10)
    
    def test_perimeter_1(self):
        result = triangle.perimeter(3, 4, 5)
        self.assertEqual(result, 12)
    
    def test_perimeter_2(self):
        result = triangle.perimeter(5, 5, 5)
        self.assertEqual(result, 15)
    
    def test_perimeter_3(self):
        result = triangle.perimeter(7, 8, 9)
        self.assertEqual(result, 24)
    
    def test_perimeter_4(self):
        result = triangle.perimeter(2.5, 3.5, 4.5)
        self.assertAlmostEqual(result, 10.5, places=2)
    
    def test_perimeter_5(self):
        result = triangle.perimeter(0, 0, 0)
        self.assertEqual(result, 0)

    def test_area_6(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(-10, 10, 1)