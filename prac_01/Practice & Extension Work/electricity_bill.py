"""Electricity bill estimator"""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928


def main():
    print("Electricity bill estimator 2.0")
    tariff_choice = input("Which tariff? 11 or 31: ")
    daily_use_in_kwh = float(input("Enter daily use in kWh: "))
    number_of_billing_days = int(input("Enter number of billing days: "))
    # estimated_bill = (TARIFF_11 * daily_use_in_kwh) * number_of_billing_days
    # TODO: Add tariff selection functionality
    print(f"Estimated bill: ${estimated_bill:.2f}")


main()
