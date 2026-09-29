import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from calculator import advanced_math as am, basic_math as bm, conversions


class TestCombinatorics(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(bm.factorial(0), 1)
        self.assertEqual(bm.factorial(5), 120)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            bm.factorial(-1)

    def test_permutations_and_combinations(self):
        self.assertEqual(bm.permutations(5, 2), 20)
        self.assertEqual(bm.combinations(5, 2), 10)

    def test_large_values_are_exact(self):
        # the original float-division version lost precision here
        self.assertEqual(bm.combinations(100, 50), 100891344545564193334812497256)

    def test_r_greater_than_n(self):
        with self.assertRaises(ValueError):
            bm.permutations(2, 5)


class TestStatistics(unittest.TestCase):
    def test_describe(self):
        r = am.describe([1, 2, 2, 3, 4])
        self.assertEqual(r["mean"], 2.4)
        self.assertEqual(r["median"], 2)
        self.assertEqual(r["mode"], [2])
        self.assertAlmostEqual(r["std_dev"], 1.0198039, places=6)

    def test_no_unique_mode(self):
        self.assertIsNone(am.describe([1, 2, 3])["mode"])

    def test_empty_rejected(self):
        with self.assertRaises(ValueError):
            am.describe([])


class TestConversions(unittest.TestCase):
    def test_length(self):
        results = dict(conversions.convert_units(0, 1000))
        self.assertEqual(results["kilometers"], 1.0)

    def test_temperature(self):
        results = dict(conversions.convert_units(2, 100))
        self.assertEqual(results["degrees Fahrenheit"], 212.0)
        self.assertEqual(results["kelvin"], 373.15)

    def test_decimal_to_bases(self):
        self.assertEqual(conversions.decimal_to_base(10, 2), "1010")
        self.assertEqual(conversions.decimal_to_base(8, 8), "10")
        self.assertEqual(conversions.decimal_to_base(255, 16), "FF")

    def test_negative_decimal_to_binary(self):
        self.assertEqual(conversions.decimal_to_base(-5, 2), "-101")

    def test_base_to_decimal(self):
        self.assertEqual(conversions.base_to_decimal("1010", 2), 10)
        self.assertEqual(conversions.base_to_decimal("ff", 16), 255)

    def test_invalid_base_input(self):
        with self.assertRaises(ValueError):
            conversions.base_to_decimal("102", 2)


if __name__ == "__main__":
    unittest.main()
