from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy
from .config import configuration
from flask_migrate import Migrate

app = Flask(__name__)

## cargar configuraciones
app.config.from_object(configuration["development"])
db = SQLAlchemy(app)
migrate = Migrate(app,db)


## import vies bluprints
from src.views.auth import auth
app.register_blueprint(auth)

# import index
from src.views.orders import home
app.register_blueprint(home)

from src.views.conductores import conductor
app.register_blueprint(conductor)

with app.app_context():
    db.create_all()

@app.route("/")
def redirect_login():
    return redirect(url_for("auth.register"))