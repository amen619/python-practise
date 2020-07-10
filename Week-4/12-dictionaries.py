wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for key, value in wardrobe.items():
	for end in wardrobe.values():
		print("{} {}".format(key, end))

# NOT Solved yet. Expected output is red shirt, blue shirt etc etc
