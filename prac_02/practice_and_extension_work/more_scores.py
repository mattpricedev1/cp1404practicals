"""More scores program."""


def main():
    """..."""


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


if __name__ == "__main__":
    main()
