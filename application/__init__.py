from flask import Flask
from flask_sqlalchemy import SQLAlchemy

frontend = Flask(__name__)

from application import routes