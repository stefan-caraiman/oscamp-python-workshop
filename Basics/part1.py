#!/usr/bin/python
#This is a comment
#Python is a dynamic typed language.
intExample = 42 # declaring an int
longExample = 2000L # long variable
floatExample = 3.1415 # float/double variable
boolExample = True #a bool variable -> evaluted to false

#Print on console in Python 2.7.x
print type(longExample)
#Print on console in Python 3.x
#from __future__ import print_function
print("Hello there everyone!")
#Let's take a further look at conditional operators
print True and False
print True or False
print not True

#Other operands
a = 5
b = 2.0
print a / b
print a // b
print int(a ** b)
print a % b # works on floating point number,although it's not accurate
print a > b #True
print a < b #False
print a == b #False
print a != b #True
