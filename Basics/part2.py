"""
Example of python functions and modules.
"""
from __future__ import print_function
from math import sqrt

print(sqrt(121))
#string formatting
fname = "Ann"
lname = "Marlen"
print("Hello there %s %s!" % (fname,lname),end="")
print("Goodbye {1} {0}".format(fname,lname))
def f():
	return "Hello world!"


def f2():
	def f():
		return "Goodbye world!"
	print(f())

def to_add(nr):
	def sum(number):
		return nr + number
	return sum

f2()
add_5_to = to_add(5)
print(add_5_to(36))


#Classes
class Test(object):
    def __init__(self):
        self.__a = 'var a'
        self._b = "var b"

t = Test()
print(t._b)
print(t._Test__a)
# you can still access private variables, double underscore is just a namemangle,the variable is still
# in the form such as : instancename._className__privatevar

class Books:
	number_of_books = 0
	def __init__(self,author,title):
		self.author = author
		self.title = title
		self.number_of_books = Books.number_of_books
		Books.number_of_books += 1
class Animal:
    # None signifies the lack of a value
    # You can make a variable private by starting it with __
    __name = None
    __height = None
    __weight = None
    __sound = None
    _ex = None
 
    # The constructor is called to set up or initialize an object
    # self allows an object to refer to itself inside of the class
    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound
        self._ex = 42
 
    def set_name(self, name):
        self.__name = name
 
    def set_height(self, height):
        self.__height = height
 
    def set_weight(self, height):
        self.__height = height
 
    def set_sound(self, sound):
        self.__sound = sound
 
    def get_name(self):
        return self.__name
 
    def get_height(self):
        return str(self.__height)
 
    def get_weight(self):
        return str(self.__weight)
 
    def get_sound(self):
        return self.__sound
 
    def get_type(self):
        print("Animal")
 
    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {}".format(self.__name, self.__height, self.__weight, self.__sound)
 
# How to create a Animal object
cat = Animal('Whiskers', 33, 10, 'Meow')
 
print(cat.toString())
print(cat._ex)

