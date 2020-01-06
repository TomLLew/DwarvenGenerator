from flask import render_template, request, redirect, url_for
from application import Main


@Main.route('/')
@Main.route('/home')
def home():
    return render_template('home.html', title='Dwarven Generator')