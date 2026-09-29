"""Advanced math: quadratic equation solver, complex number arithmetic and
descriptive statistics."""

import cmath
import math
import statistics

from calculator.input_utils import read_float, read_int, read_numbers


# ------------------------------------------------------------------ quadratic
def solve_quadratic(a, b, c):
    """Return (kind, roots) where kind is 'two_real', 'one_real' or 'complex'."""
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero for a quadratic equation.")
    d = b * b - 4 * a * c
    if d > 0:
        s = math.sqrt(d)
        return "two_real", ((-b + s) / (2 * a), (-b - s) / (2 * a))
    if d == 0:
        return "one_real", (-b / (2 * a),)
    s = cmath.sqrt(d)
    return "complex", ((-b + s) / (2 * a), (-b - s) / (2 * a))


def run_quadratic():
    print("Quadratic Equation Solver")
    print("The standard form is: ax^2 + bx + c = 0")
    a = read_float("Enter the coefficient a: ")
    b = read_float("Enter the coefficient b: ")
    c = read_float("Enter the coefficient c: ")
    kind, roots = solve_quadratic(a, b, c)
    if kind == "two_real":
        print("The equation has two real roots:", roots[0], "and", roots[1])
    elif kind == "one_real":
        print("The equation has one real root:", roots[0])
    else:
        print("The equation has no real roots.")
        print("The complex roots are:", roots[0], "and", roots[1])


# -------------------------------------------------------------- complex numbers
def complex_add(a, b):
    return a + b


def complex_subtract(a, b):
    return a - b


def complex_multiply(a, b):
    return a * b


def complex_divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b


OPERATIONS = [
    ("Addition", complex_add), ("Subtraction", complex_subtract),
    ("Multiplication", complex_multiply), ("Division", complex_divide),
]


def _read_complex(label):
    real = read_float(f"Enter the real part of the {label} complex number: ")
    imag = read_float(f"Enter the imaginary part of the {label} complex number: ")
    return complex(real, imag)


def run_complex():
    print("Complex Number Operations")
    for i, (name, _) in enumerate(OPERATIONS, start=1):
        print(f"{i}. {name}")
    name, func = OPERATIONS[read_int("Enter your choice (1-4): ", 1, 4) - 1]
    a = _read_complex("first")
    b = _read_complex("second")
    print(f"The result of {name.lower()} is: {func(a, b)}")


# ----------------------------------------------------------------- statistics
def describe(data):
    """Return a dict with mean, median, mode (or None) and population std dev."""
    if not data:
        raise ValueError("At least one value is required.")
    modes = statistics.multimode(data)
    has_unique_mode = len(modes) == 1 or len(modes) < len(set(data))
    return {
        "mean": statistics.mean(data),
        "median": statistics.median(data),
        "mode": modes if has_unique_mode else None,
        "std_dev": statistics.pstdev(data),
    }


def run_statistics():
    print("Statistics (Mean, Median, Mode, Standard Deviation)")
    result = describe(read_numbers())
    print(f"Mean: {result['mean']}")
    print(f"Median: {result['median']}")
    if result["mode"] is None:
        print("Mode: No unique mode found.")
    else:
        print(f"Mode: {', '.join(str(m) for m in result['mode'])}")
    print(f"Standard Deviation: {result['std_dev']}")
