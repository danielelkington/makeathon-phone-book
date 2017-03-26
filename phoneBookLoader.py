''' Written by Daniel Elkington for the SISG Makeathon
	Loads a large amount of person data into memory, returning it as a list.
	Also provides the ability to add new people, which appends them to the end of the file.
'''
import csv
import sys
import time
from person import Person

class PhoneBookLoader:
	def __init__(self):
		#If you have access to the large 'people.csv' file, change this to 'people.csv' to use it
		self.fileName = 'small-people.csv'

	def load(self):
		people = []
		start = time.time()

		#Figure out how many people there are
		lines = sum(1 for line in open(self.fileName))
		currentLine = 0

		#Loop through CSV loading all people
		with open(self.fileName, 'r') as peopleFile:
			peopleReader = csv.reader(peopleFile, delimiter=',')
			next(peopleReader, None) #ignore header line
			print 'Loading people...'
			for personRow in peopleReader:
				currentLine += 1
				if (currentLine % 200000 == 0):
					percentComplete = (currentLine * 100.0)/lines
					sys.stdout.write('\r' + "%.2f" % percentComplete + '% complete')
					sys.stdout.flush()
				people.append(Person(personRow[0], personRow[1], personRow[2], personRow[3]))
			end = time.time()
			sys.stdout.write('\rLoading people completed in ' + "%.0f" % (end - start) + ' seconds!\n')
			sys.stdout.flush()

		return people

	def addPerson(self, people):
		firstName = raw_input('Enter first name: ')
		middleName = raw_input('Enter middle name: ')
		familyName = raw_input('Enter family name: ')
		havePhoneNumber = False
		while not havePhoneNumber:
			phoneNumber = raw_input('Enter phone number: ')
			try:
				phoneNumberAsInt = int(phoneNumber)
				if not len(phoneNumber) == 10:
					print 'Not a phone number, must be a 10-digit number!'
				else:
					havePhoneNumber = True
			except ValueError:
				print 'Not a phone number, must be a 10-digit number!'				
		person = Person(firstName, middleName, familyName, phoneNumber)
		people.append(person);
		personString = firstName + ',' + middleName + ',' + familyName + ',' + phoneNumber + '\n'
		with open(self.fileName, 'a') as file:
			file.write(personString)
		print 'Person added!'
		print
		return people