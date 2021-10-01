from flask import render_template, flash, redirect
from flask_login import current_user

from app import app, db
from app.forms import LoginForm


# TODO return an object for the front end to consume
from app.models import User


@app.route("/login", methods=["POST"])
def login():
    if current_user.is_authenticated:
        return ""

    form = LoginForm()

    if form.validate_on_submit():
        return "{\"username\": " + current_user.__repr__ + "}"

    return "{}"


@app.route("/logout", methods=["POST"])
def logout(username):
    pass


@app.route("/register", methods=["POST"])
def register(username, password, email):
    user = User(username, password, email)
    db.session.add(user)
    db.session.commit()

    return "{}"