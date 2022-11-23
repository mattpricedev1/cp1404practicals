from prac_09.silver_service_taxi import SilverServiceTaxi

my_new_taxi = SilverServiceTaxi("Hummer", 200, 2)
my_new_taxi.drive(18)
print(f"{my_new_taxi} Total Fare: ${my_new_taxi.get_fare()}")
