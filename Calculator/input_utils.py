"""Shared, validated console input helpers.

Every prompt loops until the user gives valid input, so no other module
needs its own try/except around input().
"""


def read_int(prompt, min_value=None, max_value=None):
    """Ask for a whole number, optionally within [min_value, max_value]."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue
        if min_value is not None and value < min_value:
            print(f"Please enter a number that is at least {min_value}.")
            continue
        if max_value is not None and value > max_value:
            print(f"Please enter a number that is at most {max_value}.")
            continue
        return value


def read_float(prompt):
    """Ask for any real number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def read_yes_no(prompt):
    """Ask a y/n question; returns True for yes, False for no."""
    while True:
        answer = input(prompt).strip().lower()
        if answer == "y":
            return True
        if answer == "n":
            return False
        print("Invalid input. Please enter 'y' for yes or 'n' for no.")


def read_numbers(min_count=1):
    """Ask how many numbers, then read that many floats into a list."""
    count = read_int("How many elements?: ", min_value=min_count)
    return [read_float(f"Enter element {i + 1}: ") for i in range(count)]
