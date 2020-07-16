def format_address(address_string):
  # Declare variables
  house_number = 0
  street = ""
  separate_add = address_string.split()

  # Traverse through the address parts
  for address in separate_add:
    if address.isnumeric():
      house = address
    else:
      street += address + " "
  # Return the formatted string  
  return "house number {} on street named {}".format(house, street)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"


