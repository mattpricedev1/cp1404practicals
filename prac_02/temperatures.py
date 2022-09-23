"""
Using functions to convert celsius to fahrenheit and vice versa.
"""

MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit"


def main():
    """Program to convert celsius to fahrenheit and vice versa"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit"""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def convert_fahrenheit_to_celsius(fahrenheit):
    """Converts fahrenheit to celsius"""
    celsius = 5 / 9.0 * (fahrenheit - 32)
    return celsius


main()
