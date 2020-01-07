from flask import render_template, request, redirect, url_for
from application import backend

@backend.route('/')
def backend():
    return ("backend")