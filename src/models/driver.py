from src import db



class Driver(db.Model):
    email = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    phone_number = db.Column(db.String(10))
    password = db.Column(db.String(500))

    def __repr__(self) -> str:
        return f"User: {self.email}"


