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
@app.route('/send3', methods=["GET", "POST"])
def send3():
	json_dict = request.get_json(force=True);
	poscoord = json_dict['position']
	timespentcoord = json_dict['timeSpent']
	print("position",poscoord)
	print("timeSpent", timespentcoord)
	
	with open("input.csv", "a") as file:
		csv_file = csv.writer(file)
		csv_file.writerow([str(poscoord), str(timespentcoord)])
		
	conn = sqlite3.connect('example.db')
	c = conn.cursor()
	c.execute('''drop table if exists feature3''')
	c.execute('''CREATE TABLE feature3 (poscoord text, timespentcoord text)''')
	conn.commit()
	l=[(str(poscoord), str(timespentcoord))]
	c.executemany('INSERT INTO feature3 VALUES (?,?)', l)
	
	for row in c.execute('SELECT * FROM feature3 ORDER BY poscoord'):
		print("ROW", row)
		
	return 'Successful'
        
if __name__ == '__main__':
	app.run(debug=True)
