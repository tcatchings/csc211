#!/usr/bin/env python3

from flask import Flask, request, render_template
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD']=True

@app.route('/')
def index():
    return '<h1>CSC211 HW 7: Flask Assigment</h1>'

@app.route('/list')
@app.route('/list/<int>')
def list(int=None):
    return render_template('list.html', int=int)
