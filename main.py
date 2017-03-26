''' Written by Daniel Elkington for the SISG Makeathon
	This program reads a large amount of sample person data and puts it into the class 'Person'.
	A command line application allows the user to interact with the person data, performing tasks such as 
	adding a new person, or searching for people.
	The challenge is to come up with a fast way of searching the person data.
'''

import time
import sys
from phoneBookLoader import *
import makeathonCodeHere

def getUserInput():
	userInput = raw_input('Enter ''A'' to add a person, ''S'' to search for a person, ''R'' to reload your custom code, or ''Q'' to quit: ')
	while True:
		if (userInput.upper() == 'A' or userInput.upper() == 'R' or userInput.upper() == 'S' or userInput.upper() == 'Q'):
			return userInput.upper()
		userInput = raw_input('Bad input, try again: ')

def customSetupCode(customCode, people):
	print 'Doing your custom setup code...'
	start = time.time()
	customCode.setup(people)
	end = time.time()
	sys.stdout.write('\rYour custom setup code completed in ' + "%.0f" % (end - start) + ' seconds!\n')

def reloadCustomCode(people):
	reload(makeathonCodeHere)
	customCode = makeathonCodeHere.MakeathonCodeHere()
	print 'Reloaded your custom code!'
	customSetupCode(customCode, people)
	return customCode

def searchPerson(people):
	badInput = True
	while badInput:
		firstName = raw_input('First name, or blank:')
		middleName = raw_input('Middle name, or blank:')
		familyName = raw_input('Family name, or blank:')
		if (firstName == '' and middleName == '' and familyName == ''):
			print 'Must enter at least one search term!'
		else:
			badInput = False
	start = time.time()
	peopleFound = customCode.personSearch(people, firstName, middleName, familyName)
	end = time.time()
	print
	print 'Results:'
	for person in peopleFound:
		print person.toString()
	print 'Found ' + str(len(peopleFound)) + ' people in ' + "%.4f" % (end - start) + ' seconds!'

if __name__ == '__main__':
	print '*******************************'
	print 'Welcome to the Australian Phone Book app!'

	customCode = makeathonCodeHere.MakeathonCodeHere()
	
	#Load people
	loader = PhoneBookLoader()
	people = loader.load()

	#Do any custom setup code
	customSetupCode(customCode, people)

	#Enter the main loop
	exit = False
	while not exit:
		userInput = getUserInput()
		if userInput == 'A':
			people = loader.addPerson(people)
		elif userInput == 'R':
			customCode = reloadCustomCode(people)
		elif userInput == 'S':
			searchPerson(people)
		elif userInput == 'Q':
			exit = True

	print 'Bye :)'
	print '*******************************'