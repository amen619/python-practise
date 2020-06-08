def convert_distance(miles):
	return miles * 1.6  # approximately 1.6 km in 1 mile
my_trip_miles = 55

# Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)
# Fill in the blank to print the result of the conversion
print("The distance in kilometers is " +str(my_trip_km))

# Calculate the round-trip in kilometers by doubling the result,
# and fill in the blank to print the result
print("The round-trip in kilometers is "+str(my_trip_km * 2))

