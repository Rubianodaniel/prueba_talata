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
from src.models.delivery import Delivery, AssignedOrder
from src.models.driver import Driver
from src import db

home = Blueprint('home',__name__, url_prefix="/user")

def assigned():
    driver_ = Driver.query.all()
    list_driver = []
    for element in driver_:
        driver_id = element.id
        list_driver.append(driver_id)

    if list_driver  == None:
        return jsonify({"message": "we have not drivers"})
    else:

        select_driver = random.choice(list_driver)
        assigned_order = AssignedOrder(
                                    driver_id = select_driver,
                                    )
        db.session.add(assigned_order)
        db.session.commit()
        return jsonify({"message": "created order"})


@home.route("/delivery", methods=["GET", "POST"])
def create_order():
    # try:
        if request.method == "POST":
            email = request.json["email"]
            title = request.json["title"]
            description = request.json["description"]
            addres = request.json["addres"]

            order = Delivery(
                        email=email,
                        title = title,
                        description = description,
                        addres = addres)    
            
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
               
                return jsonify({"mensaje":"created order"})
        else:
            return jsonify({"format":{
                                    "email": "ejemplo@gmail.com",
                                    "title": "pizza",
                                    "description": "pizza peperoni",
                                    "addres" : "add"
                                    }})
    # except Exception as ex:
    #     return jsonify({'mensaje':"method no found"})           






@home.route("/orders/<int:id>")
def show_order_by_user(id):
    try:
        user_id= User.query.filter(User.id == id).first()
        delivery = Delivery.query.filter_by(email = user_id.email).all()
        delivery = list(reversed(delivery))
        db.session.commit()
        list_order = []
        for element in delivery:
            orders = {'title':element.title,
                    'description':element.description,
                    "order_date" : element.created,
                    "address" : element.addres    
            }
            list_order.append(orders)
     
        return jsonify({
            "oreds": list_order
        })
    except Exception as ex:
        return jsonify({'mensaje':"id does not exist"})
        

@home.route("/orders")
def show_all_oders():
    try:
        delivery = Delivery.query.all()
        delivery = list(reversed(delivery))
        db.session.commit()
        list_order = []
        for element in delivery:
            orders = {
                    'email': element.email,
                    'title':element.title,
                    'description':element.description,
                    "order_date" : element.created,
                    "address" : element.addres    
                    }
            list_order.append(orders)
     
        return jsonify({
            "oreds": list_order
            })

    except Exception as ex:
        return jsonify({'mensaje':"method not allowed"})
      
   

        