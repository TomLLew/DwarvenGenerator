from flask import Flask
from flask_sqlalchemy import SQLAlchemy

service2 = Flask(__name__)

from application import routes