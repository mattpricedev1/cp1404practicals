"""
Wimbledon program
"""

from operator import itemgetter

CSV_FILE = "wimbledon.csv"
MENU = "(D) - Display Wimbledon champions and countries that have won Wimbledon\n" \
       "(S) - Sort the players by who has won the most championships\n" \
       "(L) - Display longest game played"
COUNTRY_INDEX = 1
PLAYER_INDEX = 2


def main():
    """Get csv file as input and process records for output"""
    records = get_records(CSV_FILE)
    player_to_count, countries = process_records(records)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "D":
            display_records(player_to_count, countries)
        elif choice == "S":
            sort_players(player_to_count)
        elif choice == "L":
            process_game_records(records)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using the Wimbledon program")


def get_records(csv_file):
    """Retrieve records from csv file and append to list"""
    records = []
    with open(csv_file, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # skip first line
        for line in in_file:
            attribute = line.strip().split(",")  # remove commas and separate each attribute
            records.append(attribute)
        return records


def process_records(records):
    """Add player and count to dictionary and country to set list"""
    player_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[COUNTRY_INDEX])  # add new country to set list
        try:
            player_to_count[record[PLAYER_INDEX]] += 1
        except KeyError:
            player_to_count[record[PLAYER_INDEX]] = 1
    return player_to_count, countries


def display_records(player_to_count, countries):
    """Display player names and victories with countries in alphabetical order"""
    print("Wimbledon Champions:")
    for name, count in player_to_count.items():
        print(name, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(country for country in sorted(countries)))


def sort_players(player_to_count):
    """Sort players from most to least championships won."""
    sorted_players = sorted(player_to_count.items(), key=itemgetter(1), reverse=True)
    for player in sorted_players:
        print(player[0], player[1])


def process_game_records(records):
    # create list comprehension of all games played
    games = [record[5:] for record in records]
    for i, game in enumerate(games):
        print(f"Game {i + 1:<2} ({records[i][2]} vs {records[i][4]}) -\t{game}")


main()
