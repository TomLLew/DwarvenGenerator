from flask import render_template, request, redirect, url_for
from application import app


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Dwarven Generator')