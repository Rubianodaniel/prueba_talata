from http import HTTPStatus
import datetime as dt
from datetime import datetime
from flask import (
    Blueprint,
    request,
    jsonify)
 
from werkzeug.security import generate_password_hash
from src.models.driver import Driver
from src.models.delivery import Orders
from src import db


conductor = Blueprint('driver',__name__, url_prefix="/driver")

## register driver
@conductor.route("/register", methods= ["GET","POST"])
def register_driver():
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

            driveres = Driver(name=name,
                        last_name=last_name,
                        email=email,
                        phone_number=phone_number,
                        password=password_hash)

            
            unique_email = Driver.query.filter_by(email = email).first()
            if unique_email == None:
                db.session.add(driveres)
                db.session.commit()
                return jsonify({"message": "registered Driver"}),HTTPStatus.CREATED
            else:
                return jsonify({"message": "Driver already exist"}),HTTPStatus.CONFLICT
            
        return jsonify({"message": "drivers register" ,
                        "format" : {"name":"name",
                                    "last_name": "lastname",
                                    "email": "aaa@aaa.com",
                                    "phone_number": "3156324583",
                                    "password" : "pasword"
                                    }}),HTTPStatus.OK

    except Exception as ex:
        return jsonify({'mensaje':"format of the object or any of its keys or values are outside the allowed format"},HTTPStatus.CONFLICT)   


    
@conductor.route("/", methods= ["GET"])
def show_all_drivers():
   
    driver = Driver.query.all()
    db.session.commit()
    list_costumer = []
    for element in driver:
        costumers = {
                'name':element.name,
                'last_name': element.last_name,
                'email':element.email,
                'phone_number':element.phone_number,  
                }
        list_costumer.append(costumers)
    
    return jsonify({
        "driver": list_costumer
        }), HTTPStatus.OK

 


@conductor.route("/orders/<string:email>")
def show_order_by_driver(email):
    try:
        if email != "":
            driver_ = Driver.query.filter(Driver.email == email).first()
            if driver_ == None:
                return jsonify({'mensaje':"User not found"}), HTTPStatus.NOT_FOUND
            else:
                order_ = driver_.orders
            
            db.session.commit()
            list_order = []
            for element in order_:
                orders = {
                        'email': element.email,
                        'email_driver':element.email_driver,
                        'title':element.title,
                        'description':element.description,
                        "created" : element.created,
                        "address_order" : element.addres_order,
                        "delivery_date" : element.delivery_date,
                        "delivery_time_slot" : element.delivery_time_slot  
                        }
                list_order.append(orders)
            return jsonify({
                "oreds": list_order
            }),HTTPStatus.OK
    except Exception as ex:
        return jsonify({'mensaje':"Data entered does not correspond to the data type or format allowed"}),HTTPStatus.CONFLICT


@conductor.route("/orders/<string:email>/<string:date>")
def show_order_driver_date(email, date):
    try:
        if email != "" and date != "":
            driver_ = Driver.query.filter(Driver.email == email).first()
            if driver_ == None:
                return jsonify({'mensaje':"User not found"}),HTTPStatus.NOT_FOUND
            else:
                order_= driver_.orders
            
            try:
                date_ = dt.datetime.strptime(date, "%Y-%m-%d").date()
            except Exception as ex:
                return jsonify({'mensaje':"the date format does not match what the parameter is receiving"}),HTTPStatus.CONFLICT 
                 
            db.session.commit()
            list_order = []
            for element in order_:
                if date_ == element.delivery_date:
                    orders = {
                            'email': element.email,
                            'email_driver':element.email_driver,
                            'title':element.title,
                            'description':element.description,
                            "created" : element.created,
                            "address_order" : element.addres_order,
                            "delivery_date" : element.delivery_date,
                            "delivery_time_slot" : element.delivery_time_slot  
                            }
                    list_order.append(orders)
            if len(list_order) != 0:
                return jsonify({
                    "oreds": list_order
                }),HTTPStatus.OK
            else:
                return jsonify({
                    "message": "Driver not found or Date not found"
                }), HTTPStatus.NOT_FOUND
    except Exception as ex:
        return jsonify({'mensaje':"The entered parameters do not exist or do not correspond to the format."}),HTTPStatus.NOT_FOUND
      




        




















    