from flask import render_template, flash, redirect
from flask_login import current_user, login_user

from app import app, db
from app.forms import LoginForm
from app.models import User


# TODO return an object for the front end to consume
from app.models import User


@app.route("/login", methods=["POST"])
def login():
    if current_user.is_authenticated:
        return ""

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(user.password_hash):
            # TODO decide what's most convenient to pass to the front
            return ""
        login_user(user, remember=True)

        return "{\"username\": " + current_user.__repr__ + "}"

    return "{}"


@app.route("/logout", methods=["POST"])
def logout(username):
    pass


@app.route("/register", methods=["POST"])
def register(username, password, email):
    user = User(username, password, email)
    valid_email = user.validate_email(email)


    db.session.add(user)
    db.session.commit()

    return user.__repr__()