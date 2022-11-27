from dotenv import dotenv_values



class DevConfig():

    env = {**dotenv_values(".env")}
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456789@localhost/api_prueba"
    SQLALCHEMY_TRACK_MODIFICATION = False
    # MYSQL_HOST = env["MYSQL_HOST"]
    # MYSQL_USER = env["MYSQL_USER"]
    # MYSQL_PASSWORD = env["MYSQL_PASSWORD"]
    # MYSQL_DB = env["MYSQL_DB"]
  

    

configuration = {
    'development' : DevConfig
}

