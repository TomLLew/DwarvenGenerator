from flask import Flask
from flask_sqlalchemy import SQLAlchemy

service1 = Flask(__name__)

from application import routes