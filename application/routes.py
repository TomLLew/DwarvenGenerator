from flask import render_template, request, redirect, url_for
from application import frontend
import requests, json


@frontend.route('/')
@frontend.route('/home', methods=['GET', 'POST'])
def home():
    form = request.form.get('gender')
    gender = {"gender":"none"}
    gender["gender"] = form
    stats = {}
    if request.method == 'POST':
        response = requests.post('http://127.0.0.1:5003/stats', params=gender).json()
        stats.update(response)
        return response
    return render_template('home.html', title='Dwarven Generator')