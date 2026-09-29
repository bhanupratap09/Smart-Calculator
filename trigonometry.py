"""Trigonometric and inverse trigonometric functions."""

import math

from calculator.input_utils import read_float, read_int

EPS = 1e-12  # treats floating-point noise like sin(pi) ~ 1e-16 as zero


def sine(r):
    return math.sin(r)


def cosine(r):
    return math.cos(r)


def tangent(r):
    return math.tan(r)


def cosecant(r):
    s = math.sin(r)
    if abs(s) < EPS:
        raise ValueError("Cosecant is undefined for the given angle.")
    return 1 / s


def secant(r):
    c = math.cos(r)
    if abs(c) < EPS:
        raise ValueError("Secant is undefined for the given angle.")
    return 1 / c


def cotangent(r):
    s = math.sin(r)
    if abs(s) < EPS:
        raise ValueError("Cotangent is undefined for the given angle.")
    return math.cos(r) / s


def arcsine(x):
    if not -1 <= x <= 1:
        raise ValueError("Arcsine is undefined for inputs outside [-1, 1].")
    return math.degrees(math.asin(x))


def arccosine(x):
    if not -1 <= x <= 1:
        raise ValueError("Arccosine is undefined for inputs outside [-1, 1].")
    return math.degrees(math.acos(x))


def arctangent(x):
    return math.degrees(math.atan(x))


def arccosecant(x):
    if abs(x) < 1:
        raise ValueError("Arccosecant is undefined for |x| < 1.")
    return math.degrees(math.asin(1 / x))


def arcsecant(x):
    if abs(x) < 1:
        raise ValueError("Arcsecant is undefined for |x| < 1.")
    return math.degrees(math.acos(1 / x))


def arccotangent(x):
    if x == 0:
        return 90.0
    return math.degrees(math.atan(1 / x))


TRIG_FUNCTIONS = [
    ("Sine", sine), ("Cosine", cosine), ("Tangent", tangent),
    ("Cosecant", cosecant), ("Secant", secant), ("Cotangent", cotangent),
]

INVERSE_FUNCTIONS = [
    ("Arcsine", arcsine), ("Arccosine", arccosine), ("Arctangent", arctangent),
    ("Arccosecant", arccosecant), ("Arcsecant", arcsecant),
    ("Arccotangent", arccotangent),
]


def _choose(options):
    for i, (name, _) in enumerate(options, start=1):
        print(f"{i}. {name}")
    return options[read_int(f"Enter your choice (1-{len(options)}): ", 1, len(options)) - 1]


def run_trig():
    print("Select a trigonometric function:")
    name, func = _choose(TRIG_FUNCTIONS)
    while True:
        unit = input("Is your angle in degrees or radians? (d/r): ").strip().lower()
        if unit in ("d", "r"):
            break
        print("Invalid input. Please enter 'd' for degrees or 'r' for radians.")
    angle = read_float("Enter your angle: ")
    radians = math.radians(angle) if unit == "d" else angle
    print(f"The {name.lower()} is:", func(radians))


def run_inverse_trig():
    print("Select an inverse trigonometric function:")
    name, func = _choose(INVERSE_FUNCTIONS)
    x = read_float("Enter your number: ")
    print(f"The {name.lower()} (in degrees) is:", func(x))
