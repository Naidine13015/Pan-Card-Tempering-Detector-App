import os
from os import environ # We are importing the environnement

# We've created a class name config in which we have sent people and testing as false and the base directly variable.
class Config(object):

    DEBUG = False
    Testing = False

    basedir = os.path.abspath(os.path.dirname(__file__))

    # Set a secret key
    SECRET_KEY = "naidine13015"

    UPLOADS = "app/app/static/uploads"

    SESSION_COOKIE_SECURE = True
    DEFAULT_THEME = None

class DevelopementConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False

class DebugConfig(Config):
    DEBUG = False