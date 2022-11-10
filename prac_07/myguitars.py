"""More Guitars!"""

from guitar import Guitar

CSV_FILE = "guitars.csv"


def main():
    guitars = load_guitars(CSV_FILE)
    for guitar in guitars:
        print(guitar)
    print("Add guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.\n")
        name = input("Name: ")
    save_guitars(CSV_FILE, guitars)


def load_guitars(csv_file):
    guitars = []
    with open(csv_file, "r", encoding="utf-8-sig") as in_file:
        for row in in_file:
            row = row.strip().split(",")
            guitar = Guitar(row[0], row[1], row[2])
            guitars.append(guitar)
    return guitars


def save_guitars(csv_file, guitars):
    with open(csv_file, "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


if __name__ == "__main__":
    main()
