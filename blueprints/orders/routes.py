from flask import Blueprint, render_template
from flask_login import current_user, login_required

from models import Customer, Product


orders_bp = Blueprint(
    "orders",
    __name__,
    url_prefix="/orders",
)


@orders_bp.route("/")
@login_required
def index():

    customers = (
        Customer.query
        .order_by(Customer.customer_name)
        .all()
    )

    products = (
        Product.query
        .order_by(Product.product_name)
        .all()
    )

    return render_template(
        "orders/index.html",
        customers=customers,
        products=products,
    )