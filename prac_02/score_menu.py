"""

"""

import random

MENU = "E - Enter score\nP - Print score\nS - Print stars\nQ - Quit"


def main():
    """Program"""
    score = 0
    result = ""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "E":
            score = int(input("Enter score: "))
            while score < 0 or score > 100:
                print("Invalid score")
                score = int(input("Enter score: "))
            result = determine_result(score)
        elif choice == "P":
            print(f"{score} is {result}")
        elif choice == "S":
            print_stars(score)
        else:
            print(f"\"{choice}\" invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("bye")


def print_stars(score):
    """Display name with length of hyphens."""
    print('*' * score)


def determine_result(score):
    """Check if score is valid and determine result"""
    if score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


main()
