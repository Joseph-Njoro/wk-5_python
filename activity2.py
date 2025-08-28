class Animal:
    def move(self):
        pass

class Bird(Animal):
    def move(self):
        return "Flying 🕊️"

class Fish(Animal):
    def move(self):
        return "Swimming 🐠"

animals = [Bird(), Fish()]

for animal in animals:
    print(animal.move())
