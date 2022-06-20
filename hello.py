'''
Example of instantiating a Person class and two objects: Josh and Derek
The Person class currently has two properties, firstName and lastName
and one method, printFullName(), which prints the full name of the object

See if you can practice adding properties (e.g. self.age)

run the script in the terminal by typing `python3 hello.py`
'''

class Person:
	def __init__(self, firstName, lastName):
		self.firstName = firstName
		self.lastName = lastName
	
	def printFullName(self):
		# this is an fString, a simple way to format strings which reference variables
		print(f"{self.firstName} {self.lastName}")

Derek = Person("Derek", "Curley")
Josh = Person("Josh", "Kenney")

Derek.printFullName()
Josh.printFullName()