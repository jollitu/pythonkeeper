import re

from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from email_validator import validate_email


password_validation_pattern = "\S{8,}$"


# TODO align this to Lorelei
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=False, unique=True)
    password_hash = db.Column(db.String(255))

    # Print
    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.__validate_password(self, password)
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __validate_password(self, password):
        return re.Match(password_validation_pattern, password, flags=0)

    # TODO do these belong here? Hmmmmmm.
    def validate_email(self, email):
        return validate_email(self, email)

    # TODO, lol
    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))
