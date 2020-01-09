from flask import render_template, request, redirect, url_for
from application import frontend
from application.forms import GenderForm
import requests, json


@frontend.route('/')
@frontend.route('/home', methods=['GET', 'POST'])
def home():
    form = GenderForm()
    print(form.gender)
    if form.validate_on_submit():
        payload = request.form['gender']
        print(form.gender)
        stats = {}
        
        response = requests.post('http://127.0.0.1:5003/stats', params=payload).json()
        stats.update(response)
        return render_template('home.html', title='Dwarven Generator', form=form)
    return render_template('home.html', title='Dwarven Generator', form=form)