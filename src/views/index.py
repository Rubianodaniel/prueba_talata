from flask import (
    render_template,
    Blueprint,
    flash,
    g,
    redirect,
    request,
    session,
    url_for,
    jsonify
)

from werkzeug.exceptions import abort

## importar modelos y base de datos
from src.models.user import User
from src.models.delivery import Delivery
from src import db

from src.views.auth import login_required


home = Blueprint('home',__name__, url_prefix="/user")

## register user

def get_user():
    user = User.query.get_or_404(id)
    print(user)
    return user


@home.route("/home")
@login_required
def index():
    user_id = g.user.id
    delivery = Delivery.query.filter_by(costumer=user_id).all()
    db.session.commit()
    list_order = []
    for element in delivery:
        orders = {'title':element.title,
                'description':element.description,
                "order_date" : element.created    
        }
        list_order.append(orders)


    return jsonify({
        "oreds": list_order
    })


@home.route("/delivery", methods=["GET", "POST"])
@login_required
def create_delivery():
    return jsonify({"mensaje":"daniel"})

        