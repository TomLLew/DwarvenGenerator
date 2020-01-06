from flask import Flask
from flask_sqlalchemy import SQLAlchemy

Main = Flask(__name__)

from application import routes