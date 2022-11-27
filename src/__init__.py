from flask import Flask,redirect,url_for,render_template,request
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
from src.views.index import home
app.register_blueprint(home)

with app.app_context():
    db.create_all()

@app.route("/")
def redirect_login():
    return redirect(url_for("auth.login"))