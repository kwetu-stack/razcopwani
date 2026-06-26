from datetime import datetime
from sqlalchemy import func

from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import login_required

from models import DailySale, db

daily_sales_bp = Blueprint(
    "daily_sales",
    __name__,
    url_prefix="/daily-sales"
)

SALES_CATEGORIES = [
    "Lyons Ice Cream",
    "Pops Vendors",
    "Lyons Boxes",
    "OOH Ice Cream",
    "Compound",
    "Fusion",
    "OOH Lala",
    "Groceries",
    "Cones",
    "Cheese",
    "Frozen Groceries",
    "Galitos Sauces",
    "Presto",
    "Sprinkles",
    "Soft Mix",
]


@daily_sales_bp.route("/", methods=["GET", "POST"])
@login_required
def index():

    if request.method == "POST":

        sale_date_str = request.form.get("sale_date")

        if not sale_date_str:
            flash("Please select a sales date.", "danger")
            return redirect(url_for("daily_sales.index"))

        sale_date = datetime.strptime(
            sale_date_str,
            "%Y-%m-%d"
        ).date()

        DailySale.query.filter_by(
            sale_date=sale_date
        ).delete()

        for category in SALES_CATEGORIES:

            value = request.form.get(category, "0")

            try:
                sales_value = float(value or 0)
            except ValueError:
                sales_value = 0

            db.session.add(
                DailySale(
                    sale_date=sale_date,
                    product_name=category,
                    sales_value=sales_value
                )
            )

        db.session.commit()

        flash(
            "Daily sales saved successfully.",
            "success"
        )

        return redirect(
            url_for("daily_sales.index")
        )

        # Default to today's date
    selected_date = datetime.today().date()

    # If a date is supplied in the URL, use it
    date_str = request.args.get("sale_date")
    if date_str:
        try:
            selected_date = datetime.strptime(
                date_str,
                "%Y-%m-%d"
            ).date()
        except ValueError:
            pass

    # Load saved sales for the selected date
    today_sales = DailySale.query.filter_by(
        sale_date=selected_date
    ).all()

    today_dict = {
        sale.product_name: sale.sales_value
        for sale in today_sales
    }

    # Calculate cumulative sales for each category
    cumulative_sales = (
        db.session.query(
            DailySale.product_name,
            func.sum(DailySale.sales_value)
        )
        .group_by(DailySale.product_name)
        .all()
    )

    cumulative_dict = {
        product: total or 0
        for product, total in cumulative_sales
    }

    return render_template(
        "daily_sales/index.html",
        sales_categories=SALES_CATEGORIES,
        selected_date=selected_date,
        today_dict=today_dict,
        cumulative_dict=cumulative_dict,
    )
    