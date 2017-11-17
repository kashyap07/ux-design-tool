import csv
import json
import collections

CSV_PATH = 'input.csv'
JSON_PATH = 'd3.json'

r = csv.reader(open(CSV_PATH))
lines = [l for l in r]
lines.insert(0,["label","y"])
with open("input.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(lines)


csv_file = csv.DictReader(open(CSV_PATH, 'r'))

#print(csv_file)

json_list = []
for row in csv_file:
    #print(type(row))
    x = [("label", row["label"]), ("y", row["y"])]
    json_list.append(collections.OrderedDict(x))

#print(json_list)

a = json.dumps(json_list)
b = "d3 = '"
c = b + a+"';"
file(JSON_PATH, 'w').write(c)

