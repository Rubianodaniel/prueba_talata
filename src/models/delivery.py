from datetime import datetime
from src import db


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), db.ForeignKey("user.email"))
    email_driver = db.Column(db.String(50),db.ForeignKey("driver.email"))
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(50))
    description = db.Column(db.Text)
    addres_order = db.Column(db.String(50))
    delivery_date = db.Column(db.Date,nullable=False)
    delivery_time_slot = db.Column(db.String(40))
    user = db.relationship("User", backref=db.backref("orders", lazy = True))
    driver = db.relationship("Driver", backref=db.backref("orders", lazy = True))
    

    def __repr__(self) -> str:
        return f"Delivery: {self.title}"

   
    def __repr__(self) -> str:
        return f"User: {self.title}"