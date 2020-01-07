from flask import render_template, request, redirect, url_for
from application import service2

@service2.route('/', methods=['GET', 'POST'])
def random_name():
    return ("service 2")