"""Main menu and control loop.

Replaces the original recursive re() function with a plain while loop,
so long sessions can never hit Python's recursion limit.
"""

from calculator import advanced_math, basic_math, conversions, matrix_ops, trigonometry
from calculator.input_utils import read_int, read_yes_no

MENU_ITEMS = [
    ("Addition", basic_math.run_add),
    ("Subtraction", basic_math.run_subtract),
    ("Multiplication", basic_math.run_multiply),
    ("Division", basic_math.run_divide),
    ("Square Root", basic_math.run_square_root),
    ("Power", basic_math.run_power),
    ("Logarithm", basic_math.run_logarithm),
    ("Trigonometric Functions", trigonometry.run_trig),
    ("Inverse Trigonometric Functions", trigonometry.run_inverse_trig),
    ("Quadratic Equation Solver", advanced_math.run_quadratic),
    ("Matrix Operations", matrix_ops.run_matrix_operations),
    ("Inverse Matrix", matrix_ops.run_inverse),
    ("Complex Number Operations", advanced_math.run_complex),
    ("Factorial", basic_math.run_factorial),
    ("Statistics (Mean, Median, Mode, Standard Deviation)", advanced_math.run_statistics),
    ("Permutations and Combinations", basic_math.run_perm_comb),
    ("Unit conversion", conversions.run_unit_conversion),
    ("Base conversion", conversions.run_base_conversion),
]
EXIT_CHOICE = len(MENU_ITEMS) + 1


def show_menu():
    print("\nWelcome to the Advanced Scientific Calculator!")
    print("Select an operation:")
    for i, (label, _) in enumerate(MENU_ITEMS, start=1):
        print(f"{i}. {label}")
    print(f"{EXIT_CHOICE}. Exit")


def main():
    while True:
        show_menu()
        choice = read_int(f"Enter your choice (1-{EXIT_CHOICE}): ", 1, EXIT_CHOICE)
        if choice == EXIT_CHOICE:
            break
        _, handler = MENU_ITEMS[choice - 1]
        try:
            handler()
        except (ValueError, ZeroDivisionError, OverflowError) as exc:
            print(f"Error: {exc}")
        if not read_yes_no("Do you want to perform another operation? (y/n): "):
            break
    print("Exiting the calculator. Goodbye!")
