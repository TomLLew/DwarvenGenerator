from flask import render_template, request, redirect, url_for
from application import frontend
from application.forms import GenderForm
import requests, json


@frontend.route('/')
@frontend.route('/home', methods=['GET', 'POST'])
def home():
    form = GenderForm()
    if request.method == 'POST':
        payload = {"gender":"none"}
        gender = form.gender.data
        payload["gender"] = gender
        response = requests.post('http://127.0.0.1:5003/stats', params=payload).json()
        return render_template('character.html', title='Dwarven Character', form=form, data=response)
    if request.method == 'GET':
        return render_template('home.html', title='Dwarven Generator', form=form)