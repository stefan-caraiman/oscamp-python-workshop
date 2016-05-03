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

- _single_leading_underscore: weak "internal use" indicator.  E.g. "from M
  import *" does not import objects whose name starts with an underscore.

- single_trailing_underscore_: used by convention to avoid conflicts with
  Python keyword, e.g.

  Tkinter.Toplevel(master, class_='ClassName')

- __double_leading_underscore: when naming a class attribute, invokes name
  mangling (inside class FooBar, __boo becomes _FooBar__boo; see below).

- __double_leading_and_trailing_underscore__: "magic" objects or
  attributes that live in user-controlled namespaces.  E.g. __init__,
  __import__ or __file__.  Never invent such names; only use them
  as documented.