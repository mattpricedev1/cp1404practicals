"""Menu-driven number sequence program"""

MENU = "(E)ven numbers from x to y\n(O)dd numbers from x to y\n(S)quares from x to y" \
       "(Q)uit"


def main():
    print("Number Sequence Generator")
    x = int(input("Enter x value: "))
    y = int(input("Enter y value: "))
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "E":
            pass
        elif choice == "O":
            pass
        elif choice == "S":
            pass
        else:
            "Invalid choice"
        print(MENU)
        choice = input(">>> ").upper()
    print("See you next time!")


main()
