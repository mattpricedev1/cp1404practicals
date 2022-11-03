from guitar import Guitar


def main():
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.\n")
        name = input("Name: ")

    # test Guitar objects
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.90))
    guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))

    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth $ {guitar.cost:>8.2f}")


main()
