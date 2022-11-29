from datetime import datetime
from src import db


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), db.ForeignKey("user.email"))
    email_driver = db.Column(db.String(50),db.ForeignKey("driver.email"))
    title = db.Column(db.String(50))
    description = db.Column(db.Text)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    addres = db.Column(db.String(50))
    user = db.relationship("User", backref=db.backref("orders", lazy = True))
    driver = db.relationship("Driver", backref=db.backref("orders", lazy = True))
    

    def __repr__(self) -> str:
        return f"Delivery: {self.title}"

   
    def __repr__(self) -> str:
        return f"User: {self.title}"