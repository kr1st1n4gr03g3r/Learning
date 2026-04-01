# - Create a distance converter converting Km to miles
km = float(1.609)
miles = float(1)
miles_to_km = miles / km
# - Take two inputs from user: Their first name and the distance in km
first_name = input("What's your first name?")
user_km_distance = float(input("How many km?"))
# - Print: Greet user by name and show km, and mile values
print(f"Hello, {first_name.capitalize()}. {user_km_distance} km is {user_km_distance * miles_to_km} miles!")
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name