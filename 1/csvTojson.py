import csv
import json
import collections

CSV_PATH = 'input.csv'
JSON_PATH = 'd1.json'

csv_file = csv.DictReader(open(CSV_PATH, 'r'))

#print(csv_file)

json_list = []
for row in csv_file:
    #print(type(row))
    x = [("x", row["x"]),("y", row["y"]), ("value", row["value"])]
    json_list.append(collections.OrderedDict(x))

#print(json_list)

a = json.dumps(json_list)
b = "d1 = '"
c = b + a+"';"
#file(JSON_PATH, 'w').write(c)
f=open(JSON_PATH,"w")
f.write(c)

