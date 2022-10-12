""""Quick Pick" Lottery Ticket Generator"""

from random import randint

NUMBERS_PER_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

number_of_quick_picks = int(input("How many quick picks? "))
for i in range(number_of_quick_picks):
    quick_pick = []
    for j in range(NUMBERS_PER_LINE):
        number = randint(MIN_NUMBER, MAX_NUMBER)
        # if random number already exists, new number is generated
        while number in quick_pick:
            number = randint(MIN_NUMBER, MAX_NUMBER)
        quick_pick.append(number)
    quick_pick.sort()
    print(" ".join(f"{number:2}" for number in quick_pick))
