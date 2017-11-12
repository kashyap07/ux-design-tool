import csv
import json
import collections

CSV_PATH = 'csv1.csv'
JSON_PATH = 'd3.json' #name of the feature

csv_file = csv.DictReader(open(CSV_PATH, 'r'))

json_list = []
for row in csv_file:
    print(type(row))
    x = [("label", row["label"]), ("y", row["y"])] #columns in the database
    json_list.append(collections.OrderedDict(x))
    
a = json.dumps(json_list)
b = "d3 = '"  #name of the feature
c = b + a+"';"
file(JSON_PATH, 'w').write(c)
