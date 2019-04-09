import numpy as np
import copy

class DSAHashTable:
	def __init__(self, size):
		self.size = self.nextPrime(int(size))
		self.hashtable = np.empty(self.size, dtype=object)
		self.count = 0

	def isFull(self):
		return self.size == self.count

	def nextPrime(self, start):
		if start % 2 == 0:
			primeVal = start + 1
		else:
			primeVal = start

		primeVal = primeVal - 2
		isPrime = False
		while not isPrime:
			primeVal = primeVal + 2
			ii = 3
			isPrime = True
			while ii*ii <= primeVal and isPrime:
				if primeVal % ii == 0:
					isPrime = False
				else:
					ii = ii + 2

		return int(primeVal)


	def put(self, key, value):
		new = DSAHashEntry(key, value)
		idx = self.hash(key)
		if self.shouldResize():
			new_size = self.nextPrime(int(self.size + 1))
			self.resize(new_size)
		elif self.hashtable[idx] == None:
			self.hashtable[idx] = new
			self.count += 1
		elif self.hashtable[idx].getState() in {0,1}:
			self.hashtable[idx] = new
			self.count += 1
		elif self.hashtable[idx].getState() == 2:
			if self.hashtable[idx].getKey() == key:
				print('same key error')
				return
			step = self.stepHash(key)
			found = False
			while self.hashtable[idx] != None and found != True:
				if self.hashtable[idx].getState() in {0,1}:
					found = True
				else:
					idx = idx + step
					if idx >= self.size:
						idx = (idx - self.size)
			self.hashtable[idx] = new
			self.count += 1
		else:
			print('error in put()')
			return None

		return 'added at: ' + str(idx)


	def get(self, key):
		idx = self.hash(key)
		found = False

		while not found:
			if self.hashtable[idx] == None:
				print('key does not exist')
				return
			elif self.hashtable[idx].getKey() == key and self.hashtable[idx].getState() == 2:
				found = True
			elif self.hashtable[idx].getState() in {0,1,2}:
				step = self.stepHash(key)
				idx = idx + step
				if idx >= self.size:
					idx = (idx - self.size)

		return self.hashtable[idx]

	def remove(self, key):
		idx = self.hash(key)
		found = False

		while not found:
			if self.hashtable[idx] == None:
				print('key does not exist')
				return
			elif self.hashtable[idx].getKey() == key and self.hashtable[idx].getState() == 2:
				found = True
			elif self.hashtable[idx].getState() in {1,2}:
				step = self.stepHash(key)
				idx = idx + step
				if idx >= self.size:
					idx = (idx - self.size)

		val = self.hashtable[idx]
		self.hashtable[idx].setState(1)
		self.count -= 1
		return val

	def shouldResize(self):
		lf = self.count/self.size
		if lf > 0.75:
			resize = True
		else:
			resize = False

		return resize

	def resize(self, size):
		old = copy.deepcopy(self.hashtable)
		self.hashtable = np.empty(size, dtype=object)
		self.size = size
		self.count = 0

		for i in old:
			if i == None:
				pass
			elif i.getState() == 2:
				self.put(i.getKey(), i.getValue())


	def hash(self, key):
		key = str(key)
		key = bytearray(key.encode())
		a = 63689
		b = 378551
		hashIdx = 0

		for i in range(0, len(key)):
			hashIdx = (hashIdx * a) + key[i]
			a *= b

		return hashIdx % self.size

	def stepHash(self, key):
		key = self.hash(key)
		max_step = self.nextPrime(int(self.size * 0.25))
		return (max_step - (key % max_step))



class DSAHashEntry:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.state = 2

	def __str__(self):
		return str(str(self.key) + ':' + str(self.value))

	def getKey(self):
		return self.key
	
	def getValue(self):
		return self.value

	def getState(self):
		return self.state

	def setState(self, state):
		self.state = state

	def setFree(self):
		self.state = 0

	def setPrevUsed(self):
		self.state = 1

	def setUsed(self):
		self.state = 2




