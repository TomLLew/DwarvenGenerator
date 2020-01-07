from flask import Flask
from flask_sqlalchemy import SQLAlchemy

backend = Flask(__name__)

from application import routes
