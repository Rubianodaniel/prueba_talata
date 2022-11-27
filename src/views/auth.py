from flask import (
    render_template,
    Blueprint,
    flash,
    g,
    redirect,
    request,
    session,
    url_for
)
from werkzeug.security import check_password_hash,generate_password_hash
from src.models.user import User
from src import db


auth = Blueprint('auth',__name__, url_prefix="/auth")

## register user
@auth.route("/register", methods= ["GET","POST"])
def register():
    if request.method == "POST":
        name = request.form.get('name')
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        phone_number = request.form.get("phone_number")
        password = request.form.get("password")
        password_hash = generate_password_hash(password)

        user = User(name=name,
                    last_name=last_name,
                    email=email,
                    phone_number=phone_number,
                    password=password_hash)
        
        error = None
        if not name:
            error = "name required"
        elif not password:
            error = "password required"
        elif not email:
            error = "email required"
        
        unique_email = User.query.filter_by(email = email).first()
        if unique_email == None:
            db.session.add(user)
            db.session.commit()
        else:
            error = f'email {email} already exist'
        
        flash(error)


    return render_template("auth/register.html")

## iniciar session
@auth.route("/login", methods= ["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        costumer = User.query.filter_by(email = email).first()
        
        error = None
        if (costumer == None):
            error = "incorrect email"
        elif not check_password_hash(costumer.password, password):
            error = "incorrect password"

        if error is None:
            session.clear()
            session['user_id']= costumer.id
            #return redirect(url_for('index'))
    
        flash(error)
    return render_template("auth/login.html")