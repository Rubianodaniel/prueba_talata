import functools
from os import error

from flask import (
    render_template,
    Blueprint,
    flash,
    g,
    redirect,
    request,
    session,
    url_for,
    jsonify)
 
from werkzeug.security import check_password_hash,generate_password_hash
from src.models.user import User
from src import db


auth = Blueprint('auth',__name__, url_prefix="/auth")

## register user
@auth.route("/register", methods= ["GET","POST"])
def register():
    try:
        if request.method == "POST":
            name = request.json['name']
            last_name = request.json["last_name"]
            email = request.json["email"]
            phone_number = request.json["phone_number"]
            password = request.json["password"]
            password_hash = generate_password_hash(password)

            user = User(name=name,
                        last_name=last_name,
                        email=email,
                        phone_number=phone_number,
                        password=password_hash)

            
            unique_email = User.query.filter_by(email = email).first()
            if unique_email == None:
                db.session.add(user)
                db.session.commit()
                return jsonify({"message": "registered user"})
            else:
                return jsonify({"message": "user already exist"})
            
        return jsonify({"message": "registre un usuario" ,
                        "format" : {"name":"name",
                                    "last_name": "lastname",
                                    "email": "aaa@aaa.com",
                                    "phone_number": "3156324583",
                                    "password" : "pasword"
                                    }})
        
        else:
            return jsonify({"format":{
                                    "name":"name4",
                                    "last_name": "lastname2",
                                    "email": "ejemplo@gmail.com",
                                    "phone_number": "3156324583",
                                    "password" : "pasword"
                                    }})  
    except Exception as ex:
        return jsonify({'mensaje':"method no found"})       


    

