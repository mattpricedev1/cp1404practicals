"""
Do-from-scratch Exercises
Taxi Simulator program

while choice is not q (need a menu)
    choose from list of available taxis
    choose how far they want to drive
    display trip cost and add it to bill

requires list of taxi objects
    taxis = [Taxi(), SilverServiceTaxi(), ...]

call the drive() method on the chosen object within the list

use a variable called 'current_taxi' to store a taxi object
when the user chooses a taxi to avoid driving nothing at the
start of the program
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose, d)rive"


def main():
    """Main menu of Taxi Simulator program."""
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print(MENU)
    choice = input(">>> ")
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice: ")
        elif choice == "d":
            if current_taxi:
                current_taxi.start_fare()
                distance_to_drive = float(input("Drive how far? "))
                current_taxi.drive(distance_to_drive)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
        else:
            print("Invalid option")
    for taxi in taxis:
        print(taxi)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


if __name__ == "__main__":
    main()
