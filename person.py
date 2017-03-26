''' Written by Daniel Elkington for the SISG Makeathon
	Represents a person
'''

class Person:
	def __init__(self, firstName, middleName, familyName, phoneNumber):
		self.firstName = firstName
		self.middleName = middleName
		self.familyName = familyName
		self.phoneNumber = phoneNumber

	def toString(self):
		return self.firstName + ' ' + self.middleName + ' ' + self.familyName + ' (' + self.phoneNumber + ')'