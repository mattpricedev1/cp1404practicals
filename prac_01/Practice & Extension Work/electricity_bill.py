"""Electricity bill estimator"""


def main():
    print("Electricity bill estimator")
    cents_per_kwh = float(input("Enter cents per kWh: "))
    daily_use_in_kwh = float(input("Enter daily use in kWh: "))
    number_of_billing_days = int(input("Enter number of billing days: "))
    estimated_bill = ((cents_per_kwh / 100) * daily_use_in_kwh) * number_of_billing_days
    print("Estimated bill: $", estimated_bill, sep="")


main()
