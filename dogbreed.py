cclass Dog:
    species = "Canine"   # class variable (shared by all objects)

    def __init__(self, dog_breed, color):
        self.dog_breed = dog_breed   # instance variable
        self.color = color           # instance variable

ob1 = Dog("German Shepherd", "Black")
ob2 = Dog("Labrador", "Yellow")

print(ob1.species, ob1.dog_breed, ob1.color)
print(ob2.species, ob2.dog_breed, ob2.color)
