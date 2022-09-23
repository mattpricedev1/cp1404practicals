"""
User enters a number of items and the price of each different item
Computes and displays the total price of those items
If the total price is over $100, then a 10% discount is applied to the total before the amount is displayed
"""
DISCOUNT = 0.9

total_price = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for item in range(number_of_items):
    item_price = float(input("Price of item: "))
    total_price += item_price
if total_price > 100:
    total_price *= DISCOUNT
print(f"Total price for 3 items is ${total_price:.2f}")
