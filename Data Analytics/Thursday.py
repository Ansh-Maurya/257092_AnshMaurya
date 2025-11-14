#Class
'''class Car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"{self.color} {self.brand} is driving 🚗")

car1 = Car("BMW","Black")
car1.drive()'''

#Encapsulation
'''class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age

p1 = Person("Ansh",900)
print(p1._Person__age)'''

#Inheritance
'''class Animal:
    def speak(self):
        print("Animal Speaks")
    
class Dog(Animal):
    def speak(self):
        print("Dog Barks 🐶")

dog = Dog()
dog.speak()
'''
#Polymorphism
'''class Animal:
    def sound(self):
        print("animals have different sounds")
class Cat(Animal):
    def sound(self):
        return "Meow"
    
class Dog(Animal):
    def sound(self):
        return "Woof"
for animal in [Cat(),Dog()]:
    print(animal.sound())'''

#Abstraction
'''from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car started")

class Bike(Vehicle):
    def start(self):
        print("Bike started")
Vehicles = [Car(),Bike()]

for v in Vehicles:
    v.start()'''

#Pandas

import pandas as pd

'''data = {
    "Name" : ['Ritik','Aman','Priya','Neha'],
    "Age" : [21,23,20,22],
    "Marks" : [85,90,78,88]
}
df = pd.DataFrame(data)
print(df)
print(pd.__version__)'''
'''
a = [1,7,2]
myvar = pd.Series(a,index=['x','y','z'])
print(myvar['y'])'''

data = {"Math":90,"Science":85,"English":70}
ds = pd.Series(data.get("Science"))
print(ds)