from datetime import datetime
from src import db


class Delivery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    title = db.Column(db.String(50))
    description = db.Column(db.Text)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    addres = db.Column(db.String(50))
   
  
    def __init__(self,
                email,
                title,
                description,
                addres):
        self.email = email
        self.title = title
        self.description = description
        self.addres = addres

    def __repr__(self) -> str:
        return f"Delivery: {self.title}"


class AssignedOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    driver_id = db.Column(db.Integer)
    order_id = db.Column(db.Integer, db.ForeignKey("delivery.id"))
    delivery = db.relationship("Delivery", backref=db.backref("driver", lazy = True))
 
    
    def __init__(self,driver_id):
        self.conductor_id = driver_id
   
    def __repr__(self) -> str:
        return f"User: {self.driver_id}"