CSV_FILE = "wimbledon.csv"


def main():
    records = get_records(CSV_FILE)
    print(records)


def get_records(csv_file):
    records = []
    with open(csv_file, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            row = line.strip().split(",")
            records.append(row)
        return records


main()
