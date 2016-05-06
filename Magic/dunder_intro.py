class x():
	def __init__(self):
		self.a = 5
	def __len__(self):
		return 60

a = x()
print len(a)

#difference between __new__ and __init__
#__new__ creates and instance and returns it
#__init__ initializates the new instance and returns nothing
class Apple(str):
	def __new__(cls,fruit):
		if fruit != "apple":
			raise ValueError("It has to be an apple")
		else:
			return str.__new__(cls,str)
	def __init__(self,fruit):
		self.fruit = fruit

	def get_fruit(self):
		return self.fruit

a = Apple("apple")
print a.get_fruit().upper().lower().join("X ")