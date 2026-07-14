from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    abort,
    flash,
)

from flask_login import (
    login_required,
    current_user,
)

from models import db
from models import Outlet


outlets_bp = Blueprint(
    "outlets",
    __name__,
    url_prefix="/outlets",
)


@outlets_bp.route("/")
@login_required
def index():

    outlets = (
        Outlet.query
        .order_by(Outlet.outlet_name)
        .all()
    )

    return render_template(
        "outlets/index.html",
        outlets=outlets,
    )


@outlets_bp.route("/new", methods=["GET", "POST"])
@login_required
def new():

    if not current_user.is_admin:
        abort(403)

    if request.method == "POST":

        outlet_name = request.form["outlet_name"].strip()

        existing = Outlet.query.filter_by(
            outlet_name=outlet_name
        ).first()

        if existing:

            flash(
                "An outlet with that name already exists.",
                "warning",
            )

            return render_template(
                "outlets/form.html",
                outlet=request.form,
            )

        outlet = Outlet(
            outlet_name=outlet_name,
            is_active=request.form.get("is_active") == "1",
        )

        db.session.add(outlet)
        db.session.commit()

        flash(
            "Outlet created successfully.",
            "success",
        )

        return redirect(
            url_for("outlets.index")
        )

    return render_template(
        "outlets/form.html",
        outlet=None,
    )


@outlets_bp.route("/<int:id>/edit", methods=["GET", "POST"])
@login_required
def edit(id):

    if not current_user.is_admin:
        abort(403)

    outlet = Outlet.query.get_or_404(id)

    if request.method == "POST":

        outlet_name = request.form["outlet_name"].strip()

        existing = (
            Outlet.query
            .filter(
                Outlet.outlet_name == outlet_name,
                Outlet.id != outlet.id,
            )
            .first()
        )

        if existing:

            flash(
                "An outlet with that name already exists.",
                "warning",
            )

            return render_template(
                "outlets/form.html",
                outlet=outlet,
            )

        outlet.outlet_name = outlet_name

        outlet.is_active = (
            request.form.get("is_active") == "1"
        )

        db.session.commit()

        flash(
            "Outlet updated successfully.",
            "success",
        )

        return redirect(
            url_for("outlets.index")
        )

    return render_template(
        "outlets/form.html",
        outlet=outlet,
    )


@outlets_bp.route("/<int:id>/activate")
@login_required
def activate(id):

    if not current_user.is_admin:
        abort(403)

    outlet = Outlet.query.get_or_404(id)

    outlet.is_active = True

    db.session.commit()

    flash(
        "Outlet activated successfully.",
        "success",
    )

    return redirect(
        url_for("outlets.index")
    )


@outlets_bp.route("/<int:id>/deactivate")
@login_required
def deactivate(id):

    if not current_user.is_admin:
        abort(403)

    outlet = Outlet.query.get_or_404(id)

    outlet.is_active = False

    db.session.commit()

    flash(
        "Outlet deactivated successfully.",
        "success",
    )

    return redirect(
        url_for("outlets.index")
    )
