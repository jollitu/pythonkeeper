import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # TODO don't leave the "test" option in place, lol
    SECRET_KEY = os.environ.get('SECRET_KEY') or "test"

    # TODO
    DB_URI = os.environ.get("DB_URL") or \
        'sqlite:///' + os.path.join(basedir, "app.db")

    # TODO this will probably be enabled later on
    TRACK_MODS = False