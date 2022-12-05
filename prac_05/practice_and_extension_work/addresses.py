"""Name and address lookup program using a dictionary."""

MENU = "(E) - Enter a new name & address\n" \
       "(C) - Change an address for an existing entry\n" \
       "(D) - Display the address for a name you choose\n" \
       "(Q) - Quit"


def main():
    """Display main menu for address lookup program."""
    name_to_address = {"Matthew": "32/157-159 Stuart Dr, Wulguru, 4811",
                       "Michael": "24 Cockatoo Cct, Douglas, 4814"}
    print_addresses(name_to_address)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "E":
            add_address(name_to_address)
        elif choice == "C":
            change_address(name_to_address)
        elif choice == "D":
            display_address(name_to_address)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print_addresses(name_to_address)
    print("Thank you using address lookup")


def print_addresses(name_to_address):
    """Display formatted version of the addresses."""
    max_length = max(len(name) for name in list(name_to_address.keys()))
    for name, address in name_to_address.items():
        print(f"{name:{max_length}} -\t{address}")


def add_address(address_book):
    """Add a new address."""
    new_name = input("Enter a name: ")
    new_address = input("Enter an address: ")
    address_book[new_name] = new_address


def change_address(address_book):
    """Change the address of the chosen name."""
    name = input("Which name would you like to change the address of? ").title()
    while name not in address_book:
        print("Name does not exist in address book. Please try again.")
        name = input("Which name would you like to change the address of? ").title()
    new_address = input("What is the new address? ")
    address_book[name] = new_address


def display_address(address_book):
    """Display the address of the chosen name."""
    name = input("Please enter the name of the person you want to see the address of: ").title()
    try:
        print(f"The address is: {address_book[name]}")
    except KeyError:
        print("No such name in dictionary")


if __name__ == '__main__':
    main()
