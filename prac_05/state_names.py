"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland",
                "NSW": "New South Wales",
                "SA": "South Australia",
                "NT": "Northern Territory",
                "WA": "Western Australia",
                "ACT": "Australian Capital Territory",
                "VIC": "Victoria",
                "TAS": "Tasmania"}

print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(f"{state_code:3} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

for state_code, state in CODE_TO_NAME.items():
    print(f"{state_code:3} is {state}")
