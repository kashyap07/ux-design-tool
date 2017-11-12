from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import csv

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
	#print("xcoord",xcoord)
	#print("ycoord", ycoord)
	
	with open("csv1.csv", "a") as file:
		csv_file = csv.writer(file)
		csv_file.writerow([str(x), str(y), str(time)])
	
	X=[]
	Y=[]
	with open('csv1.csv') as f: #csv1.csv is the file that Vandana creates.
    header = next(f).strip().split(',')
    for x in f:
         x = x.strip().split(',')
         X.append(int(x[0]))
         Y.append(int(x[1]))
	#print(X)
	#print(Y)

	Z=zip(X,Y)
	resultList = list(Z)
	#print(resultList)

	counter=Counter(resultList)
	#print(counter)

	with open('database1_heatmaps.csv', 'w') as f:#database1_heatmaps is what Yash will read.
		writer = csv.writer(f) 
		writer.writerow(['Coordinates','Time_Spent'])
		for k,v in counter.items():
			writer.writerow([k,v])
		
	return 'Successful'
        
if __name__ == '__main__':
	app.run(debug=True)
