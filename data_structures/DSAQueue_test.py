from DSAQueue import *

numPassed = 0
numTests = 0
qq = None

# using linked list so none of the count tests will work and it can't get full

# test 1 - creation & isEmpty()
print("Testing queue creation and isEmpty():")
try:
	numTests += 1
	qq = DSAQueue()
	if not qq.isEmpty():
		raise ListError("Count should begin at zero (0)")
	else:
		numPassed += 1
		print("Passed")
except:
	print("Failed")

# # test 2 - getCount() when empty
# print("Testing getCount() when empty:")
# try:
# 	numTests += 1
# 	if qq.getCount() != 0:
# 		raise ValueError("Queue length should be equal to # of elements currently in queue (0)")
# 	else:
# 		numPassed += 1
# 		print("Passed")
# except:
# 	print("Failed")

# test 3 - peek() when empty
print("Testing peek() when empty:")
try:
	numTests += 1
	if qq.peek() != None:
		raise ListError("A peek on an empty queue should return null (None)")
	else:
		numPassed += 1
		print("Passed")
except:
	print("Failed")

# test 4 - dequeue from empty
print("Testing dequeue() when empty:")
try:
	numTests += 1
	if qq.dequeue() != None:
		raise ListError("A dequeue on an empty list should return null (None)")
	else:
		numPassed += 1
		print("Passed")
except:
	print("Failed")

# test 5 - enqueue() from empty
print("Testing enqueue():")
try:
	numTests += 1
	qq.enqueue(2)
	qq.enqueue(32.45)
	qq.enqueue('hello')
	qq.enqueue('world')
	qq.enqueue('spam')
	numPassed += 1
	print("Passed")
except:
	print("Failed")

# # test 6 - getCount() after enqueue
# print("Testing getCount() with elements:")
# try:
# 	numTests += 1
# 	if qq.getCount() != 5:
# 		raise ValueError("Queue length should be equal to # of elements currently in queue (5)")
# 	else:
# 		numPassed += 1
# 		print("Passed")
# except:
# 	print("Failed")

# test 7 - dequeue() on a queue with multiple elements
print("Testing dequeue() with elements:")
try:
	numTests += 1
	if qq.dequeue() != 2:
		raise ValueError("Dequeue should return first, front value (2)")
	elif qq.dequeue() != 32.45:
		raise ValueError("Dequeue should return first, front value (32.45)")
	else:
		numPassed += 1
		print("Passed")
except:
	print("Failed")

# # test 7 - getCount() after dequeue
# print("Testing getCount() after a dequeue:")
# try:
# 	numTests += 1
# 	if qq.getCount() != 3:
# 		raise ValueError("Queue length should be equal to # of elements currently in queue (3)")
# 	else:
# 		numPassed += 1
# 		print("Passed")
# except:
# 	print("Failed")

#test 8 - peek after dequeue and enqueue
print("Testing peek() after a dequeue & enqueue:")
try:
	numTests += 1
	if qq.peek() != 'hello':
		raise ListError("Current front element should be 'hello'")
	qq.enqueue(3)
	qq.enqueue(5)
	qq.enqueue(11)
	qq.dequeue()
	if qq.peek() != 'world':
		raise ListError("Current front element should be 'world'")
	else:
		numPassed += 1
		print("Passed")
except:
	print("Failed")

# test 9 - dequeue until empty
print("Testing dequeue() until empty:")
try:
	numTests += 1
	qq.dequeue()
	qq.dequeue()
	qq.dequeue()
	qq.dequeue()
	qq.dequeue()
	if qq.dequeue() != None:
		raise ListError("A dequeue on an empty list should return null (None)")
	else:
		numPassed += 1
		print("Passed")
except:
	print("Failed")

# test 10 - enqueue until full (testing isFull())
print("Testing enqueue() until full:")
try:
	numTests += 1
	for _ in range(100):
		qq.enqueue('eggs')
	#print(qq.getCount())
	if qq.enqueue(2) != None:
		raise ListError("An enqueue attempt on a full queue should return null (None)")
	else:
		numPassed += 1
		print("Passed")
except:
	print("Failed")

# # test 11 - isFull() functions properly
# print("Testing isFull():")
# try:
# 	numTests += 1
# 	if not qq.isFull():
# 		raise ListError("A full queue should return True when queried by isFull()")
# 	else:
# 		numPassed += 1
# 		print("Passed")
# except:
# 	print("Failed")

# print test summary
print("\nNumber PASSED: ", numPassed, "/", numTests)
print("-> ", numPassed/numTests*100, "%\n")

