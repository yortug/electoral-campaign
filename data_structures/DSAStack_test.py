from DSAStack import *

numPassed = 0
numTests = 0
ss = None

# using linked list so none of the count tests will work and it can't get full

# test 1 - creation & isEmpty()
print("Testing stack creation and isEmpty():")
try:
	numTests += 1
	ss = DSAStack()
	if not ss.isEmpty():
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
# 	if ss.getCount() != 0:
# 		raise ValueError("stack length should be equal to # of elements currently in stack (0)")
# 	else:
# 		numPassed += 1
# 		print("Passed")
# except:
# 	print("Failed")

# test 3 - pop() when empty
print("Testing pop() when empty:")
try:
	numTests += 1
	if ss.pop() != None:
		raise ListError("A pop on an empty stack should return null (None)")
	else:
		numPassed += 1
		print("Passed")
except:
	print("Failed")

# test 4 - pop from empty
print("Testing pop() when empty:")
try:
	numTests += 1
	if ss.pop() != None:
		raise ListError("A pop on an empty list should return null (None)")
	else:
		numPassed += 1
		print("Passed")
except:
	print("Failed")

# test 5 - push() from empty
print("Testing push():")
try:
	numTests += 1
	ss.push(2)
	ss.push(32.45)
	ss.push('hello')
	ss.push('world')
	ss.push('spam')
	numPassed += 1
	print("Passed")
except:
	print("Failed")

# # test 6 - getCount() after push
# print("Testing getCount() with elements:")
# try:
# 	numTests += 1
# 	if ss.getCount() != 5:
# 		raise ValueError("Stack length should be equal to # of elements currently in stack (5)")
# 	else:
# 		numPassed += 1
# 		print("Passed")
# except:
# 	print("Failed")

# test 7 - pop() on a stack with multiple elements
print("Testing pop() with elements:")
try:
	numTests += 1
	if ss.pop() != 'spam':
		raise ValueError("pop should return first, front value (spam)")
	elif ss.pop() != 'world':
		raise ValueError("pop should return first, front value (world)")
	else:
		numPassed += 1
		print("Passed")
except:
	print("Failed")

# # test 7 - getCount() after pop
# print("Testing getCount() after a pop:")
# try:
# 	numTests += 1
# 	if ss.getCount() != 3:
# 		raise ValueError("stack length should be equal to # of elements currently in stack (3)")
# 	else:
# 		numPassed += 1
# 		print("Passed")
# except:
# 	print("Failed")

#test 8 - pop after pop and push
print("Testing pop() after a pop & push:")
try:
	numTests += 1
	if ss.pop() != 'hello':
		raise ListError("Current front element should be 'hello'")
	ss.push(3)
	ss.push(5)
	ss.push(11)
	ss.pop()
	if ss.pop() != 5:
		raise ListError("Current front element should be 5")
	else:
		numPassed += 1
		print("Passed")
except:
	print("Failed")

# test 9 - pop until empty
print("Testing pop() until empty:")
try:
	numTests += 1
	ss.pop()
	ss.pop()
	ss.pop()
	if ss.pop() != None:
		raise ListError("A pop on an empty list should return null (None)")
	else:
		numPassed += 1
		print("Passed")
except:
	print("Failed")

# test 10 - push until full (testing isFull())
print("Testing push() until full:")
try:
	numTests += 1
	for _ in range(100):
		ss.push('eggs')
	#print(ss.getCount())
	if ss.push(2) != None:
		raise ListError("An push attempt on a full stack should return null (None)")
	else:
		numPassed += 1
		print("Passed")
except:
	print("Failed")

# # test 11 - isFull() functions properly
# print("Testing isFull():")
# try:
# 	numTests += 1
# 	if not ss.isFull():
# 		raise ListError("A full stack should return True when queried by isFull()")
# 	else:
# 		numPassed += 1
# 		print("Passed")
# except:
# 	print("Failed")

# print test summary
print("\nNumber PASSED: ", numPassed, "/", numTests)
print("-> ", numPassed/numTests*100, "%\n")


