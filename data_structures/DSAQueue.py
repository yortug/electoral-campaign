from linkedLists import *

class DSAQueue():
	"""docstring for DSAStack"""
	def __init__(self):
		self.items = DSALinkedList()

	def __str__(self):
		x = [i for i in self.items]
		return str(x)
	
	def __len__(self):
		if self.isEmpty():
			return 0
		else:
			count = 0
			for i in self.items:
				count+=1
			return count

	def __iter__(self):
		for i in self.items:
			yield i

	def isEmpty(self):
		return self.items.isEmpty()

	# def isFull(self):
	# 	return self.count == self.items.size

	# def getCount(self):
	# 	return self.count

	def enqueue(self, value):
		self.items.insertFirst(value)

	def peek(self):
		return self.items.peekLast()

	def dequeue(self):
		if self.isEmpty():
			print('Queue is empty.')
		else:
			return self.items.removeLast()

