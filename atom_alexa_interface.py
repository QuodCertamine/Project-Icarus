#! /usr/bin/python3

from firebase import firebase
from time import gmtime, strftime, localtime

"""
This is the command interface. Connects to Alexa
"""

# initialize Firebase Application connection
class Alexa():
	def __init__(self, location=None, user=None, command=None):
		self._fb = firebase.FirebaseApplication("https://atom-pet.firebaseio.com", None)

		# Initial State
		time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
		data = {'state':'standby', 'location':location, 'timestamp':time ,'user':user, 'command': command}
		result = self._fb.patch("/status", data)
		self._state = data
		
	def update_state(self):
		# Look at the database to see if there have been any changes
		self._state = self._fb.get('/status', None)
		return self._state