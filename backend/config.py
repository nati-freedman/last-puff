from os import environ, path

from dotenv import load_dotenv

# Application's main directory
basedir = path.abspath(path.dirname(__file__))
# Specificy a `.env` file containing key/value config values
load_dotenv(path.join(basedir, '.env'))

class Config:
    SECRET_KEY = environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL') or \
        'sqlite:///' + path.join(basedir, 'app.db')
    ENVIRONMENT = environ.get("ENVIRONMENT")
    FLASK_APP = environ.get("FLASK_APP")
    FLASK_DEBUG = environ.get("FLASK_DEBUG")