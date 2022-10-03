"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? Entering a string such as "blah"
2. When will a ZeroDivisionError occur? When a number less than or equal to zero is entered.
3. Could you change the code to avoid the possibility of a ZeroDivisionError? Yes, by using a while loop.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator <= 0:
        print("Denominator must be greater than zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
