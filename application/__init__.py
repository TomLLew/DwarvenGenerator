from flask import Flask
from flask_sqlalchemy import SQLAlchemy

frontend = Flask(__name__)

frontend.config['SECRET_KEY'] = 'test'

from application import routes