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
            for i in range(x, y + 1):
                if i % 2 == 0:
                    print(i, end=" ")
        elif choice == "O":
            for i in range(x, y + 1):
                if i % 2 == 1:
                    print(i, end=" ")
        elif choice == "S":
            for i in range(x, y + 1):
                print(i**2, end=" ")
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("See you next time!")


main()
