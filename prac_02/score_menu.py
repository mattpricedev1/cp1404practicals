"""
Similar to Lecture 2 dothisnow.py, program with main menu.
"""

MENU = "E - Enter score\nP - Print score\nS - Print stars\nQ - Quit"


def main():
    """Program with main menu to get a user score and determine result"""
    score = 0
    result = ""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "E":
            score = get_valid_score()
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


def get_valid_score():
    """Check if score meets the min/max condition"""
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


def print_stars(score):
    """Display score with length of stars"""
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
