# Python program to demonstrate
# method overriding


# Defining parent class
class Parent():
	
	# Constructor
	def __init__(self):
		self.value = "Inside Parent"
		
	# Parent's show method
	def show(self):
		print(self.value)
		
# Defining child class
class Child(Parent):
	
	# Constructor
	def __init__(self):
		self.value = "Inside Child"
		
	# Child's show method
	def show(self):
		print(self.value)
		
		
# Driver's code
obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()


a = 4
b = 10
print(int.__add__(a,b))

a = '4'
b = '10'
print(str.__add__(a,b))

a = 4
b = 10
print(int.__sub__(b,a))

print("Address of A is",id(a))
