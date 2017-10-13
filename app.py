from flask import Flask, render_template
from flask import request
from datetime import date
import json
from Activity import Activity

# creating flask application
app = Flask(__name__)
app.config["REDIS_URL"] = "redis://localhost"


# index route
@app.route('/')
def index():
	return render_template('index.html')

# static page rendering
@app.route('/<string:page_name>/')
def static_page(page_name):
    return render_template('%s.html' % page_name)


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
	app.run(
		debug=True,
		threaded=True,
		host=('0.0.0.0'),
		port=8888
	)