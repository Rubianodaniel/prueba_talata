import random
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

            driveres = Driver(name=name,
                        last_name=last_name,
                        email=email,
                        phone_number=phone_number,
                        password=password_hash)

            
            unique_email = Driver.query.filter_by(email = email).first()
            if unique_email == None:
                db.session.add(driveres)
                db.session.commit()
                return jsonify({"message": "registered Driver"})
            else:
                return jsonify({"message": "Driver already exist"})
            
        return jsonify({"message": "drivers register" ,
                        "format" : {"name":"name",
                                    "last_name": "lastname",
                                    "email": "aaa@aaa.com",
                                    "phone_number": "3156324583",
                                    "password" : "pasword"
                                    }})

    except Exception as ex:
        return jsonify({'mensaje':"method no allowed"})   


    
@conductor.route("/", methods= ["GET"])
def show_all_drivers():
    try:
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
            })

    except Exception as ex:
        return jsonify({'mensaje':"method not allowed"})


@conductor.route("/orders/<string:email>")
def show_order_by_driver(email):
    try:
        if email != "":
            driver_ = Driver.query.filter(Driver.email == email).first()
            order_= driver_.orders
            
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
            print(driver_.orders)
            return jsonify({
                "oreds": list_order
            })
    except Exception as ex:
        return jsonify({'mensaje':"User not found"})


@conductor.route("/orders/<string:email>/<string:date>")
def show_order_driver_date(email, date):
    # try:
        if email != "" and date != "":
            driver_ = Driver.query.filter(Driver.email == email).first()
            order_= driver_.orders
            
            try:
                date_ = dt.datetime.strptime(date, "%Y-%m-%d").date()
            except Exception as ex:
                return jsonify({'mensaje':"the date format does not match what the parameter is receiving"}) 
                 
            db.session.commit()
            list_order = []
            for element in order_:
                print(element.delivery_date, date_)
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
                })
            else:
                return jsonify({
                    "message": "Driver not found or Date not found"
                })
    # except Exception as ex:
    #     return jsonify({'mensaje':"User not found"})
      




        




















    