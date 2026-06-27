from datetime import datetime, timedelta

from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import login_required
from sqlalchemy import func

from models import db, DailySale


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

    selected_date = datetime.today().date()

    if request.method == "POST":

        date_string = request.form.get("sale_date")

        if not date_string:

            flash(
                "Please select a sales date.",
                "danger"
            )

            return redirect(
                url_for("daily_sales.index")
            )

        selected_date = datetime.strptime(
            date_string,
            "%Y-%m-%d"
        ).date()

        DailySale.query.filter_by(
            sale_date=selected_date
        ).delete()

        for category in SALES_CATEGORIES:

            value = request.form.get(
                category,
                "0"
            )

            try:

                amount = float(value or 0)

            except ValueError:

                amount = 0

            db.session.add(

                DailySale(
                    sale_date=selected_date,
                    product_name=category,
                    sales_value=amount
                )

            )

        db.session.commit()

        flash(
            "Daily sales saved successfully.",
            "success"
        )

        next_date = selected_date + timedelta(days=1)

        return redirect(

    url_for(
        "daily_sales.index",
        sale_date=next_date.strftime("%Y-%m-%d")
    )

)
    date_string = request.args.get("sale_date")

    if date_string:

        selected_date = datetime.strptime(
            date_string,
            "%Y-%m-%d"
        ).date()

    sales_data = {}

    rows = DailySale.query.filter_by(
        sale_date=selected_date
    ).all()

    for row in rows:

        sales_data[row.product_name] = row.sales_value

    cumulative_sales = {}

    for category in SALES_CATEGORIES:

        total = (
            db.session.query(
                func.coalesce(
                    func.sum(DailySale.sales_value),
                    0
                )
            )
            .filter(
                DailySale.product_name == category,
                DailySale.sale_date <= selected_date
            )
            .scalar()
        )

        cumulative_sales[category] = float(total)
        total_cumulative = sum(cumulative_sales.values())

    return render_template(
    "daily_sales/index.html",
    sales_categories=SALES_CATEGORIES,
    selected_date=selected_date,
    today_dict=sales_data,
cumulative_dict=cumulative_sales,
total_cumulative=total_cumulative,
)


    