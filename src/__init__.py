from flask import Flask,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from .config import configuration


app = Flask(__name__)

## cargar configuraciones
app.config.from_object(configuration["development"])
db = SQLAlchemy(app)



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