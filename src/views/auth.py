from http import HTTPStatus
from flask import (
    Blueprint,
    request,
    jsonify)
 
from werkzeug.security import generate_password_hash
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

            if email == "":
                return jsonify({"message": "Email cannot be empty "}),HTTPStatus.CONFLICT

            user = User(name=name,
                        last_name=last_name,
                        email=email,
                        phone_number=phone_number,
                        password=password_hash)

            
            unique_email = User.query.filter_by(email = email).first()
            if unique_email == None:
                db.session.add(user)
                db.session.commit()
                return jsonify({"message": "registered user"}), HTTPStatus.CREATED
            else:
                return jsonify({"message": "user already exist"}), HTTPStatus.CONFLICT
            
        return jsonify({"message": "registre un usuario" ,
                        "format" : {"name":"name",
                                    "last_name": "lastname",
                                    "email": "aaa@aaa.com",
                                    "phone_number": "3156324583",
                                    "password" : "pasword"
                                    }}),HTTPStatus.OK

    except Exception as ex:
        return jsonify({'mensaje':"format of the object or any of its keys or values are outside the allowed format"})   


    
@auth.route("/user", methods= ["GET"])
def show_all_users():
    
    user = User.query.all()
    db.session.commit()
    list_costumer = []
    for element in user:
        costumers = {
                'name':element.name,
                'last_name': element.last_name,
                'email':element.email,
                'phone_number':element.phone_number,  
                }
        list_costumer.append(costumers)
    
    return jsonify({
        "costumers": list_costumer
        })


      