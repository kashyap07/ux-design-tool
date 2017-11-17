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
@app.route('/send2', methods=["GET", "POST"])
def send2():
	#print("hello")
	json_dict = request.get_json(force=True);
	fromcoord = json_dict['from']
	tocoord = json_dict['to']
	print("from",fromcoord)
	print("to", tocoord)
	
	with open("csv2.csv", "a") as file:
		csv_file = csv.writer(file)
		csv_file.writerow([str(fromcoord), str(tocoord)])	
	file.close()
	
	conn = sqlite3.connect('example.db')
	c = conn.cursor()
	c.execute('''drop table if exists feature2''')
	c.execute('''CREATE TABLE feature2 (fromcoord text, tocoord text)''')
	conn.commit()
	l=[(str(fromcoord), str(tocoord))]
	c.executemany('INSERT INTO feature2 VALUES (?,?)', l)
	
	for row in c.execute('SELECT * FROM feature2 ORDER BY fromcoord'):
		print("ROW", row)
		
	'''
	fromTime=[]
	endTime=[]
	count=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	with open("csv2.csv") as f: 
		new = []
		for i in f:
			if(i != '\n'):
				new.append(i)
		#print(new)
		
	for x in new:
		a=x.split(",")
		a1=a[0][11:16]#Gives the Start Time
		a2=a[1][11:16]#Gives the End Time
		a=a1[0:2]
		b=a2[0:2]
		#print("A1",a1,"A2",a2,"a",a,"b",b)
		
		for i in range(int(a),int(b)+1):
			count[i]=count[i]+1
		#for i in range(len(count)):
			#print("I,Count",i,count)
	
	with open('feature2_updated.csv','a') as file:
		#print("Hello")
		writer = csv.writer(file)
		for i in range(len(count)):
			#print("COUNT",count)
			writer.writerow([count[i]])
	'''
	return 'Successful'
        
if __name__ == '__main__':
	app.run(debug=True)
