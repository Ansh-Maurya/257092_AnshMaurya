#1st task (Voting system)
'''age = int(input("Enter you age: "))
if age<0:
    print("Invalid input")
elif age>=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")'''

#2nd task (Grading system)
'''
grade = int(input("Enter your grade: "))
if (grade >= 35 and grade < 65):
    print("C")
elif (grade >= 65 and grade <=80):
    print("B")
elif (grade > 80 and grade <=85):
    print("A")
elif grade > 85:
    print("A++")
else:
    print("Fail") '''

#List
'''a = ["Rachit","Vaishnavi","Shalini",12]
print(type(a))
#Tuples: It is use to store the multiple values in the single variable but tuples are immutable
b = ("Ansh","Harshit",12)
#sets: are used to store the multiple values in single variable but sets are unordered and unindexed
c = {"ansh","shiva",12,7.0}
print(type(c))
#Dictionary: are used to store multiple values in single variable in key:value pair
d = {"Name":"Ansh","Age":10000,"College":"Saitm"}
print(d["College"])'''

#Loops: while loop
'''count = 5
while count>0:
    if count%2==0:
        print(f"{count} is even")
    else:
        print(f"{count} is odd")
    count-=1

age = 0
while age<=100:
    if age>=18:
        print(f"You are eligible to vote,your age is {age}")
    else:
        print("Not") 
    age+=1  '''
#For Loop
'''nums=[1,2,3,4,5,6,7,8,9]
for num in nums:
    if num %2==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd") '''

'''for i in range(1,11,2):
    print(i)'''

'''marks={"A":75,"B":90,"C":40,"D":80,"E":20}
for i in marks:
    if marks[i]>=90:
        print("A++")
    elif marks[i]>=80 and marks[i]<90:
        print("A")
    elif marks[i]<80 and marks[i]>=60:
        print("B")
    elif marks[i]<60 and marks[i]>=40:
        print("C")
    else:
        print("Fail")'''

'''def add(num):
    return num+num

result = add(25)
print("add is ",result)
result = add(15)
print("add is ",result)
result = add(20)
print("add is ",result)'''

def abc():
    print("Hello World")
abc()


def abc(name):
    print(f"My name is {name} ")
abc("Rajeev")
abc("rashika")
abc("nia")
abc("amar")

def square(num):
    return num*num
result = square(25)
print("Square is ",result)
result = square(15)
print("Square is ",result)
result = square(20)
print("Square is ",result)
result = square(5)
print("Square is ",result)
result = square(12)
print("Square is ",result)