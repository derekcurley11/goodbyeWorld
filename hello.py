'''
Example of instantiating a Person class and two objects
Josh and Derek
The Person class currently has two properties, firstName and lastName
and one method, printFullName(), which prints the full name of the object

See if you can practice adding properties (e.g. self.age)
'''

class Person:
	def __init__(self, firstName, lastName):
		self.firstName = firstName
		self.lastName = lastName
	
	def printFullName(self):
		print(f"{self.firstName} {self.lastName}")

Derek = Person("Derek", "Curley")
Josh = Person("Josh", "Kenney")

Derek.printFullName()
Josh.printFullName()