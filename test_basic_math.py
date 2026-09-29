import math
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from calculator import basic_math as bm


class TestArithmetic(unittest.TestCase):
    def test_add(self):
        self.assertEqual(bm.add([1, 2, 3]), 6)

    def test_subtract(self):
        self.assertEqual(bm.subtract([10, 3, 2]), 5)

    def test_multiply(self):
        self.assertEqual(bm.multiply([2, 3, 4]), 24)

    def test_divide(self):
        self.assertEqual(bm.divide([100, 5, 2]), 10)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            bm.divide([5, 0])


class TestPowersLogs(unittest.TestCase):
    def test_square_root(self):
        self.assertEqual(bm.square_root(9), 3)

    def test_square_root_negative(self):
        with self.assertRaises(ValueError):
            bm.square_root(-9)

    def test_power(self):
        self.assertEqual(bm.power(2, 10), 1024.0)

    def test_natural_log(self):
        self.assertAlmostEqual(bm.logarithm(math.e), 1.0)

    def test_log_base_10(self):
        self.assertAlmostEqual(bm.logarithm(1000, 10), 3.0)

    def test_log_invalid_inputs(self):
        with self.assertRaises(ValueError):
            bm.logarithm(-1)
        with self.assertRaises(ValueError):
            bm.logarithm(10, 1)
        with self.assertRaises(ValueError):
            bm.logarithm(10, -2)


if __name__ == "__main__":
    unittest.main()
