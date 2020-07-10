animals = ["Lion", "Zebra", "Monkey", "Dolphin", "Shark"]

chars = 0

for animal in animals:
    chars += len(animal)

print("Total charectors: {}, Average Length: {}".format(chars, chars/len(animals)))
