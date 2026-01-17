#day1 starting from basics
print("Hello World!",end=" ") #this will print both lines in same line 
print("Myself Kirtika Khowal currently pursuing BTECH-CSE(AI/ML)")
print("I am", 19 ,"years old")

#this is single line comment

"""
this is multiline
comment
"""
#assigning variables
x="kirtika"
y=19
print(x,y)

#casting if you want to specify the data type
x=str(3) #here 3 is string not integer

#assigning value to multiple variable
x,y,z= "tiya","harshita","khushi"
print(x,y,z)

#global variable (variable which are assigned outside the function)
x= "awesome"
def myfunc():
    print("python is " + x)
    myfunc()

#global vs local
x = "awesome" #global

def myfunc():
  x = "fantastic" #local
  print("Python is " + x)

myfunc()

print("Python is " + x)


#data types in python
x = str("Hello World")	#str	
x = int(20)	#int	
x = float(20.5)	#float	
x = complex(1j)	#complex	
x = list(("apple", "banana", "cherry"))	#list	
x = tuple(("apple", "banana", "cherry"))	#tuple	
x = range(6)	#range	
x = dict(name="John", age=36)	#dict	
x = set(("apple", "banana", "cherry"))	#set	
x = frozenset(("apple", "banana", "cherry"))	#frozenset	
x = bool(5)	#bool	
x = bytes(5)	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5)) #memoryview

#type of number
x=1
y=0.9
z=1j
print(type(x))
print(type(y))
print(type(z))

#import random number
import random
print(random.randrange(1,10)) #it will print any random number btw 1 to 9

#slicing
b="hello world"
print(b[2:5]) #print from position 2 to 4 5 will not include
print(b[:5]) #print from start to 4 5 will not include
print(b[2:])#print from 2 to end
print(b[-5:-2])#print wor
print(b.upper())#return string in upper case
print(b.lower())#return string in lower case
print(b.replace("h","j"))#replace h with j
print(b.split(","))#split string into substring

#boolean values
#true
print(10 > 9)
print(10 == 9)
print(10 < 9)

"""Almost any value is evaluated to True if it has some sort of content.
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones."""

#false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

"""empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False."""

#arithmetic operators
x = 15
y = 4

print(x + y)#add
print(x - y)#substract
print(x * y)#multiple
print(x / y)#divide
print(x % y)#remainder
print(x ** y)#power
print(x // y)#reamainder

#comparison operator
x = 5
y = 3

print(x == y) #equal
print(x != y)#not equal
print(x > y)# x greater
print(x < y)#y greater
print(x >= y)#x greater or equal
print(x <= y)#y greater or equal

#logical 
x=5
print(x>0 and x<10)
print(x>5 or x<10)
print(not(x>3 and x<10))