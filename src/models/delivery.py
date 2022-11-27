from datetime import datetime
from src import db


class Delivery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    costumer = db.Column(db.Integer, db.ForeignKey("user.id"),nullable=False)
    title = db.Column(db.String(50))
    description = db.Column(db.Text)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
   
  
    def __init__(self,
                costumer,
                title,
                description,
                created):
        self.costumer = costumer
        self.title = title
        self.description = description
        self.created = created

    def __repr__(self) -> str:
        return f"Delivery: {self.title}"