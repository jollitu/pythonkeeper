from app import routes, models
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Init Flask
app = Flask(__name__)
app.config.from_object(Config)

# Init SQLAlchemy
db = SQLAlchemy(app)

# Init Flask-Login
login = LoginManager(app)
