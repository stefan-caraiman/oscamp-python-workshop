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