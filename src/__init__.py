from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy
from .config import configuration

app = Flask(__name__)

## cargar configuraciones
app.config.from_object(configuration["development"])
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()