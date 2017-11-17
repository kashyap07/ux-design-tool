import csv
from datetime import datetime
import json

#05:30
def __datetime(date_str):
    return datetime.strptime(date_str, '%H:%M')

input_file = "input.csv"

time_container = list(map(lambda x:[x,0],range(0,24)))
time_container.insert(0, ["Time","y"])
#print(time_container)

JSON_PATH = 'd2.json'

with open(input_file,'r') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			s_time = row[0]
			e_time = row[1]
			s_hour = int(s_time.split(":")[0])
			e_hour = int(e_time.split(":")[0])
			e_min = int(e_time.split(":")[1])
			#print(s_hour)

			start = __datetime(s_time)
			end = __datetime(e_time)
			#print((end - start).seconds/60)

			diff = (end - start)
			diff_min = diff.seconds/60
			diff_hour = diff.seconds/3600
			#print(diff_min)
			count = 0
			while(diff_min>0):
				time_container[s_hour + count][1] += 1
				count += 1
				diff_min -= 60
			if(e_min>0 and s_hour != e_hour and e_hour!=24):
				time_container[s_hour + count][1] += 1

#print(time_container)
with open("output.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(time_container)













