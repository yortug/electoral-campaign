class DSAListNode():
	"""docstring for DSAListNode"""
	def __init__(self, value):
		self.value = value
		self.next = None
		self.prev = None

	# def getValue(self):
	# 	return self.value

	# def setValue(self, inValue):
	# 	self.value = inValue

	# def getNext(self):
	# 	return self.next

	# def setNext(self, newNext):
	# 	self.next = newNext


class DSALinkedList():
	"""docstring for DSALinkedList"""
	def __init__(self):
		self.head = None
		self.tail = None

	# def displayList(self):
	# 	if self.isEmpty():
	# 		print("List is empty.")
	# 	else:
	# 		count = 0
	# 		curNd = self.head
	# 		while curNd.next != None:
	# 			print(count, curNd.value)
	# 			curNd = curNd.next
	# 			count += 1
	# 		print(count, curNd.value)

	# def displayList(self):
	# 	if self.isEmpty():
	# 		return '[]'
	# 	else:
	# 		tidy = []
	# 		curNd = self.head
	# 		while curNd.next != None:
	# 			tidy.append(curNd.value)
	# 			curNd = curNd.next
	# 		tidy.append(curNd.value)
	# 		return tidy

	def __str__(self):
		x = [i for i in self]
		return str(x)

	def __getitem__(self, index):
		count = 0
		cur = self.head
		if index > len(self):
			print("Index is out of bounds")
		else:
			while count < index:
				cur = cur.next
				count += 1

		return cur

	def findNode(self, value):
		cur = self.head
		z = cur.value
		while z != value and cur.next != None:
			cur = cur.next
			z = cur.value

		return cur

	def deleteNode(self, value):
		dele = self.findNode(value)
		#print(self, 'MYSELF')
		#print(dele.value, 'YEEET')

		if self.head is None or dele is None: 
			return 
		if self.head == dele: 
			self.head = dele.next
			self.head.prev = None
		if self.tail == dele:
			self.tail = dele.prev
			self.tail.next = None
		if dele.next is not None: 
			dele.next.prev = dele.prev 
			dele.prev.next = dele.next
		# if dele.prev is not None:
		# 	dele.prev.next = dele.next
		# 	print(dele.prev, 'HERE FAM')
		# 	dele.next.prev = dele.prev

		


	def isEmpty(self):
		return self.head == None

	def insertFirst(self, newValue):
		newNd = DSAListNode(newValue)
		if self.isEmpty():
			self.head = newNd
			self.tail = newNd
		else:
			self.head.prev = newNd 
			newNd.next = self.head
			self.head = newNd
			newNd.prev = None

	def insertLast(self, newValue):
		newNd = DSAListNode(newValue)
		if self.isEmpty():
			self.head = newNd
			self.tail = newNd
		else:
			self.tail.next = newNd
			newNd.prev = self.tail
			self.tail = newNd
			newNd.next = None
			
	
	def peekFirst(self):
		if self.isEmpty():
			pass
		else:
			return self.head.value

	def peekLast(self):
		if self.isEmpty():
			pass
		else:
			return self.tail.value
	
	def removeFirst(self):
		if self.isEmpty():
			pass
		else:
			first = self.head.value
			self.head = self.head.next
			if self.isEmpty():
				pass
			else:
				self.head.prev = None
			return first

	def removeLast(self):
		if self.isEmpty():
			pass
		else:
			last = self.tail.value
			self.tail = self.tail.prev
			if self.tail == None:
				self.head = None
				return last
			else:
				self.tail.next = None
				return last

	def __len__(self):
		if self.isEmpty():
			return 0
		else:
			count = 0
			# curNd = self.head
			# while curNd != None:
			# 	count += 1
			# 	curNd = curNd.next
			for i in self:
				count += 1
			return count

	def __iter__(self):
		cursor = self.head
		while cursor != None:
			yield cursor.value
			cursor = cursor.next
		
		