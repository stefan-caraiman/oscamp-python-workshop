#!/usr/bin/python
#This is a comment
#Python is a dynamic typed language.
#Everything in Python is an object, everything.
#
intExample = 42 # declaring an int
longExample = 2000L # long variable
floatExample = 3.1415 # float/double variable
boolExample = True #a bool variable -> evaluted to false
aString = "Anna"
multiLine = '''Well, would you look at that.
There are a lot of people.
Huh?'''
#Print on console in Python 2.7.x
print type(longExample)
#Print on console in Python 3.x
#from __future__ import print_function
print(multiLine)
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

#Data types/structures
#Lists -> mutable,iterable,non-unique elements
aList = [3.14,"First",500,True,"Kitty",23L,[1,"Ann"]]
print type(aList)
print len(aList)
#Slicing
print aList[6][1]
print aList[1:3]
aList.append(121)
aList.insert(0,"First")
aList.remove("First")
aList.sort()
aList.reverse()
print aList

#Tuples are immutable, meaning their values cannot be changed once initialized
windowSize = (800,600)
lst = list(windowSize)
print all(isinstance(val,int) for val in lst)