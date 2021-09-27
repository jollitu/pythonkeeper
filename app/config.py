import os

class Config(object):
    # TODO don't leave the "test" option in place, lol
    SECRET_KEY = os.environ.get('SECRET_KEY') or "test"