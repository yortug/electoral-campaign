from Processing import *
from Region import *
import sys
sys.path.append("../")
from bs4 import BeautifulSoup
import requests
import re

## FINDING COORDS FOR EACH ELECTORATE

pp = Processing()

the_data = pp.unserialize('australia4.pickle')

Australia = Country('Australia', len(the_data))
Australia.setStates(the_data)

test = []

#print(Australia)
#print('==================')
for i in Australia.getStates():
	#print(i)
	for j in i.getElectorates():
		#print('\t ', j)
		test.append([i.getCode(), j.getDivName()])
		# for k in j.getParties():
		# 	#print('\t\t ', k)
		# 	for x in k.getCandidates():
		# 		#print('\t\t\t ', x)


print()
print()
# print(test)

# html_file = requests.get('https://en.wikipedia.org/wiki/Division_of_Blair').text
# soup = BeautifulSoup(html_file, 'lxml')
# x = soup.find('span', attrs={'class':'geo-dec'}).text
# x = re.sub('[^0-9,. ]', '', x)
# x = 'Blair ' + x
# x = x.split(' ')

# print(x)

test2 = []
count=0
for i in test:
	html_file = requests.get('https://en.wikipedia.org/wiki/Division_of_' + str(i[1])).text
	soup = BeautifulSoup(html_file, 'lxml')
	x = soup.find('span', attrs={'class':'geo-dec'})
	if x != None:
		#print(i + ' : ' + x.text)
		x = re.sub('[^0-9,. ]', '', x.text).replace(' ', '?')

		x = i[0] + '?' + i[1] + '?' + '-'+x
		x = x.split('?')
		print(count,x)
		test2.append(x)
	else:
		#print(i + ' : ' + 'NONE')
		x = i[0] + '?' + i[1] + '?' + 'NONE' + '?' + 'NONE'
		x = x.split('?')
		print(count,x)
		test2.append(x)
	count+=1

#print(test2)

test2[58][2] = '-27.793072' 
test2[58][3] = '153.356213'
print(test2[58])

with open('electorate_coords.csv', 'w') as csv_file:
	csv_writer = csv.writer(csv_file, delimiter=',')
	csv_writer.writerow(['State','Division', 'Latitude', 'Longitude'])
	for i in test2:
		csv_writer.writerow(i)


