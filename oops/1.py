class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

# Inheritance
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

# Polymorphism
def animal_sound(animal):
    animal.speak()

# Creating objects
a1 = Animal("GenericAnimal")
d1 = Dog("Tommy")

animal_sound(a1)  # GenericAnimal makes a sound
animal_sound(d1)  # Tommy says Woof!
