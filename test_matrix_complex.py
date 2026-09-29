import os
import sys
import unittest

import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from calculator import advanced_math as am, matrix_ops


class TestMatrix(unittest.TestCase):
    def setUp(self):
        self.a = np.array([[1.0, 2.0], [3.0, 4.0]])
        self.b = np.array([[5.0, 6.0], [7.0, 8.0]])

    def test_add(self):
        np.testing.assert_array_equal(matrix_ops.add(self.a, self.b), [[6, 8], [10, 12]])

    def test_subtract(self):
        np.testing.assert_array_equal(matrix_ops.subtract(self.b, self.a), [[4, 4], [4, 4]])

    def test_multiply(self):
        np.testing.assert_array_equal(matrix_ops.multiply(self.a, self.b), [[19, 22], [43, 50]])

    def test_add_dimension_mismatch(self):
        with self.assertRaises(ValueError):
            matrix_ops.add(self.a, np.zeros((3, 3)))

    def test_multiply_dimension_mismatch(self):
        with self.assertRaises(ValueError):
            matrix_ops.multiply(np.zeros((2, 3)), np.zeros((2, 3)))

    def test_inverse(self):
        result = matrix_ops.inverse(self.a)
        np.testing.assert_allclose(np.dot(self.a, result), np.eye(2), atol=1e-9)

    def test_singular_matrix(self):
        with self.assertRaises(ValueError):
            matrix_ops.inverse(np.array([[1.0, 2.0], [2.0, 4.0]]))

    def test_non_square_inverse(self):
        with self.assertRaises(ValueError):
            matrix_ops.inverse(np.zeros((2, 3)))


class TestComplex(unittest.TestCase):
    def test_arithmetic(self):
        a, b = complex(1, 2), complex(3, 4)
        self.assertEqual(am.complex_add(a, b), complex(4, 6))
        self.assertEqual(am.complex_subtract(a, b), complex(-2, -2))
        self.assertEqual(am.complex_multiply(a, b), complex(-5, 10))
        self.assertAlmostEqual(am.complex_divide(a, b), complex(0.44, 0.08))

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            am.complex_divide(complex(1, 1), complex(0, 0))


if __name__ == "__main__":
    unittest.main()
