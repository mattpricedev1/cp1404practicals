"""
Wimbledon program
"""

CSV_FILE = "wimbledon.csv"
COUNTRY_INDEX = 1
PLAYER_INDEX = 2


def main():
    """Get csv file as input and process records for output"""
    records = get_records(CSV_FILE)
    player_to_count, countries = process_records(records)
    display_records(player_to_count, countries)


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
    print("\nThese 12 countries have won Wimbledon:")
    print(", ".join(country for country in sorted(countries)))


main()
