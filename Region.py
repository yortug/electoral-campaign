import numpy as np
from Processing import *

"""
almost all of these functions are really boring, just
setters, getters and maybe a couple basic find functions;
thus i've not really commented on anything, although the
reasons behind me setting my classes up this way can be found
from within the documentation if you're curious
"""

pp = Processing()

class Country:
	def __init__(self, country_name, nStates):
		self.country = country_name
		self.states = np.empty(nStates, dtype = object)

	def __str__(self):
		return str(self.country) + ' ' + str(len(self.states))

	def setStates(self, state_objects):
		for i,z in enumerate(state_objects):
			self.states[i] = z

	def getStates(self):
		return self.states

	def findState(self, state):
		i = 0
		val = None
		while i < len(self.states) and self.states[i].getCode() != state:
			i += 1
		if i >= len(self.states):
			val = None
		else:
			val = self.states[i]

		return val

class State:
	def __init__(self, symbol, nElectorates):
		self.symbol = symbol
		self.electorates = np.empty(nElectorates, dtype = object)

	def __str__(self):
		return str(self.symbol) + ' ' + str(len(self.electorates))

	def getCode(self):
		return self.symbol

	def getElectorates(self):
		return self.electorates

	def setElectorates(self, division_names, division_party_numbers):
		for i,z in enumerate(division_names):
			self.electorates[i] = Division(z, division_party_numbers[i])

	def findElectorate(self, electorate):
		i = 0
		val = None
		while i < len(self.electorates) and self.electorates[i].getDivName() != electorate:
			i += 1
		if i >= len(self.electorates):
			val = None
		else:
			val = self.electorates[i]

		return val


class Division:
	def __init__(self, label, nParties):
		self.division = label
		self.parties = np.empty(nParties, dtype = object)

	def __str__(self):
		return str(self.division) + ' ' + str(len(self.parties))

	def getDivName(self):
		return self.division

	def getParties(self):
		return self.parties

	def setParties(self, party_names, party_candidates):
		# print('party names: ' + str(party_names))
		# print('party candidate ID: ' + str(party_candidates))
		for i,z in enumerate(party_names):
			self.parties[i] = Party(z, len(party_candidates[i]))

	def findParty(self, party):
		i = 0
		val = None
		while i < len(self.parties) and self.parties[i].getPartyName() != party:
			i += 1
		if i >= len(self.parties):
			val = None
		else:
			val = self.parties[i]

		return val

class Party:
	def __init__(self, name, nCandidates):
		self.party = name
		self.candidates = np.empty(nCandidates, dtype = object)
		self.votes = 0

	def __str__(self):
		return str(self.party) + ' ' + str(len(self.candidates)) + ' [' + str(self.votes) + ']'

	def getPartyName(self):
		return self.party

	def getCandidates(self):
		return self.candidates

	def getVotes(self):
		return self.votes

	def setVotes(self):
		"""
		iterates through all the candidates within this
		party and increments the total votes as it does so
		"""
		numVotes = 0
		for i in self.candidates:
			numVotes += i.getVotes()
		
		self.votes = numVotes

	def setCandidates(self, candidate_ids):
		for i,z in enumerate(candidate_ids):
			self.candidates[i] = Candidate(z)

class Candidate:
	def __init__(self, candidate_id):
		self.id = candidate_id
		self.fname = ''
		self.lname = ''
		self.elected = None
		self.helected = None
		self.votes = 0

		self.state = ''
		self.division = ''
		self.party = ''

	def __str__(self):
		if self.party != '':
			val = str(self.state)+' | '+str(self.division)+' | '+str(self.party)+' | '+str(self.elected)+' | '+str(self.helected)+' | '+str(self.id)+' | '+str(self.lname)+' | '+str(self.fname)+' | '+str(self.votes)
		else:
			val = str(self.state)+' | '+str(self.division)+' | '+'000'+' | '+str(self.elected)+' | '+str(self.helected)+' | '+str(self.id)+' | '+str(self.lname)+' | '+str(self.fname)+' | '+str(self.votes)

		return val

	def getID(self):
		return self.id

	def getVotes(self):
		return int(self.votes)

	def getFname(self):
		return self.fname

	def getLname(self):
		return self.lname

	def getState(self):
		return self.state

	def getDivision(self):
		return self.division

	def getParty(self):
		return self.party

	def setFname(self, fname):
		self.fname = fname

	def setLname(self, lname):
		self.lname = lname

	def setElected(self, elected):
		self.elected = elected

	def setHelected(self, helected):
		self.helected = helected

	def updateVotes(self, votes):
		self.votes += votes

	def setState(self, state):
		self.state = state

	def setDivision(self, division):
		self.division = division

	def setParty(self, party):
		self.party = party



