#this program is an advance scientific calculator which can perform various operations like addition, subtraction, multiplication, division, square root, power, logarithm, trigonometric functions and many more.
import math as mt
import numpy as np
import statistics as stats
def calculator():
    def re():
        r = input("Do you want to perform another operation? (y/n): ")
        if r.lower() == 'y':
            while True:
                calculator()
        elif r.lower() == 'n':
            print("Exiting the calculator. Goodbye!")
            return
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")
            re()
    print("Welcome to the Advanced Scientific Calculator!")
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Power")
    print("7. Logarithm")
    print("8. Trigonometric Functions")
    print("9. Inverse Trigonometric Functions")
    print("10. Quadratic Equation Solver")
    print("11. Matrix Operations")
    print("12. Inverse Matrix")
    print("13. Complex Number Operations")
    print("14. Factorial")
    print("15. Statistics (Mean, Median, Mode, Standard Deviation)")
    print("16. Permutations and Combinations")
    print("17. Unit conversion")
    print("18. Base conversion")
    print("19. Exit")
    while True:
        try:
            e = int(input("Enter your choice (1-19): "))
            break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 19.")
            continue
    if e == 1:
        while True:
            try:
                n = int(input("How many elements?: "))
                if n <= 0:
                    print("Please enter a positive integer.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a positive integer.")
        a = []
        for i in range(n):
            while True:
                try:
                    b = float(input("Enter your {}st element: ".format(i+1)))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            a.append(b)
        print("The sum is: ", sum(a))
        re()
    elif e == 2:
        while True:
            try:
                n = int(input("How many elements?: "))
                if n <= 0:
                    print("Please enter a positive integer.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a positive integer.")
        a = []
        for i in range(n):
            while True:
                try:
                    b = float(input("Enter your {}st element: ".format(i+1)))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            a.append(b)
        print("The difference is: ", a[0] - sum(a[1:]))
        re()
    elif e == 3:
        while True:
            try:
                n = int(input("How many elements?: "))
                if n <= 0:
                    print("Please enter a positive integer.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a positive integer.")
        a = []
        for i in range(n):
            while True:
                try:
                    b = float(input("Enter your {}st element: ".format(i+1)))
                    a.append(b)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        result = 1
        for i in a:
            result *= i
        print("The product is: ", result)
        re()
    elif e == 4:
        while True:
            try:
                n = int(input("How many elements?: "))
                if n <= 0:
                    print("Please enter a positive integer.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a positive integer.")
        a = []
        while True:
            try:
                r = float(input("Enter your first element: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        for i in range(n - 1):
            while True:
                try:
                    b = float(input("Enter your {}st element: ".format(i+2)))
                    a.append(b)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        for i in a:
            r /= i
        print("The quotient is: ", r)
        re()
    elif e == 5:
        while True:
            try:
                n = float(input("Enter your number: "))
                if n < 0:
                    print("Square root is not defined for negative numbers.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        print("The square root is: ", mt.sqrt(n))
        re()
    elif e == 6:
        while True:
            try:
                n = float(input("Enter your base: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        while True:
            try:
                m = float(input("Enter your exponent: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        print("The result is: ", mt.pow(n, m))
        re()
    elif e == 7:
        while True:
            try:
                n = float(input("Enter your number: "))
                if n <= 0:
                    print("Logarithm is undefined for the given inputs.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        while True:
            try:
                m = input("Enter your base: ")
                if m <= '0' or m == '1':
                    print("Logarithm is undefined for the given inputs.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid base.")
        if m == 'e':
            print("The logarithm is: ", mt.log(n))
        else:
            m = float(m)
            print("The logarithm is: ", mt.log(n,m))
        re()
    elif e == 8:
        print("Select a trigonometric function:")
        print("1. Sine")
        print("2. Cosine")
        print("3. Tangent")
        print("4. Cosecant")
        print("5. Secant")
        print("6. Cotangent")
        while True:
            try:
                f = int(input("Enter your choice (1-6): "))
                if f < 1 or f > 6:
                    print("Invalid input. Please enter a number between 1 and 6.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 6.")
        while True:
            n = input("Is ur angle in degrees or radians? (d/r): ")
            if n.lower() == 'd':
                while True:
                    try:
                        deg = float(input("Enter your angle in degrees: "))
                        rad = mt.radians(deg)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid angle in degrees.")
                break
            elif n.lower() == 'r':
                while True:
                    try:
                        rad = float(input("Enter your angle in radians: "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid angle in radians.")
                break
            else:
                print("Invalid input. Please enter 'd' for degrees or 'r' for radians.")
        if f == 1:
            print("The sine is: ", mt.sin(rad))
        elif f == 2:
            print("The cosine is: ", mt.cos(rad))
        elif f == 3:
            print("The tangent is: ", mt.tan(rad))
        elif f == 4:    
            if mt.sin(rad) == 0:
                print("Cosecant is undefined for the given angle.")
            else:
                print("The cosecant is: ", 1/mt.sin(rad))
        elif f == 5:
            if mt.cos(rad) == 0:
                print("Secant is undefined for the given angle.")
            else:
                print("The secant is: ", 1/mt.cos(rad))
        elif f == 6:
            if mt.tan(rad) == 0:
                print("Cotangent is undefined for the given angle.")
            else:
                print("The cotangent is: ", 1/mt.tan(rad))
        re()
    elif e == 9:
        print("Select an inverse trigonometric function:")
        print("1. Arcsine")
        print("2. Arccosine")
        print("3. Arctangent")
        print("4. Arccosecant")
        print("5. Arcsecant")
        print("6. Arccotangent")
        while True:
            try:
                g = int(input("Enter your choice (1-6): "))
                if g < 1 or g > 6:
                    print("Invalid input. Please enter a number between 1 and 6.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 6.")
        while True:
            try:
                n = float(input("Enter your number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        if g == 1:
            if n < -1 or n > 1:
                print("Arcsine is undefined for the given input.")
            else:
                print("The arcsine is: ", mt.degrees(mt.asin(n)))
        elif g == 2:
            if n < -1 or n > 1:
                print("Arccosine is undefined for the given input.")
            else:
                print("The arccosine is: ", mt.degrees(mt.acos(n)))
        elif g == 3:
            print("The arctangent is: ", mt.degrees(mt.atan(n)))
        elif g == 4:
            if n < -1 or n > 1:
                print("Arccosecant is undefined for the given input.")
            else:
                print("The arccosecant is: ", mt.degrees(mt.asin(1/n)))
        elif g == 5:
            if n < -1 or n > 1:
                print("Arcsecant is undefined for the given input.")
            else:
                print("The arcsecant is: ", mt.degrees(mt.acos(1/n)))
        elif g == 6:
            print("The arccotangent is: ", mt.degrees(mt.atan(1/n)))
        re()
    elif e == 10:
        print("Quadratic Equation Solver")
        print("The standard form of a quadratic equation is: ax² + bx + c = 0")
        while True:
            try:
                a = float(input("Enter the coefficient a: "))
                b = float(input("Enter the coefficient b: "))
                c = float(input("Enter the coefficient c: "))
                if a == 0:
                    print("Coefficient 'a' cannot be zero for a quadratic equation.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter valid numbers for coefficients.")
        d = b**2 - 4*a*c
        if d < 0:
            print("The equation has no real roots.")
            print("The complex roots are: ", (-b/(2*a)) + (mt.sqrt(-d)/(2*a))*1j, " and ", (-b/(2*a)) - (mt.sqrt(-d)/(2*a))*1j)
        elif d == 0:
            root = -b / (2*a)
            print("The equation has one real root: ", root)
        else:
            root1 = (-b + mt.sqrt(d)) / (2*a)
            root2 = (-b - mt.sqrt(d)) / (2*a)
            print("The equation has two real roots: ", root1, " and ", root2)
        re()
    elif e == 11:
        print("Matrix Operations")
        print("Select an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        while True:
            try:
                h = int(input("Enter your choice (1-3): "))
                if h < 1 or h > 3:
                    print("Invalid input. Please enter a number between 1 and 3.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 3.")
        if h == 1:
            while True:
                try:
                    r1 = int(input("Enter the number of rows for the first matrix: "))
                    c1 = int(input("Enter the number of columns for the first matrix: "))
                    r2 = int(input("Enter the number of rows for the second matrix: "))
                    c2 = int(input("Enter the number of columns for the second matrix: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter valid integers for dimensions.")
            if r1 != r2 or c1 != c2:
                print("Matrix addition is not possible with the given dimensions.")
            else:
                print("Enter the elements of the first matrix:")
                A = np.zeros((r1, c1))
                for i in range(r1):
                    for j in range(c1):
                        A[i][j] = float(input(f"Element [{i+1}][{j+1}]: "))
                print("Enter the elements of the second matrix:")
                B = np.zeros((r2, c2))
                for i in range(r2):
                    for j in range(c2):
                        B[i][j] = float(input(f"Element [{i+1}][{j+1}]: "))
                C = A + B
                print("The result of matrix addition is:")
                print(C)
        elif h == 2:   
            while True:
                try:
                    r1 = int(input("Enter the number of rows for the first matrix: "))
                    c1 = int(input("Enter the number of columns for the first matrix: "))
                    r2 = int(input("Enter the number of rows for the second matrix: "))
                    c2 = int(input("Enter the number of columns for the second matrix: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter valid integers for dimensions.")
            if r1 != r2 or c1 != c2:
                print("Matrix subtraction is not possible with the given dimensions.")
            else:
                print("Enter the elements of the first matrix:")
                A = np.zeros((r1, c1))
                for i in range(r1):
                    for j in range(c1):
                        A[i][j] = float(input(f"Element [{i+1}][{j+1}]: "))
                print("Enter the elements of the second matrix:")
                B = np.zeros((r2, c2))
                for i in range(r2):
                    for j in range(c2):
                        B[i][j] = float(input(f"Element [{i+1}][{j+1}]: "))
                C = A - B
                print("The result of matrix subtraction is:")
                print(C)
        elif h == 3:
            while True:
                try:
                    r1 = int(input("Enter the number of rows for the first matrix: "))
                    c1 = int(input("Enter the number of columns for the first matrix: "))
                    r2 = int(input("Enter the number of rows for the second matrix: "))
                    c2 = int(input("Enter the number of columns for the second matrix: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter valid integers for dimensions.")
            if c1 != r2:
                print("Matrix multiplication is not possible with the given dimensions.")
            else:
                print("Enter the elements of the first matrix:")
                A = np.zeros((r1, c1))
                for i in range(r1):
                    for j in range(c1):
                        A[i][j] = float(input(f"Element [{i+1}][{j+1}]: "))
                print("Enter the elements of the second matrix:")
                B = np.zeros((r2, c2))
                for i in range(r2):
                    for j in range(c2):
                        B[i][j] = float(input(f"Element [{i+1}][{j+1}]: "))
                C = np.dot(A, B)
                print("The result of matrix multiplication is:")
                print(C)
        re()
    elif e == 12:
        print("Inverse Matrix")
        while True:
            try:
                r = int(input("Enter the number of rows for the matrix: "))
                c = int(input("Enter the number of columns for the matrix: "))
                break
            except ValueError:
                print("Invalid input. Please enter valid integers for dimensions.")
        if r != c:
            print("Inverse is not possible for non-square matrices.")
        else:
            print("Enter the elements of the matrix:")
            A = np.zeros((r, c))
            for i in range(r):
                for j in range(c):
                    A[i][j] = float(input(f"Element [{i+1}][{j+1}]: "))
            try:
                A_inv = np.linalg.inv(A)
                print("The inverse of the matrix is:")
                print(A_inv)
            except np.linalg.LinAlgError:
                print("The matrix is singular and does not have an inverse.")
        re()
    elif e == 13:
        print("Complex Number Operations")
        print("Select an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        while True:
            try:
                i = int(input("Enter your choice (1-4): "))
                if i < 1 or i > 4:
                    print("Invalid input. Please enter a number between 1 and 4.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")
        if i in [1, 2, 3, 4]:
            while True:
                try:
                    a_real = float(input("Enter the real part of the first complex number: "))
                    a_imag = float(input("Enter the imaginary part of the first complex number: "))
                    b_real = float(input("Enter the real part of the second complex number: "))
                    b_imag = float(input("Enter the imaginary part of the second complex number: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter valid numbers for real and imaginary parts.")
            a = complex(a_real, a_imag)
            b = complex(b_real, b_imag)
            if i == 1:
                result = a + b
                print(f"The result of addition is: {result}")
            elif i == 2:
                result = a - b
                print(f"The result of subtraction is: {result}")
            elif i == 3:
                result = a * b
                print(f"The result of multiplication is: {result}")
            elif i == 4:
                if b == 0:
                    print("Division by zero is not allowed.")
                else:
                    result = a / b
                    print(f"The result of division is: {result}")
        re()
    elif e == 14:
        print("Factorial")
        while True:
            try:
                n = int(input("Enter a number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        if n == 0:
            print("The factorial of 0 is 1.")
        else:
            result = 1
            for i in range(1, n + 1):
                result *= i
            print(f"The factorial of {n} is {result}.")
        re()
    elif e == 15:
        print("Statistics (Mean, Median, Mode, Standard Deviation)")
        while True:
            try:
                n = int(input("How many elements?: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        elements = []
        for i in range(n):
            while True:
                try:
                    elem = float(input(f"Enter element {i + 1}: "))
                    elements.append(elem)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        mean = sum(elements) / len(elements)
        print(f"Mean: {mean}")
        median = np.median(elements)
        print(f"Median: {median}")
        try:
            mode = stats.mode(elements)
            print(f"Mode: {mode}")
        except stats.StatisticsError:
            print("Mode: No unique mode found.")
        std_dev = np.std(elements)
        print(f"Standard Deviation: {std_dev}")
        re()
    elif e == 16:
        print("Permutations and Combinations")
        while True:
            try:
                n = int(input("Enter the total number of items (n): "))
                r = int(input("Enter the number of items to choose (r): "))
                break
            except ValueError:
                print("Invalid input. Please enter valid integers.")
        if r > n:
            print("r cannot be greater than n.")
        else:
            permutations = mt.factorial(n) / mt.factorial(n - r)
            combinations = mt.factorial(n) / (mt.factorial(r) * mt.factorial(n - r))
            print(f"Permutations (P({n}, {r})): {int(permutations)}")
            print(f"Combinations (C({n}, {r})): {int(combinations)}")
        re()
    elif e == 17:
        print("Unit Conversion")
        print("Select a conversion type:")
        print("1. Length (meters to kilometers, miles, feet)")
        print("2. Weight (kilograms to grams, pounds, ounces)")
        print("3. Temperature (Celsius to Fahrenheit, Kelvin)")
        print("4. Pressure (Pascals to atmospheres, bar, psi)")
        print("5. Time (seconds to minutes, hours, days)")
        print("6. Energy (Joules to calories, kilowatt-hours)")
        while True:
            try:
                j = int(input("Enter your choice (1-6): "))
                if j < 1 or j > 6:
                    print("Invalid input. Please enter a number between 1 and 6.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 6.")
        if j == 1:
            while True:
                try:
                    meters = float(input("Enter length in meters: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            print(f"{meters} meters is {meters / 1000} kilometers.")
            print(f"{meters} meters is {meters * 0.000621371} miles.")
            print(f"{meters} meters is {meters * 3.28084} feet.")
        elif j == 2:
            while True:
                try:
                    kilograms = float(input("Enter weight in kilograms: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            print(f"{kilograms} kilograms is {kilograms * 1000} grams.")
            print(f"{kilograms} kilograms is {kilograms * 2.20462} pounds.")
            print(f"{kilograms} kilograms is {kilograms * 35.274} ounces.")
        elif j == 3:
            while True:
                try:
                    celsius = float(input("Enter temperature in Celsius: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            print(f"{celsius}°C is {(celsius * 9/5) + 32}°F.")
            print(f"{celsius}°C is {celsius + 273.15} K.")
        elif j == 4:
            while True:
                try:
                    pascals = float(input("Enter pressure in Pascals: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            print(f"{pascals} Pascals is {pascals / 101325} atmospheres.")
            print(f"{pascals} Pascals is {pascals / 100000} bar.")
            print(f"{pascals} Pascals is {pascals / 6894.76} psi.")
        elif j == 5:    
            while True:
                try:
                    seconds = float(input("Enter time in seconds: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            print(f"{seconds} seconds is {seconds / 60} minutes.")
            print(f"{seconds} seconds is {seconds / 3600} hours.")
            print(f"{seconds} seconds is {seconds / 86400} days.")
        elif j == 6:
            while True:
                try:
                    joules = float(input("Enter energy in Joules: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            print(f"{joules} Joules is {joules / 4.184} calories.")
            print(f"{joules} Joules is {joules / 3600000} kilowatt-hours.")
        re()
    elif e == 18:
        print("Base Conversion")
        print("Select a conversion type:")
        print("1. Decimal to Binary")
        print("2. Decimal to Octal")
        print("3. Decimal to Hexadecimal")
        print("4. Binary to Decimal")
        print("5. Octal to Decimal")
        print("6. Hexadecimal to Decimal")
        while True:
            try:
                k = int(input("Enter your choice (1-6): "))
                if k < 1 or k > 6:
                    print("Invalid input. Please enter a number between 1 and 6.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 6.")  
        if k == 1:
            while True:
                try:
                    decimal = int(input("Enter a decimal number: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
            print(f"{decimal} in binary is {bin(decimal)[2:]}.")
        elif k == 2:
            while True:
                try:
                    decimal = int(input("Enter a decimal number: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
            print(f"{decimal} in octal is {oct(decimal)[2:]}.")
        elif k == 3:
            while True:
                try:
                    decimal = int(input("Enter a decimal number: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
            print(f"{decimal} in hexadecimal is {hex(decimal)[2:].upper()}.")
        elif k == 4:
            while True:
                try:
                    binary = input("Enter a binary number: ")
                    decimal = int(binary, 2)
                    break
                except ValueError:
                    print("Invalid binary number.")
            print(f"{binary} in decimal is {decimal}.")
        elif k == 5:
            while True:
                try:
                    octal = input("Enter an octal number: ")
                    decimal = int(octal, 8)
                    break
                except ValueError:
                    print("Invalid octal number.")
            print(f"{octal} in decimal is {decimal}.")
        elif k == 6:
            while True:
                try:
                    hexadecimal = input("Enter a hexadecimal number: ")
                    decimal = int(hexadecimal, 16)
                    break
                except ValueError:
                    print("Invalid hexadecimal number.")
            print(f"{hexadecimal} in decimal is {decimal}.")
    else:
        print("Exiting the calculator. Goodbye!")
calculator()
