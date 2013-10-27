import os
import json
from flask import Flask
from flask import render_template, send_from_directory, Response, url_for, request

# app initialization
app = Flask(__name__)
app.config.update(
	DEBUG = True,
	SECRET_KEY = 'e6373add09271e1087155c903f0a593012399435136372cc'
)

# controllers
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

# special file handlers
@app.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static'), 'img/favicon.ico')

# error handlers
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

# server launchpad
if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)