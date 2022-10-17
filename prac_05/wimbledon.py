CSV_FILE = "wimbledon.csv"


def main():
    records = get_records(CSV_FILE)
    player_to_count, countries = process_records(records)
    display_records(player_to_count, countries)


def get_records(csv_file):
    records = []
    with open(csv_file, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # skip first line
        for line in in_file:
            attribute = line.strip().split(",")  # remove commas and separate attributes
            records.append(attribute)
        return records


def process_records(records):
    player_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[1])
        try:
            player_to_count[record[2]] += 1
        except KeyError:
            player_to_count[record[2]] = 1
    return player_to_count, countries


def display_records(player_to_count, countries):
    print("Wimbledon Champions:")
    for name, count in player_to_count.items():
        print(name, count)
    print(", ".join(country for country in sorted(countries)))


main()
