from DSAHash import *
#from Processing import *
#import matplotlib.pyplot as plt

## REMEMBER TO UNCOMMENT OUT THE RETURN STATEMENT ON THE PUT() FUNCTION WHEN SHOWCASING TEST FILE

# FITS TABLE?
# PROPERTY 1: YES... all hashed indexes are mod'd by the length of the current hash table, thus it is
# impossible for them to be any larger than the hash table itself

# FAST TO COMPUTE?
# PROPERTY 2: YES... hash function used was quite a simple one from the lecture notes, it uses the
# 'a' and 'b' value to edit the bytecode array of the key's string value, and then the hashed int
# is indexed on a numpy array making it very fast

# REPEATABLE?
# PROPERTY 3: YES... as is shown when I test my hash() function in this file, calling the function
# with the exact same key will result in a hashed index which is identical, regardless of when
# the function was actually called - it's repeatable!

# DISTRIBUTES KEYS EVENLY?
# PROPERTY 4: YES... double hashing is used which means that primary and secondary clustering
# should be avoided when collisions are met - no bunching should occur - check distribution.png

print("CREATING HASH TABLE (10):")
ht = DSAHashTable(10)
print('size: ', ht.size)

print()

print("TESTING HASH()")
print('hashed: test1 -> ', ht.hash('test1'))
print('hashed: test1 -> ', ht.hash('test1'))
print('hashed: 2 -> ', ht.hash(2))
print('hashed: 2 -> ', ht.hash(2))
print('hashed: hfdxhgudsjhfj -> ', ht.hash('hfdxhgudsjhfj'))
print('hashed: hfdxhgudsjhfj -> ', ht.hash('hfdxhgudsjhfj'))
print('hashed: xd -> ', ht.hash('xd'))
print('hashed: xd -> ', ht.hash('xd'))
print('hashed: a -> ', ht.hash('a'))
print('hashed: a -> ', ht.hash('a'))

print()

print("TESTING STEPHASH()")
print('stepHashed: a -> ', ht.stepHash('a'))
print('(9 + 3) - 11 = ', str((9 + 3)-11), ' -> is new index after collision?')

print()

print("TESTING THE COLLISION:")
print('xd -> should go to 9')
print(ht.put('xd', 1337))
print('a -> should collide on 9')
print('a -> should then go to 1')
print(ht.put('a', 80085))

print()

print("TESTING GENERAL PUT()")
print('adding: some_key')
print(ht.put('some_key', 13371))
print('adding: ab')
print(ht.put('ab', 13372))
print('adding: hello')
print(ht.put('hello', 13373))
print('!attempting to add a NOT unique key!')
print('adding: hello')
ht.put('hello', 1337)

print()

print("TESTING GENERAL GET()")
print('getting: some_key')
print(ht.get('some_key'))
print('getting: hello')
print(ht.get('hello'))
print('!attempting to get a NON EXISTENT key!')
print('getting: this_isnt_existent')
ht.get('this_isnt_existent')

print()

#print(ht.count / len(ht.hashtable))

print()

print("TESTING GENERAL REMOVE()")
print('removing: some_key')
print(ht.remove('some_key'))
print('removing: xd')
print(ht.remove('xd'))
print("!attempting to get 'a' which depends on 'xd' (earlier collision)!")
print('getting: a')
print("!attempting to remove a NON EXISTENT key!")
print('removing: gsgdfgfdg')
ht.remove('gsgdfgfdg')

print()

print('TESTING SHOULDRESIZE()')
print('the load factor is currently: ', ht.count / len(ht.hashtable))
print(ht.shouldResize())

print()

print('TESTING RESIZE()')
print('current size: ', len(ht.hashtable))
print('current count: ', ht.count)
print('  ',ht.put('b', 2))
print('  ',ht.put('c', 2))
print('  ',ht.put('d', 2))
print('  ',ht.put('e', 2))
print('  ',ht.put('f', 2))
print('  ',ht.put('g', 2))
print('  ',ht.put('h', 2))
print('current size: ', len(ht.hashtable))
print('current count: ', ht.count)
print('  ',ht.put('i', 2))
print('  ',ht.put('j', 2))
print('  ',ht.put('k', 2))
print('  ',ht.put('l', 2))
print('current size: ', len(ht.hashtable))
print('current count: ', ht.count)

print()

print("QUICK LOOK AT THE CURRENT HASH TABLE")
for i in ht.hashtable:
	print(i, end = ' | ')

print()
print()

# importing names csv
# pp = Processing()
# names = Processing().readCSV('RandomNames7000(1).csv', 1)

# print("CREATING A HASH TABLE (10 000): ")
# ht2 = DSAHashTable(10000)

# for i in names:
# 	ht2.put(i[0], i[1])

# print()

# print("A QUICK GET() AND REMOVE()")
# print('getting: 14007241')
# print(ht2.get('14007241'))
# print('removing: 14007241')
# print(ht2.remove('14007241'))
# print('getting: 14007241')
# ht2.get('14007241')

# print()

# y = np.empty(len(ht2.hashtable), dtype=int)

# print("LOOKING AT THE CURRENT NAMES HASH TABLE")
# for i,z in enumerate(ht2.hashtable):
# 	print(z, end = ' | ')
# 	if z != None:
# 		y[i] = np.random.uniform(low=200, high=2500)
# 	else:
# 		y[i] = np.random.uniform(low=-2500, high=-200)

# print()
# print()

#print(y)
# rng = np.random.RandomState(0)
# x = np.random.uniform(low=0.0, high=10007.0, size = 10007)
# colors = rng.rand(10007)
# sizes = 1000 * rng.rand(10007)

# my_dpi = 240
# plt.figure(figsize=(3200/my_dpi, 2400/my_dpi), dpi=my_dpi)

# plt.scatter(x, y, c = colors, alpha=0.3, s = sizes, cmap = 'viridis')

# plt.savefig('distribution.png')

# print("FIGURE OUTPUTTED TO: dsitribution.png")

