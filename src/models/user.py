from src import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    phone_number = db.Column(db.String(10))
  
    def __init__(self,
                name,
                last_name,
                email,
                phone_number):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

    def __repr__(self) -> str:
        return f"User: {self.name}"