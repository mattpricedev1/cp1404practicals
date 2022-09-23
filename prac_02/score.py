"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

from random import randint


def main():
    """Program for getting a result based off of user score"""
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)


def determine_result(score):
    """Check if score is valid and determine result"""
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    if score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


def get_random_score():
    """Randomly generate a score and print result"""
    score = randint(1, 100)
    result = determine_result(score)
    print(score, result)


get_random_score()
main()
