from flask import Flask
from flask import request
from datetime import date
import json
from Activity import Activity

# creating flask application
app = Flask(__name__)
app.config["REDIS_URL"] = "redis://localhost"

@app.route('/store', methods=['POST'])
def store_data():
	if(request.method == 'POST'):
		if('data' in request.form and request.form['data']):
			try:
				data = json.loads(request.form['data']) # data in json
				activity = Activity()
			except Exception as e:
				print (str(e))
			finally:
				activity.insert_activity(data)
				activity.save()
			return '1'
	else:
		return 'IncompleteArgsError'

if __name__ == "__main__":
	app.run(threaded=True, host="0.0.0.0", port="8888")
