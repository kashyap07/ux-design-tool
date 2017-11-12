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
	poscoord = json_dict['position']
	timespentcoord = json_dict['timeSpent']
	#print("xcoord",xcoord)
	#print("ycoord", ycoord)
	
	with open("csv3.csv", "a") as file:
		csv_file = csv.writer(file)
		csv_file.writerow([str(poscoord), str(timespentcoord)])
	
	#csv3.csv is what Yash will raed directly	
	return 'Successful'
        
if __name__ == '__main__':
	app.run(debug=True)
