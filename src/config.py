import os
from dotenv import dotenv_values, load_dotenv
from os.path import join, dirname




class DevConfig():
    
    
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path=dotenv_path)
    
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456789@localhost/api_prueba"
    SQLALCHEMY_TRACK_MODIFICATION = False
    SECRET_KEY = os.environ.get("SECRET_KEY")
    # MYSQL_HOST = env["MYSQL_HOST"]
    # MYSQL_USER = env["MYSQL_USER"]
    # MYSQL_PASSWORD = env["MYSQL_PASSWORD"]
    # MYSQL_DB = env["MYSQL_DB"]
    

   

configuration = {
    'development' : DevConfig
}

if __name__=='__main__':
    configuration['development']