from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import configuration
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

def create_app(config = configuration['development']):
    app = Flask(__name__)

    ## cargar configuraciones
    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app,db)
    ## import vies bluprints
    from src.views.auth import auth
    app.register_blueprint(auth)
    # import index
    from src.views.orders import home
    app.register_blueprint(home)
    from src.views.conductores import conductor
    app.register_blueprint(conductor)
    
    @app.route('/')
    def index():
        return "<h1> PRUEBA TALATA </h1>"
    return app


