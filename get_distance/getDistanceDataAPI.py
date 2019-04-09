import googlemaps
from datetime import datetime
import pickle
import requests
import itertools
import sys
sys.path.append("../")
from Processing import *
from Region import *

key = ''

pp = Processing()

the_data = pp.unserialize('australia4.pickle')

Australia = Country('Australia', len(the_data))
Australia.setStates(the_data)

test = []

for i,z in enumerate(Australia.getStates()):
	print(z.getCode())
	test.append(list())
	for j in z.getElectorates():
		test[i].append(j.getDivName())
		#print(j.getDivName())

test[0].append('Sydney Airport')
test[0].append('Melbourne Airport')

test[1].append('Sydney Airport')

test[2].append('Darwin Airport')

test[3].append('Brisbane Airport')

test[4].append('Adelaide Airport')

test[5].append('Hobart Airport')

test[6].append('Melbourne Airport')

test[7].append('Perth Airport')

print()

x = pp.readCSV('electorate_coords.csv',2)

#print(x)

test2 = []

for j,k in enumerate(test):
	test2.append(list())
	for i,z in enumerate(itertools.combinations(test[j], 2)):
		source = list(pp.getRowsWhere(x, 1, z[0])[0])
		#print(i,source)
		dest = list(pp.getRowsWhere(x, 1, z[1])[0])
		#print(i,dest)
		source.extend(dest)

		#print(source)
		test2[j].append(source)

# count = 0
# for i in test2:
# 	for z in i:
# 		print(str(count),'\t',str(z))
# 		count+=1

print()

count=0
test3 = test2
for i,z in enumerate(test2):
	for j,x in enumerate(z):	
		orig_coord = x[2], x[3]
		dest_coord = x[6], x[7]
		url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins={}&destinations={}&mode=driving&language=en-EN&key={}&sensor=false".format(",".join(map(str, orig_coord)),",".join(map(str, dest_coord)),"".join(map(str, key)))
		result = requests.get(url).json()
		print(result)
		if str(result['rows'][0]['elements'][0]['status']) == 'OK':
			test3[i][j].append(str(result['rows'][0]['elements'][0]['distance']['value']))
			test3[i][j].append(str(result['rows'][0]['elements'][0]['duration']['value']))
		else:
			test3[i][j].append('NONE')
			test3[i][j].append('NONE')
		count+=1

for i in test3:
	for z in i:
		print('\t',str(z))

with open('api_hope.pickle', 'wb') as data:
	pickle.dump(test3, data)



