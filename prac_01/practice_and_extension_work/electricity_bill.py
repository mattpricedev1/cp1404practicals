"""Electricity bill estimator program."""

TARIFF_NUM_TO_PERCENT = {"11": 0.244618,
                         "31": 0.136928}

print("Electricity bill estimator 2.0")
estimated_bill = 0
tariff = input("Which tariff? 11 or 31: ")
while tariff not in TARIFF_NUM_TO_PERCENT:
    print("Invalid tariff")
    tariff = input("Which tariff? 11 or 31: ")
daily_kwh = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))
estimated_bill = TARIFF_NUM_TO_PERCENT[tariff] * daily_kwh * billing_days
print(f"Estimated bill: ${estimated_bill:.2f}")
