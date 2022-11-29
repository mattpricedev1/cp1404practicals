"""Electricity bill estimator program."""
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")
estimated_bill = 0
tariff = input("Which tariff? 11 or 31: ")
# cents_per_kwh = float(input("Enter cents per kWh: "))
daily_kwh = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))
if tariff == "11":
    estimated_bill = TARIFF_11 * daily_kwh * billing_days
elif tariff == "31":
    estimated_bill = TARIFF_31 * daily_kwh * billing_days
else:
    print("Invalid tariff")
print(f"Estimated bill: ${estimated_bill:.2f}")
