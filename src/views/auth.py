import functools
from os import error

from flask import (
    render_template,
    Blueprint,
    flash,
    g,
    redirect,
    request,
    session,
    url_for,
    jsonify)
 
from werkzeug.security import check_password_hash,generate_password_hash
from src.models.user import User
from src import db


auth = Blueprint('auth',__name__, url_prefix="/auth")

## register user
@auth.route("/register", methods= ["GET","POST"])
def register():

    if request.method == "POST":
        name = request.json['name']
        last_name = request.json["last_name"]
        email = request.json["email"]
        phone_number = request.json["phone_number"]
        password = request.json["password"]
        password_hash = generate_password_hash(password)

        user = User(name=name,
                    last_name=last_name,
                    email=email,
                    phone_number=phone_number,
                    password=password_hash)
        
        
        if not name:
            return jsonfy({"message":"name required"})
        elif not password:
            return jsonify({"message":"password required"})
        elif not email:
            return jsonify({"message":"email required"})
        
        unique_email = User.query.filter_by(email = email).first()
        if unique_email == None:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))
        else:
            jsonify({"message": "user already exist"})
        
        return jsonify({"message": "registered user"})


    

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
            return redirect(url_for('home.index'))
    
        flash(error)

        
    return render_template("auth/login.html")


@auth.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user= None
    else:
        g.user = User.query.get_or_404(user_id)

## cerrar session
@auth.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('index'))

#verificar si esta logeado
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))
        return view(**kwargs)
    return wrapped_view



