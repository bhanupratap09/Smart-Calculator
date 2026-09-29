"""Basic math: arithmetic, square root, power, logarithm, factorial,
permutations and combinations."""

import math

from calculator.input_utils import read_float, read_int, read_numbers


# ---------------------------------------------------------------- arithmetic
def add(numbers):
    return sum(numbers)


def subtract(numbers):
    """First number minus all the others."""
    return numbers[0] - sum(numbers[1:])


def multiply(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result


def divide(numbers):
    """First number divided by each of the others in turn."""
    result = numbers[0]
    for n in numbers[1:]:
        if n == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        result /= n
    return result


def run_add():
    print("The sum is:", add(read_numbers()))


def run_subtract():
    print("The difference is:", subtract(read_numbers()))


def run_multiply():
    print("The product is:", multiply(read_numbers()))


def run_divide():
    print("The quotient is:", divide(read_numbers()))


# ------------------------------------------------------- powers & logarithms
def square_root(x):
    if x < 0:
        raise ValueError("Square root is not defined for negative numbers.")
    return math.sqrt(x)


def power(base, exponent):
    try:
        return math.pow(base, exponent)
    except (ValueError, OverflowError) as exc:
        raise ValueError(f"Cannot compute this power: {exc}") from exc


def logarithm(x, base=None):
    """Natural log when base is None, otherwise log of x to the given base."""
    if x <= 0:
        raise ValueError("Logarithm is undefined for numbers <= 0.")
    if base is None:
        return math.log(x)
    if base <= 0 or base == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1.")
    return math.log(x, base)


def run_square_root():
    x = read_float("Enter your number: ")
    print("The square root is:", square_root(x))


def run_power():
    base = read_float("Enter your base: ")
    exponent = read_float("Enter your exponent: ")
    print("The result is:", power(base, exponent))


def run_logarithm():
    x = read_float("Enter your number: ")
    while True:
        raw = input("Enter your base (a number, or 'e'): ").strip().lower()
        if raw == "e":
            base = None
            break
        try:
            base = float(raw)
            break
        except ValueError:
            print("Invalid input. Please enter a number or 'e'.")
    print("The logarithm is:", logarithm(x, base))


# ------------------------------------------------------------- combinatorics
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return math.factorial(n)


def _check(n, r):
    if n < 0 or r < 0:
        raise ValueError("n and r must be non-negative.")
    if r > n:
        raise ValueError("r cannot be greater than n.")


def permutations(n, r):
    _check(n, r)
    return math.perm(n, r)


def combinations(n, r):
    _check(n, r)
    return math.comb(n, r)


def run_factorial():
    n = read_int("Enter a number: ")
    print(f"The factorial of {n} is {factorial(n)}.")


def run_perm_comb():
    n = read_int("Enter the total number of items (n): ")
    r = read_int("Enter the number of items to choose (r): ")
    print(f"Permutations (P({n}, {r})): {permutations(n, r)}")
    print(f"Combinations (C({n}, {r})): {combinations(n, r)}")
