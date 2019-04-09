import pickle
import csv

with open('a_distance', 'rb') as picklefile:
	result = pickle.load(picklefile)

print(result)
print()
print('distance (metres)')
print(str(result['rows'][0]['elements'][0]['distance']['value']))
print('duration (minutes)')
print(str(result['rows'][0]['elements'][0]['duration']['value']))
if str(result['rows'][0]['elements'][0]['status']) == 'OK':
	print('yes')

with open('api_hope.pickle', 'rb') as picklefile:
	test = pickle.load(picklefile)

for i in test:
	for j in i:
		print(j)

with open('electorate_distance_time.csv', 'w') as csv_file:
	csv_writer = csv.writer(csv_file, delimiter=',')
	csv_writer.writerow(['from_State','from_Division', 'from_Latitude', 'from_Longitude', 'to_State', 'to_Division', 'to_Latitude', 'to_Longitude', 'distance_metres', 'time_minutes'])
	for i in test:
		for j in i:
			csv_writer.writerow(j)