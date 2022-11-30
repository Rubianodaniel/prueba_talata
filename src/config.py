import os
from dotenv import dotenv_values, load_dotenv
from os.path import join, dirname

class Config:
       
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path=dotenv_path)
    SECRET_KEY = os.environ.get("SECRET_KEY")


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456789@localhost/api_prueba2"
    SQLALCHEMY_TRACK_MODIFICATION = False
    SQLALCHEMY_ECHO = True

class TestingConfig():
    
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456789@localhost/api_prueba"
    SQLALCHEMY_TRACK_MODIFICATION = False

   
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:123456789@localhost/api_prueba"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    

configuration = {
    'development' : DevConfig,
    'testing' : TestingConfig,
    'production' : ProdConfig
}
