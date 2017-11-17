from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import csv

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
	
	with open("input.csv", "a") as file:
		csv_file = csv.writer(file)
		csv_file.writerow([str(fromcoord), str(tocoord)])
	file.close()	
	return 'Successful'
        
if __name__ == '__main__':
	app.run(debug=True)
