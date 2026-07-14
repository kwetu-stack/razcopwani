from datetime import datetime, date

from flask import (
    Blueprint,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from flask_login import (
    current_user,
    login_required,
)

from sqlalchemy import cast, or_, String

from models import db
from models import Merchandiser
from models import Outlet
from models import OutletVisit


outlet_visits_bp = Blueprint(
    "outlet_visits",
    __name__,
    url_prefix="/outlet-visits",
)


STOCK_OPTIONS = [
    "High",
    "Moderate",
    "Low",
    "Stock Out",
]

FREEZER_OPTIONS = [
    "Good",
    "Needs Attention",
    "Not Working",
]


def active_merchandisers():
    return (
        Merchandiser.query
        .filter_by(is_active=True)
        .order_by(Merchandiser.name)
        .all()
    )


def active_outlets():
    return (
        Outlet.query
        .filter_by(is_active=True)
        .order_by(Outlet.outlet_name)
        .all()
    )


@outlet_visits_bp.route("/")
@login_required
def index():

    search = request.args.get("q", "").strip()

    query = (
        OutletVisit.query
        .join(Merchandiser)
        .join(Outlet)
    )

    if search:

        query = query.filter(
            or_(
                cast(OutletVisit.visit_date, String).ilike(f"%{search}%"),
                Merchandiser.name.ilike(f"%{search}%"),
                Outlet.outlet_name.ilike(f"%{search}%"),
            )
        )

    visits = (
        query
        .order_by(
            OutletVisit.visit_date.desc(),
            OutletVisit.id.desc(),
        )
        .all()
    )

    return render_template(
        "outlet_visits/index.html",
        visits=visits,
        search=search,
    )


@outlet_visits_bp.route("/new", methods=["GET", "POST"])
@login_required
def new():

    merchandisers = active_merchandisers()
    outlets = active_outlets()

    if request.method == "POST":

        form = request.form
        errors = []

        visit_date_value = form.get("visit_date", "").strip()
        merchandiser_id = form.get("merchandiser_id", "").strip()
        outlet_id = form.get("outlet_id", "").strip()
        icecream_stock = form.get("icecream_stock", "").strip()
        sauces_stock = form.get("sauces_stock", "").strip()
        bakery_stock = form.get("bakery_stock", "").strip()
        private_label_stock = form.get("private_label_stock", "").strip()
        freezer_condition = form.get("freezer_condition", "").strip()
        order_placed_value = form.get("order_placed")

        if not visit_date_value:
            errors.append("Visit Date is required.")

        if not merchandiser_id:
            errors.append("Merchandiser is required.")

        if not outlet_id:
            errors.append("Outlet is required.")

        stock_values = {
            "Ice Cream & Daily Indulgence": icecream_stock,
            "Sauces & Condiments": sauces_stock,
            "Bakery & Confectionery": bakery_stock,
            "Private Label": private_label_stock,
        }

        for label, value in stock_values.items():
            if value not in STOCK_OPTIONS:
                errors.append(f"{label} is required.")

        if freezer_condition not in FREEZER_OPTIONS:
            errors.append("Freezer Condition is required.")

        if order_placed_value not in {"1", "0"}:
            errors.append("Order Generated is required.")

        try:
            parsed_visit_date = datetime.strptime(
                visit_date_value,
                "%Y-%m-%d",
            ).date()
        except ValueError:
            parsed_visit_date = None
            errors.append("Visit Date must be a valid date.")

        merchandiser = None
        outlet = None

        if merchandiser_id:
            merchandiser = Merchandiser.query.filter_by(
                id=merchandiser_id,
                is_active=True,
            ).first()

            if not merchandiser:
                errors.append("Select an active merchandiser.")

        if outlet_id:
            outlet = Outlet.query.filter_by(
                id=outlet_id,
                is_active=True,
            ).first()

            if not outlet:
                errors.append("Select an active outlet.")

        if errors:

            for error in errors:
                flash(error, "warning")

            return render_template(
                "outlet_visits/form.html",
                visit=form,
                merchandisers=merchandisers,
                outlets=outlets,
                stock_options=STOCK_OPTIONS,
                freezer_options=FREEZER_OPTIONS,
                today=date.today(),
            )

        visit = OutletVisit(
            visit_date=parsed_visit_date,
            merchandiser_id=merchandiser.id,
            outlet_id=outlet.id,
            icecream_stock=icecream_stock,
            sauces_stock=sauces_stock,
            bakery_stock=bakery_stock,
            private_label_stock=private_label_stock,
            freezer_condition=freezer_condition,
            order_placed=order_placed_value == "1",
            notes=form.get("notes", "").strip() or None,
            created_by=current_user.id,
        )

        db.session.add(visit)
        db.session.commit()

        flash(
            "Outlet visit saved successfully.",
            "success",
        )

        return redirect(
            url_for("outlet_visits.index")
        )

    return render_template(
        "outlet_visits/form.html",
        visit=None,
        merchandisers=merchandisers,
        outlets=outlets,
        stock_options=STOCK_OPTIONS,
        freezer_options=FREEZER_OPTIONS,
        today=date.today(),
    )


@outlet_visits_bp.route("/view/<int:id>")
@login_required
def view(id):

    visit = OutletVisit.query.get_or_404(id)

    return render_template(
        "outlet_visits/view.html",
        visit=visit,
    )
