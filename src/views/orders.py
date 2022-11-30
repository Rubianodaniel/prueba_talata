import random
import datetime as dt
from datetime import datetime, timedelta

from flask import (
    Blueprint,
    request,
    jsonify,

)

## importar modelos y base de datos
from src.models.user import User
from src.models.delivery import Orders
from src.models.driver import Driver
from src import db

home = Blueprint('home',__name__, url_prefix="/user")

@home.route("/order", methods=["GET", "POST"])
def create_order():
    try:
        if request.method == "POST":
            email = request.json["email"]
            title = request.json["title"]
            description = request.json["description"]
            addres_order = request.json["addres_order"]
            delivery_date = request.json["delivery_date"]
            delivery_time_slot = request.json["delivery_time_slot"]
  
            try:
                ## comprobando que la franja horaria corresponda con minimo 1 hora hasta maximo 8 horas
                _init_time = dt.datetime.strptime(delivery_time_slot["init_time"], '%H:%M')
                _end_time = dt.datetime.strptime(delivery_time_slot["end_time"], '%H:%M')
                if _end_time > (_init_time + dt.timedelta(hours=8)):
                    return jsonify({"message": "maximum time slot is 8 more than the initial hour"}) 
                elif _end_time < (_init_time + dt.timedelta(hours=1)):  
                    return jsonify({"message": "minimun time slot is 1 more than the initial hour"})
                else:
                    delivery_time_slot = f'{delivery_time_slot["init_time"]} : {delivery_time_slot["end_time"]}' 
            except Exception as ex:
                return jsonify({'mensaje':"the time format does not match what the parameter is receiving"})  

        
            driver_= Driver.query.all()
            list_driver_email=[]
            for element in driver_:
                driver_email = element.email
                list_driver_email.append(driver_email)
            if len(list_driver_email) != 0: 
                email_driver = random.choice(list_driver_email)

                order = Orders(
                            email=email,
                            email_driver = email_driver,    
                            title = title,
                            description = description,
                            addres_order = addres_order,
                            delivery_date = delivery_date,
                            delivery_time_slot = delivery_time_slot
                            )
                
                user_email = User.query.filter_by(email = email).all()
                list_email = []
                for element in user_email:
                    _email = element.email
                    list_email.append(_email)

                if len(list_email) == 0:      
                    return jsonify({"mensaje":"the user is not yet registered, please register it"})
                else:
                    db.session.add(order)
                    db.session.commit()
                    return jsonify({"message": "created order"})
            else:
                return jsonify({"message": "no drivers registered in database"})        
        else:           
            return jsonify({"format":{
                                    "email": "ejemplo@gmail.com",
                                    "title": "pizza",
                                    "description": "pizza peperoni",
                                    "addres_order" : "add",
                                    "delivery_date": "2022-11-29",
                                    "delivery_time_slot" : {
                                                    "init_time":"8:00:",
                                                    "end_time" : "14:00"
                                                    }
                                    }})
    except Exception as ex:
        return jsonify({'mensaje':"table delivery does not exist in db yet"})           



@home.route("/orders/<string:email>")
def show_order_by_user(email):
    try:
        if email != "":
            order_ = Orders.query.filter_by(email = email).all()
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
            print(list_order)
            return jsonify({
                "oreds": list_order
            })
    except Exception as ex:
        return jsonify({'mensaje':"User not found"})


@home.route("/orders")
def show_all_oders():
    try:
        order_ = Orders.query.all()
        order_ = list(reversed(order_))
        db.session.commit()
        list_orders = []
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
            list_orders.append(orders)
     
        return jsonify({
            "oreds": list_orders
            })

    except Exception as ex:
        return jsonify({'mensaje':"method not allowed"})
      
   

        