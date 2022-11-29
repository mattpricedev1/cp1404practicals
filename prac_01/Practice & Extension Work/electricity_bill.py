"""Electricity bill estimator program."""
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator")
cents_per_kwh = float(input("Enter cents per kWh: "))
daily_kwh = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))
estimated_bill = cents_per_kwh / 100 * daily_kwh * billing_days
print("Estimated bill: ${}".format(estimated_bill))

