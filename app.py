from flask import Flask, render_template
from flask import request, Response
from datetime import date
import json
import csv
import collections
from collections import Counter
from datetime import datetime
import sqlite3

# creating flask application
app = Flask(__name__)
# app.config["REDIS_URL"] = "redis://localhost"

# index route
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/formgen')
def appgen():
	return render_template('Form_index.html')

@app.route('/download.html', methods=['POST'])
def send():
	res = Response(request.form['fstring'])
	res.headers["Content-Type"] = "application/force-download"
	return res

# static page rendering
@app.route('/<string:page_name>/')
def static_page(page_name):
    return render_template('%s.html' % page_name)

@app.route('/clickdata', methods=["GET", "POST"])
def click_data_store():
	json_dict = request.get_json(force=True);
	xcoord = json_dict['x']
	ycoord = json_dict['y']
	time = json_dict['time']
	print("xcoord", xcoord)
	print("ycoord", ycoord)
	print("Time", time)
	
	with open("data/csv1.csv", "a") as file:
		csv_file = csv.writer(file)
		csv_file.writerow([str(xcoord), str(ycoord), str(time)])
	file.close()
	
	conn = sqlite3.connect('data/clickdata.db')
	c = conn.cursor()
	c.execute('''drop table if exists feature1''')
	c.execute('''CREATE TABLE feature1 (xcoord text, ycoord text, time text)''')
	conn.commit()
	l=[(str(xcoord), str(ycoord), str(time))]
	c.executemany('INSERT INTO feature1 VALUES (?,?,?)', l)
	
	for row in c.execute('SELECT * FROM feature1 ORDER BY xcoord'):
		print("ROW", row)
	X=[]
	Y=[]
	
	with open("data/csv1.csv") as f: #database1.csv is the file that Vandana creates.
		new = []
		for i in f:
			if(i != None):
				new.append(i)
	
		for x in new:
			if(x != '\n'):
				x = x.strip().split(',')
				X.append(int(x[0]))
				Y.append(int(x[1]))

	Z=zip(X,Y)
	resultList = list(Z)
	counter=Counter(resultList)

	with open('data/clickdata.csv', 'w') as f:
		writer = csv.writer(f) 
		writer.writerow(['x','y','value'])
		for k,v in counter.items():
			writer.writerow([k[0], k[1], v])
	
	return 'Success'

@app.route('/visitdata', methods=["GET", "POST"])
def visit_data_store():
	json_dict = request.get_json(force=True);
	fromcoord = json_dict['from']
	tocoord = json_dict['to']
	print("from",fromcoord)
	print("to", tocoord)
	
	with open("data/visitdata.csv", "a") as file:
		csv_file = csv.writer(file)
		csv_file.writerow([str(fromcoord), str(tocoord)])
	file.close()

	return 'Success'

@app.route('/scrolldata', methods=["GET", "POST"])
def scroll_data_store():
	json_dict = request.get_json(force=True);
	poscoord = json_dict['position']
	timespentcoord = json_dict['timeSpent']
	print("position", poscoord)
	print("timeSpent", timespentcoord)
	
	with open("data/scrolldata.csv", "a") as file:
		csv_file = csv.writer(file)
		csv_file.writerow([str(poscoord), str(timespentcoord)])
		
	conn = sqlite3.connect('data/scrolldata.db')
	c = conn.cursor()
	c.execute('''drop table if exists feature3''')
	c.execute('''CREATE TABLE feature3 (poscoord text, timespentcoord text)''')
	conn.commit()
	l=[(str(poscoord), str(timespentcoord))]
	c.executemany('INSERT INTO feature3 VALUES (?,?)', l)
	
	for row in c.execute('SELECT * FROM feature3 ORDER BY poscoord'):
		print("ROW", row)
		
	return 'Success'

@app.route('/getheatmap', methods=['GET'])
def get_heatmap():
	CSV_PATH = 'data/clickdata.csv'
	csv_file = csv.DictReader(open(CSV_PATH, 'r'))

	json_list = []
	for row in csv_file:
		x = [("x", row["x"]),("y", row["y"]), ("value", row["value"])]
		json_list.append(collections.OrderedDict(x))

	return_json_obj = json.dumps(json_list)
	return return_json_obj


def __datetime(date_str):
    return datetime.strptime(date_str, '%H:%M')

@app.route('/getvisitstats', methods=['GET'])
def get_visits():
	input_file = "data/visitdata.csv"

	time_container = list(map(lambda x:[x,0],range(0,24)))
	# time_container.insert(0, ["Time","y"])

	with open(input_file,'r') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			s_time = row[0]
			e_time = row[1]
			s_hour = int(s_time.split(":")[0])
			e_hour = int(e_time.split(":")[0])
			e_min = int(e_time.split(":")[1])

			start = __datetime(s_time)
			end = __datetime(e_time)

			diff = (end - start)
			diff_min = diff.seconds/60
			diff_hour = diff.seconds/3600
		
			count = 0
			while(diff_min>0):
				time_container[s_hour + count][1] += 1
				count += 1
				diff_min -= 60
			if (e_min>0 and s_hour != e_hour and e_hour!=24):
				time_container[s_hour + count][1] += 1

	json_list = []
	d = {}

	for i in time_container:
		d[i[0]] = i[1]

	return_json_obj = json.dumps(d)
	return return_json_obj

@app.route('/getscrollstats', methods=['GET'])
def get_scrolls():
	CSV_PATH = 'data/scrolldata.csv'

	r = csv.reader(open(CSV_PATH))
	lines = [l for l in r]

	json_list = []

	d = {}

	for i in lines:
		d[i[0]] = i[1]

	return_json_obj = json.dumps(d)
	return return_json_obj

if __name__ == "__main__":
	app.run(
		debug=True,
		threaded=True,
		host=('0.0.0.0'),
		port=8888
	)
	