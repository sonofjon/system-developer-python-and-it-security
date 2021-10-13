# Exercise 1:

class FruitShop:

    def __init__(self, name, fruits):
        self.name = name
        self.fruits = fruits

    def get_fruits_count(self):
        return len(self.fruits)

my_shop = FruitShop("My Fruit Shop", ["Banana" , "Orange", "Kiwi", "Apple"])
# print(my_shop.get_fruits_count())


# Exercise 2:

class Animal:

    def eat(self):
        return "eating.. nom.. nom.."

class Horse(Animal):

    def neigh(self):
        return "neigh!"

class Dog(Animal):

    def bark(self):
        return "voof voof!"

my_horse = Horse()
# print(my_horse.neigh())

my_dog = Dog()
# print(my_dog.bark())


# Exercise 3:

class Person:

    def walk(self):
        return "walking"

class Staff:

    def work(self):
        return "working"

class BusDriver(Person, Staff):

    def drive(self):
        return "driving"

my_BusDriver = BusDriver()
# print(my_BusDriver.walk())
# print(my_BusDriver.work())
# print(my_BusDriver.drive())


# Exercise 4:

class Drums:
    def play(self):
        print("playing the drums")


class Synth:
    def play(self):
        print("playing the synth")


def play_instrument(instrument):
    instrument.play()


drums = Drums()
# play_instrument(drums)

synth = Synth()
# play_instrument(synth)


# Exercise 5

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_area(self): pass

    @abstractmethod
    def calculate_perimeter(self): pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width

    def calculate_perimeter(self):
        return 2 * self.height + 2 * self.width


circle = Circle(5)
# print(circle.calculate_area())
# print(circle.calculate_perimeter())

rectangle = Rectangle(10, 20)
# print(rectangle.calculate_area())
# print(rectangle.calculate_perimeter())
