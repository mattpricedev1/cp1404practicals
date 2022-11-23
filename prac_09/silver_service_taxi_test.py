from prac_09.silver_service_taxi import SilverServiceTaxi

my_new_taxi = SilverServiceTaxi("Gold Trip", 100, 50)
my_new_taxi.drive(50)
print(f"{my_new_taxi} Total Fare: ${my_new_taxi.get_fare()}")
my_grand_taxi = SilverServiceTaxi("Gold Trip II", 200, 700)
my_grand_taxi.drive(100)
print(f"{my_grand_taxi} Total Fare: ${my_grand_taxi.get_fare()}")
