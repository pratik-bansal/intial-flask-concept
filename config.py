import os



class Config(object):
    SECRET_KEY =  OS.environ.get('SECRET_KEY') or "secret_string"