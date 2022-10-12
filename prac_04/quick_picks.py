""""Quick Pick" Lottery Ticket Generator"""

from random import randint


MIN_NUMBER = 1
MAX_NUMBER = 45

number_of_quick_picks = int(input("How many quick picks? "))
for i in range(number_of_quick_picks):
    quick_pick = []
    for j in range(6):

