class Dog:
   animal = "Dog"
   def __init__(self, breed, colour):
        self.breed = breed
        self.colour = colour

dog1 = Dog("Labrador", "Yellow")
dog2 = Dog("German Shepherd", "Black and Tan")

print(f"Dog 1: Animal = {dog1.animal}, Breed = {dog1.breed}, Colour = {dog1.colour}")
print(f"Dog 2: Animal = {dog2.animal}, Breed = {dog2.breed}, Colour = {dog2.colour}")