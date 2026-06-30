from datetime import date, datetime

from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import current_user, login_required

from models import (
    db,
    Customer,
    Order,
    OrderItem,
    Product,
)


orders_bp = Blueprint(
    "orders",
    __name__,
    url_prefix="/orders",
)


def generate_order_number():

    today = date.today()

    prefix = f"RZ-{today.strftime('%Y%m%d')}"

    count = (
        Order.query.filter(
            Order.order_number.like(f"{prefix}%")
        ).count()
    )

    sequence = count + 1

    return f"{prefix}-{sequence:04d}"


@orders_bp.route("/", methods=["GET", "POST"])
@login_required
def index():

    if request.method == "POST":

        customer_id = request.form.get("customer_id")
        remarks = request.form.get("remarks", "").strip()

        product_ids = request.form.getlist("product_id[]")
        quantities = request.form.getlist("quantity[]")

        if not customer_id:

            flash(
                "Please select a customer.",
                "warning",
            )

            return redirect(url_for("orders.index"))

        try:

            order = Order(

                order_number=generate_order_number(),

                order_date=date.today(),

                customer_id=int(customer_id),

                sales_rep_id=current_user.id,

                remarks=remarks,

                status="Pending",

            )

            db.session.add(order)

            db.session.flush()

            for product_id, quantity in zip(product_ids, quantities):

                if not product_id:
                    continue

                qty = float(quantity or 0)

                if qty <= 0:
                    continue

                item = OrderItem(

                    order_id=order.id,

                    product_id=int(product_id),

                    quantity=qty,

                )

                db.session.add(item)

            db.session.commit()

            flash(
                f"Order {order.order_number} created successfully.",
                "success",
            )

            return redirect(
                url_for("orders.index")
            )

        except Exception as e:

            db.session.rollback()

            flash(
                f"Error saving order: {e}",
                "danger",
            )

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
@orders_bp.route("/pending")
@login_required
def pending_orders():

    orders = (
        Order.query
        .filter_by(status="Pending")
        .order_by(Order.order_date.desc(), Order.id.desc())
        .all()
    )

    return render_template(
        "orders/pending.html",
        orders=orders,
    )
@orders_bp.route("/<int:order_id>")
@login_required
def view_order(order_id):

    order = Order.query.get_or_404(order_id)

    return render_template(
        "orders/view.html",
        order=order,
    )  
@orders_bp.route("/<int:order_id>/invoice", methods=["POST"])
@login_required
def mark_invoiced(order_id):

    order = Order.query.get_or_404(order_id)

    if order.status == "Invoiced":

        flash(
            "Order has already been invoiced.",
            "warning",
        )

        return redirect(
            url_for(
                "orders.view_order",
                order_id=order.id,
            )
        )

    order.status = "Invoiced"

    order.invoiced_by_id = current_user.id

    order.invoiced_at = datetime.now()

    db.session.commit()

    flash(
        f"{order.order_number} marked as invoiced.",
        "success",
    )

    return redirect(
        url_for("orders.pending_orders")
    )      