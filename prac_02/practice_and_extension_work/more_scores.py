"""More scores program."""

from random import randint


def main():
    """Get number of scores and generate random scores in range of n."""
    number_of_scores = int(input("How many scores? "))
    for number_of_scores in range(number_of_scores):
        score = randint(0, 100)
        result = determine_result(score)
        print(result)


def determine_result(score):
    """Check if score is valid and determine result."""
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    if score >= 90:
        result = f"{score} is Excellent"
    elif score >= 50:
        result = f"{score} is Passable"
    else:
        result = f"{score} is Bad"
    return result


if __name__ == "__main__":
    main()
