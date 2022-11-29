import random

from flask import (
    Blueprint,
    request,
    jsonify,
    url_for,
    redirect
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
            addres = request.json["addres"]


            driver_= Driver.query.all()
            list_driver_email=[]
            for element in driver_:
                driver_email = element.email
                list_driver_email.append(driver_email)
            if len(list_driver_email) != 0: 
                email_driver = random.choice(list_driver_email)

                order = Orders(
                            email=email,
                            title = title,
                            description = description,
                            addres = addres,
                            email_driver = email_driver)    
                
                user_email = User.query.filter_by(email = email).all()
                list_email = []
                for element in user_email:
                    _email = element.email
                    list_email.append(_email)

                if len(list_email) == 0:      
                    return jsonify({"mensaje":"the user is not registered, please register it"})
                else:
                    db.session.add(order)
                    db.session.commit()
                    return jsonify({"message": "created order"})
            else:
                return jsonify({"message": "driver is not exist in DB"})        
        else:           
            return jsonify({"format":{
                                    "email": "ejemplo@gmail.com",
                                    "title": "pizza",
                                    "description": "pizza peperoni",
                                    "addres" : "add"
                                    }})
    except Exception as ex:
        return jsonify({'mensaje':"table delivery does not exist in db yet"})           



@home.route("/orders/<string:email>")
def show_order_by_user(email):
    try:
        order_ = Orders.query.filter_by(email = email).all()
        db.session.commit()
        list_order = []
        for element in order_:
            orders = {'title':element.title,
                    'description':element.description,
                    "order_date" : element.created,
                    "address" : element.addres    
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
                    'title':element.title,
                    'description':element.description,
                    "order_date" : element.created,
                    "address" : element.addres    
                    }
            list_orders.append(orders)
     
        return jsonify({
            "oreds": list_orders
            })

    except Exception as ex:
        return jsonify({'mensaje':"method not allowed"})
      
   

        