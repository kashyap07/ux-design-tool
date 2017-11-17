from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import csv
from collections import Counter
import sqlite3

app = Flask(__name__)
CORS(app)
#app.config.from_pyfile('config.py')

@app.route('/')
@app.route('/send', methods=["GET", "POST"])
def send():
	json_dict = request.get_json(force=True);
	xcoord = json_dict['x']
	ycoord = json_dict['y']
	time = json_dict['time']
	print("xcoord",xcoord)
	print("ycoord", ycoord)
	print("Time",time)
	
	with open("csv1.csv", "a") as file:
		csv_file = csv.writer(file)
		csv_file.writerow([str(xcoord), str(ycoord), str(time)])
	file.close()
	
	conn = sqlite3.connect('example.db')
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
	
	with open("csv1.csv") as f: #database1.csv is the file that Vandana creates.
		#header = next(f).strip().split(',')
		new = []
		for i in f:
			if(i != None):
				new.append(i)
	
		for x in new:
			if(x != '\n'):
				 x = x.strip().split(',')
				 #print(int(x[0]))
				 X.append(int(x[0]))
				 Y.append(int(x[1]))

	Z=zip(X,Y)
	resultList = list(Z)
	#print(resultList)

	counter=Counter(resultList)
	#print(counter)

	with open('input.csv', 'w') as f:
		writer = csv.writer(f) 
		writer.writerow(['x','y','value'])
		for k,v in counter.items():
			writer.writerow([k[0], k[1], v])
	
	return 'Successful'
		
if __name__ == '__main__':
	app.run(debug=True)
