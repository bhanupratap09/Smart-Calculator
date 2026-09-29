"""Unit conversions and number-base conversions."""

from calculator.input_utils import read_float, read_int

# (menu title, source unit, [(target unit, conversion function), ...])
UNIT_CATEGORIES = [
    ("Length (meters to kilometers, miles, feet)", "meters", [
        ("kilometers", lambda v: v / 1000),
        ("miles", lambda v: v * 0.000621371),
        ("feet", lambda v: v * 3.28084)]),
    ("Weight (kilograms to grams, pounds, ounces)", "kilograms", [
        ("grams", lambda v: v * 1000),
        ("pounds", lambda v: v * 2.20462),
        ("ounces", lambda v: v * 35.274)]),
    ("Temperature (Celsius to Fahrenheit, Kelvin)", "degrees Celsius", [
        ("degrees Fahrenheit", lambda v: v * 9 / 5 + 32),
        ("kelvin", lambda v: v + 273.15)]),
    ("Pressure (Pascals to atmospheres, bar, psi)", "pascals", [
        ("atmospheres", lambda v: v / 101325),
        ("bar", lambda v: v / 100000),
        ("psi", lambda v: v / 6894.76)]),
    ("Time (seconds to minutes, hours, days)", "seconds", [
        ("minutes", lambda v: v / 60),
        ("hours", lambda v: v / 3600),
        ("days", lambda v: v / 86400)]),
    ("Energy (Joules to calories, kilowatt-hours)", "joules", [
        ("calories", lambda v: v / 4.184),
        ("kilowatt-hours", lambda v: v / 3600000)]),
]


def convert_units(category_index, value):
    """Return [(target_unit, converted_value), ...] for the chosen category."""
    _, _, targets = UNIT_CATEGORIES[category_index]
    return [(unit, func(value)) for unit, func in targets]


BASE_FORMATS = {2: "b", 8: "o", 16: "X"}
BASE_NAMES = {2: "binary", 8: "octal", 16: "hexadecimal"}


def decimal_to_base(number, base):
    return format(number, BASE_FORMATS[base])


def base_to_decimal(text, base):
    try:
        return int(text, base)
    except ValueError as exc:
        raise ValueError(f"Invalid {BASE_NAMES[base]} number.") from exc


def run_unit_conversion():
    print("Unit Conversion\nSelect a conversion type:")
    for i, (title, _, _) in enumerate(UNIT_CATEGORIES, start=1):
        print(f"{i}. {title}")
    index = read_int("Enter your choice (1-6): ", 1, len(UNIT_CATEGORIES)) - 1
    _, source_unit, _ = UNIT_CATEGORIES[index]
    value = read_float(f"Enter value in {source_unit}: ")
    for unit, result in convert_units(index, value):
        print(f"{value} {source_unit} is {result} {unit}.")


BASE_MENU = [
    ("Decimal to Binary", "from_decimal", 2),
    ("Decimal to Octal", "from_decimal", 8),
    ("Decimal to Hexadecimal", "from_decimal", 16),
    ("Binary to Decimal", "to_decimal", 2),
    ("Octal to Decimal", "to_decimal", 8),
    ("Hexadecimal to Decimal", "to_decimal", 16),
]


def run_base_conversion():
    print("Base Conversion\nSelect a conversion type:")
    for i, (title, _, _) in enumerate(BASE_MENU, start=1):
        print(f"{i}. {title}")
    _, direction, base = BASE_MENU[read_int("Enter your choice (1-6): ", 1, 6) - 1]
    if direction == "from_decimal":
        number = read_int("Enter a decimal number: ")
        print(f"{number} in {BASE_NAMES[base]} is {decimal_to_base(number, base)}.")
    else:
        while True:
            text = input(f"Enter a {BASE_NAMES[base]} number: ").strip()
            try:
                result = base_to_decimal(text, base)
                break
            except ValueError as exc:
                print(exc)
        print(f"{text} in decimal is {result}.")
