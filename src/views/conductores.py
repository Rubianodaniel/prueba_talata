import random
from flask import (
    Blueprint,
    request,
    jsonify)
 
from werkzeug.security import generate_password_hash
from src.models.driver import Driver
from src import db


conductor = Blueprint('driver',__name__, url_prefix="/driver")

## register user
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




        
















# @conductor.route("/orders/<int:id>")
# def show_order_by_driver(id):
#     try:
#         driver_id = AssignedOrder.query.filter(AssignedOrder.conductor_id == id).first()
#         db.session.commit()

#         if driver_id != None:
#             order = AssignedOrder.query.filter_by(conductor_id = driver_id).all()
#             db.session.commit()
#             list_order=[]
#             for element in order:
#                 orders = {'title':element.title,
#                         'description':element.description,
#                         "order_date" : element.created,
#                         "address" : element.addres    
#                 }
#                 list_order.append(orders)
#             return jsonify({
#                             "orders": "list_order"
#                             })      
#     except Exception as ex:
#         return jsonify({'mensaje':"id does not exist"})




    