from flask import Flask, render_template, request, redirect
import datetime
import pytz # timezone 
import requests
import os



app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
	return render_template('index.html')

@app.route('/about')
def profile():
	return render_template('about.html')  

@app.route('/work')
def work():
	# testing stuff
	return render_template('work.html')


if __name__ == '__main__':
	app.run(debug=True)
