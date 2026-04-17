import math


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ValueError("Division by zero is not allowed.")
    return x / y


def power(x, y):
    return x ** y


def square_root(x):
    if x < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    return math.sqrt(x)


def logarithm(x, base=10):
    if x <= 0:
        raise ValueError("Logarithm is only defined for positive numbers.")
    if base <= 0 or base == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1.")
    return math.log(x, base)


def natural_log(x):
    if x <= 0:
        raise ValueError("Natural logarithm is only defined for positive numbers.")
    return math.log(x)


def sine(x, degrees=True):
    angle = math.radians(x) if degrees else x
    return math.sin(angle)


def cosine(x, degrees=True):
    angle = math.radians(x) if degrees else x
    return math.cos(angle)


def tangent(x, degrees=True):
    angle = math.radians(x) if degrees else x
    result = math.tan(angle)
    if math.isclose(math.cos(angle), 0.0, abs_tol=1e-12):
        raise ValueError("Tangent is undefined for this angle.")
    return result


def inverse_sine(x, degrees=True):
    if x < -1 or x > 1:
        raise ValueError("Arcsine input must be between -1 and 1.")
    result = math.asin(x)
    return math.degrees(result) if degrees else result


def inverse_cosine(x, degrees=True):
    if x < -1 or x > 1:
        raise ValueError("Arccosine input must be between -1 and 1.")
    result = math.acos(x)
    return math.degrees(result) if degrees else result


def inverse_tangent(x, degrees=True):
    result = math.atan(x)
    return math.degrees(result) if degrees else result


def factorial(x):
    if x < 0 or int(x) != x:
        raise ValueError("Factorial is only defined for non-negative integers.")
    return math.factorial(int(x))


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid whole number.")


def ask_angle_mode():
    while True:
        mode = input("Use degrees or radians? [d/r]: ").strip().lower()
        if mode in {"d", "deg", "degrees"}:
            return True
        if mode in {"r", "rad", "radians"}:
            return False
        print("Please type d for degrees or r for radians.")


def show_menu():
    print("\n=== Scientific Calculator ===")
    print(" 1. Add")
    print(" 2. Subtract")
    print(" 3. Multiply")
    print(" 4. Divide")
    print(" 5. Power")
    print(" 6. Square Root")
    print(" 7. Logarithm (base 10)")
    print(" 8. Natural Log")
    print(" 9. Sine")
    print("10. Cosine")
    print("11. Tangent")
    print("12. Arcsine")
    print("13. Arccosine")
    print("14. Arctangent")
    print("15. Factorial")
    print("16. Exit")


def main():
    print("Welcome to the Scientific Calculator!")

    while True:
        show_menu()
        choice = input("Select an operation (1-16): ").strip()

        try:
            if choice == "1":
                x = get_float("Enter the first number: ")
                y = get_float("Enter the second number: ")
                print(f"Result: {add(x, y)}")

            elif choice == "2":
                x = get_float("Enter the first number: ")
                y = get_float("Enter the second number: ")
                print(f"Result: {subtract(x, y)}")

            elif choice == "3":
                x = get_float("Enter the first number: ")
                y = get_float("Enter the second number: ")
                print(f"Result: {multiply(x, y)}")

            elif choice == "4":
                x = get_float("Enter the first number: ")
                y = get_float("Enter the second number: ")
                print(f"Result: {divide(x, y)}")

            elif choice == "5":
                x = get_float("Enter the base: ")
                y = get_float("Enter the exponent: ")
                print(f"Result: {power(x, y)}")

            elif choice == "6":
                x = get_float("Enter a number: ")
                print(f"Result: {square_root(x)}")

            elif choice == "7":
                x = get_float("Enter a number: ")
                print(f"Result: {logarithm(x)}")

            elif choice == "8":
                x = get_float("Enter a number: ")
                print(f"Result: {natural_log(x)}")

            elif choice == "9":
                x = get_float("Enter the angle/value: ")
                degrees = ask_angle_mode()
                print(f"Result: {sine(x, degrees)}")

            elif choice == "10":
                x = get_float("Enter the angle/value: ")
                degrees = ask_angle_mode()
                print(f"Result: {cosine(x, degrees)}")

            elif choice == "11":
                x = get_float("Enter the angle/value: ")
                degrees = ask_angle_mode()
                print(f"Result: {tangent(x, degrees)}")

            elif choice == "12":
                x = get_float("Enter a value between -1 and 1: ")
                degrees = ask_angle_mode()
                print(f"Result: {inverse_sine(x, degrees)}")

            elif choice == "13":
                x = get_float("Enter a value between -1 and 1: ")
                degrees = ask_angle_mode()
                print(f"Result: {inverse_cosine(x, degrees)}")

            elif choice == "14":
                x = get_float("Enter a number: ")
                degrees = ask_angle_mode()
                print(f"Result: {inverse_tangent(x, degrees)}")

            elif choice == "15":
                x = get_float("Enter a non-negative whole number: ")
                print(f"Result: {factorial(x)}")

            elif choice == "16":
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please select a number from 1 to 16.")

        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()