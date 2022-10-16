"""Hex colours using dictionaries"""

COLOUR_TO_HEXADECIMAL = {"Aqua": "#00ffff", "Beige": "#f5f5dc", "Chestnut": "#954535", "Denim": "#1560bd",
                         "Emerald": "#50c878", "Frostbite": "#e936a7", "Ginger": "#b06500", "HotPink": "#ff69b4",
                         "Indigo": "#4b0082", "Jasmine": "#f8de7e"}

colour_name = input("Enter colour name: ").title()
while colour_name != "":
    try:
        print(COLOUR_TO_HEXADECIMAL[colour_name])
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").title()
