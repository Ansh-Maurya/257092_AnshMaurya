
#Create a function to take input from user (book number) and print the corresponding value of the input
'''def func():

    book = {
        1:"Maths",2:"BEEE",3:"Chemistry",4:"WT",5:"Physics"
    }

    usr_in=int(input("Enter book number: "))
    if usr_in in book.keys():
        print(f"Book is {book[usr_in]}")
    else:
        print('Invalid Book number')

yn = input("Want to search? (y/n): ")
if yn == 'y'or yn == 'Y':
    func()
else:
    exit()'''

#Pre-Defined functions
'''import random
print("Random number:",random.randint(0,1000000000))
name = ["Ansh","Shiva","Harshit","Yash"]
print(f"Hello {random.choice(name)}")'''

'''import datetime
today = datetime.date.today()
print("Date is :",today)
now = datetime.datetime.now()
print("Time:",now)'''

'''import sys
sys = sys.platform
print(sys.version)
print(sys)'''

'''import math
print(math.pow(2,3))
print(math.sqrt(144))
print(math.pi)
print(math.ceil(2.4))
print(math.floor(4.9))'''

#Write a function to take random number and check 1.-ve or +ve 2.Even or Odd 3.Divisible by 5
'''import random
def task():
    value = random.randint(-10000,10000)
    print(f"Number:{value}")
    if value<0:
        print("Negative")
    else:
        print("Positive")
    if value%2==0:
        print("Even")
    else:
        print("Odd")
    if value%5==0:
        print("Number is divisible by 5")
    else:
        print("Number is not divisible by 5")
task()'''

#OOP in Python
'''class abc:
    def __init__(self,name,age):
        self.name=  name
        self.age = age

p1 = abc("Ansh",920)
print(p1.name)
print(p1.age)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"My name is {self.name} and I am {self.age} years old")
result1 = Person("Rachit",23)
result1.greet()'''

#Rectangle
class Rectangle:
    def _init_(self,length,breadth):
        self.length = length
        self.breadth = breadth


    def area(self):
        areaofrect= length*breadth
        print(f"Area:{areaofrect}")
length,breadth = int(input("Enter Length: ")) , int(input("Enter Breadth: "))
result = Rectangle()
result.area()

#Calc
class Calculator:
    def _init_(self,a,b):
        self.a = a
        self.b = b
        
    def add(self):
        print("Add:",a+b)
    def sub(self):
        print("Sub:",a-b)
    def mult(self):
        print("Mult:",a*b)
    def div(self):
        print("Div:",a/b)
    
a,b = int(input("Enter a:")),int(input("Enter b:"))
ad,s,m,d = Calculator(),Calculator(),Calculator(),Calculator()
ad.add()
s.sub()
m.mult()
d.div()
