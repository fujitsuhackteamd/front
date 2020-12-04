# -*- coding: utf-8 -*-
from flask import Flask, render_template, request

app = Flask(__name__, static_folder='./load', template_folder='./html_file')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login.html')
def login():
    return render_template('login.html')


# ログインフォームのテスト
@app.route('/login_result', methods=['GET', 'POST'])
def login_result():
    return "email：" + request.form["email"] + "　　pass:" + request.form["password"]


@app.route('/form.html')
def form():
    return render_template('form.html')

@app.route('/form_result', methods=['GET', 'POST'])
def form_result():
    return "email：" + request.form["age"] 


if __name__ == '__main__':
    app.run(debug=True)