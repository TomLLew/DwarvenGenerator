from flask import render_template, request, redirect, url_for
from application import service1

@service1.route('/', methods=['GET', 'POST'])
def random_job():
    return ("servie 1")