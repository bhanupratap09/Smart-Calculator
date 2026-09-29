"""Matrix addition, subtraction, multiplication and inversion (NumPy)."""

import numpy as np

from calculator.input_utils import read_float, read_int


def validate_shapes(operation, shape_a, shape_b=None):
    """Raise ValueError if the operation is impossible for these shapes."""
    if operation in ("add", "subtract") and shape_a != shape_b:
        raise ValueError(f"Matrix {operation} is not possible with the given dimensions.")
    if operation == "multiply" and shape_a[1] != shape_b[0]:
        raise ValueError("Matrix multiplication is not possible with the given dimensions.")
    if operation == "inverse" and shape_a[0] != shape_a[1]:
        raise ValueError("Inverse is not possible for non-square matrices.")


def add(a, b):
    validate_shapes("add", a.shape, b.shape)
    return a + b


def subtract(a, b):
    validate_shapes("subtract", a.shape, b.shape)
    return a - b


def multiply(a, b):
    validate_shapes("multiply", a.shape, b.shape)
    return np.dot(a, b)


def inverse(a):
    validate_shapes("inverse", a.shape)
    try:
        return np.linalg.inv(a)
    except np.linalg.LinAlgError as exc:
        raise ValueError("The matrix is singular and does not have an inverse.") from exc


def _read_shape(name):
    rows = read_int(f"Enter the number of rows for the {name} matrix: ", min_value=1)
    cols = read_int(f"Enter the number of columns for the {name} matrix: ", min_value=1)
    return rows, cols


def _read_matrix(name, shape):
    print(f"Enter the elements of the {name} matrix:")
    m = np.zeros(shape)
    for i in range(shape[0]):
        for j in range(shape[1]):
            m[i][j] = read_float(f"Element [{i + 1}][{j + 1}]: ")
    return m


def _run_binary(operation, func, label):
    shape_a = _read_shape("first")
    shape_b = _read_shape("second")
    validate_shapes(operation, shape_a, shape_b)  # fail before typing elements
    a = _read_matrix("first", shape_a)
    b = _read_matrix("second", shape_b)
    print(f"The result of matrix {label} is:")
    print(func(a, b))


def run_matrix_operations():
    print("Matrix Operations")
    print("1. Addition\n2. Subtraction\n3. Multiplication")
    choice = read_int("Enter your choice (1-3): ", 1, 3)
    if choice == 1:
        _run_binary("add", add, "addition")
    elif choice == 2:
        _run_binary("subtract", subtract, "subtraction")
    else:
        _run_binary("multiply", multiply, "multiplication")


def run_inverse():
    print("Inverse Matrix")
    shape = _read_shape("")
    validate_shapes("inverse", shape)
    m = _read_matrix("", shape)
    print("The inverse of the matrix is:")
    print(inverse(m))
