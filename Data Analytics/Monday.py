#Basics of python

print("Hello World")
a = 3
b = 4
print(a+b)
x = float(5)
x = 6
print(type(x))
print(2*6/3+900)
x = str(6) 

#Arithmetic operators
print(3+4)
print(6-7)
print(7*8)
print(4/2)
print(3**2)
print(4//2)
print(4%2)


a = 12
a+=2
print(a)

print(x)
print("hello",x,"world")

x = "Hello"
print(x.upper())
print(x.lower())
print(x.replace('l','w'))

x = "hello"
print(x.capitalize())

#Formatted String

age = 19
print(f"My age is {age} years")

a , b = 27,39
print(f"Sum {a+b}")
print(f"float {a: .2f}")
 
txt = "world"
x = txt.center(30)    #Center Function
print(x)

txt ="Hello"
print(txt.count('l'))   #Count function 

a = "abCdef"
print(a.islower())     #islower gives answer in boolean value true or false

#Comparison operators
print(7>4)   #answer will be true 
print(12 == 13)
print(12 != 13)
x = 15
print(10< x < 20)

#Logical Operators
print(12 > 15 and 15 < 20)
print(12 > 15 or 15 < 20)
print(not(15 < 20))

#bitwise operator
x , y = 6 , 3
print(x & y)
print(x | y)
print(x ^ y)
print(~x)
print(x << 2)

#Conditionals
if x>y:
    print("x is bigger than y")
elif x==y:
    print("x and y are equal")
else:
    print("y is bigger than x")