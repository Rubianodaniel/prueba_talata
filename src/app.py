from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy
from .config import configuration









# class Delivery(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50))
#     last_name = db.Column(db.String(50))
#     email = db.Column(db.String(50), unique=True)
#     phone_number = db.Column(db.String(10))
  
#     def __init__(self,
#                 name,
#                 last_name,
#                 email,
#                 phone_number):
#         self.name = name
#         self.last_name = last_name
#         self.email = email
#         self.phone_number = phone_number


# db.create_all()


# @app.route("/")
# def index():
#     return "hola"

# @app.route('/home',methods=['GET','POST'])
# def home():
#     try:
#         cursor = db.connection.cursor()
        
#         return "ok"
#     except:
#         return "error"

# @app.route('/not_found_404')
# def not_found_404():
#     return app.register_error_handler(404)

# if __name__ == '__main__':
#     app.config.from_object(configuration["development"])
    
#     app.run()