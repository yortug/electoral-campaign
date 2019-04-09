from linkedLists import *

class DSAStack():
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

	def __getitem__(self, index):
		count = 0
		cur = self.items.head
		if index > len(self):
			print("Index is out of bounds")
		else:
			while count < index:
				cur = cur.next
				count += 1

		return cur

	def isEmpty(self):
		return self.items.isEmpty()

	# def isFull(self):
	# 	return self.count == self.items.size

	# def getCount(self):
	# 	return len(self.items)

	
	def push(self, value):
		self.items.insertLast(value)
		#print('push: ',self.items.displayList())
		
	def top(self):
		return self.items.peekLast()

	def pop(self):
		if self.isEmpty():
			print('Stack is empty.')
		else:
			#try:
				return self.items.removeLast()
			#finally:
				#print('pop: ', self.items.displayList())
