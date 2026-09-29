import math
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from calculator import advanced_math as am, trigonometry as t


class TestTrigonometry(unittest.TestCase):
    def test_sine_90_degrees(self):
        self.assertAlmostEqual(t.sine(math.radians(90)), 1.0)

    def test_cosecant_undefined_at_pi(self):
        with self.assertRaises(ValueError):
            t.cosecant(math.pi)  # sin(pi) is ~1e-16, not exactly 0

    def test_secant_undefined_at_90(self):
        with self.assertRaises(ValueError):
            t.secant(math.pi / 2)

    def test_arcsine(self):
        self.assertAlmostEqual(t.arcsine(1), 90.0)

    def test_arcsine_out_of_domain(self):
        with self.assertRaises(ValueError):
            t.arcsine(2)

    def test_arcsecant_valid_and_invalid(self):
        self.assertAlmostEqual(t.arcsecant(2), 60.0)
        with self.assertRaises(ValueError):
            t.arcsecant(0.5)

    def test_arccosecant_valid_and_invalid(self):
        self.assertAlmostEqual(t.arccosecant(2), 30.0)
        with self.assertRaises(ValueError):
            t.arccosecant(0.5)

    def test_arccotangent_zero(self):
        self.assertEqual(t.arccotangent(0), 90.0)


class TestAlgebra(unittest.TestCase):
    def test_two_real_roots(self):
        kind, roots = am.solve_quadratic(1, -3, 2)
        self.assertEqual(kind, "two_real")
        self.assertEqual(sorted(roots), [1.0, 2.0])

    def test_one_real_root(self):
        kind, roots = am.solve_quadratic(1, 2, 1)
        self.assertEqual((kind, roots), ("one_real", (-1.0,)))

    def test_complex_roots(self):
        kind, roots = am.solve_quadratic(1, 1, 1)
        self.assertEqual(kind, "complex")
        self.assertAlmostEqual(roots[0].imag, math.sqrt(3) / 2)

    def test_a_zero_rejected(self):
        with self.assertRaises(ValueError):
            am.solve_quadratic(0, 2, 1)


if __name__ == "__main__":
    unittest.main()
