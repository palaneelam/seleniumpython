# 1. Class - it is a blueprint for creating objects
# 2. Objects - it is an instance of a class. When a class is defined - no memory is allocated.
#              However, when object is created - memory gets allocated
# 3. Methods - function defined inside the class
# 4. attribute - variable that is defined/declared inside the class (variable/parameter/input)
# 5. constructor - will initialise the varibales for a class
from abc import abstractmethod


# class Dog:
#     #class attribute
#     species = "Golden Retriever"
#
#     print(species)
#     #constructor
#     def __init__(self, name_dog, age):
#         #Instance attribute
#         self.name = name_dog
#         self.age = age
#
#     def description(self):
#         return f"{self.name} is {self.age} years old"
#
#     def speak(self, sound):
#         return f"{self.name} says {sound}"
#
# my_dog = Dog("Oreo", 6)
# print(my_dog.description())
# print(my_dog.speak("Woof Woof"))
#
# my_another_dog = Dog("Rocky", 10)
# print(my_another_dog.description())
# print(my_another_dog.speak("Bark bark"))

#********************************************************************************
# Core 4 principles of OOP
# 1. Encapsulation
# 2. Inheritance
# 3. Polymorphism
# 4. Abstraction

# class Person:
#     def __init__(self, name, aadhar_nbr):
#         self.__name = name                # private attribute
#         self.__aadhar_nbr = aadhar_nbr    # private attribute
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self,name):
#         self.__name = name
#         return self.__name
#
# # print(self.__name)
#
# person = Person("Neelam", 37456)
# print(person.get_name())
# print(person.set_name("aa"))
#
# person_2 = Person("Priya", 12345)
# print(person_2.get_name())

# 2. Inheritance
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         return "Animal Speaks"
#
#
# class Dog(Animal):
#     pass
     # def speak(self):
     #     return f"{self.name} says Woof"

# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} says Meow"
#
# dog = Dog("Oreo")
# cat = Cat("Kitty")
# print(dog.speak())
# print(cat.speak())

# 3. Polymorphism - allows methods to do different things based on the object it is acting upon,
# even though they share the same name. It means "many forms" and allows to
# define a single interface with multiple implementation

# class Bird:
#     def speak(self):
#         return "Tweet tweet"
#
# class Fish:
#     def speak(self):
#         return "bodo bodo"
#
# def make_sound(animal):
#     print(animal.speak())
#
# bird = Bird()
# fish = Fish()
# make_sound(bird)
# make_sound(fish)

# 4. Abstraction
class ABC:
    pass

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

rect = Rectangle(10,20)
circle = Circle(5)
print(rect.area())
print(circle.area())




























