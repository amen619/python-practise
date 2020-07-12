class Animal:
    sound = ""
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("{sound} I'm {name} {sound}".format(name=self.name, sound=self.sound))

# Piglet and Cow class has been inherited from the Animal class
class Piglet(Animal):
    sound = "Oink!"

class Cow(Animal):
    sound = "Moooo!"

nila = Piglet("Nila")
cow = Cow("Milky, cow!!")

print(nila.speak())
print(cow.speak())
