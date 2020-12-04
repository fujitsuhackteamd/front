# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__, static_folder='./load', template_folder='./html_file')

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)