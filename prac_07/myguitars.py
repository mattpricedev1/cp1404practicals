"""More Guitars!"""

from guitar import Guitar

CSV_FILE = "guitars.csv"


def main():
    guitars = load_guitars(CSV_FILE)
    guitars.sort()
    print(guitars)


def load_guitars(csv_file):
    guitars = []
    with open(csv_file, "r", encoding="utf-8-sig") as in_file:
        for row in in_file:
            row = row.strip().split(",")
            guitar = Guitar(row[0], row[1], row[2])
            guitars.append(guitar)
    return guitars


if __name__ == "__main__":
    main()
