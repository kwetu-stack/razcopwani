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
from models import Merchandiser


merchandisers_bp = Blueprint(
    "merchandisers",
    __name__,
    url_prefix="/merchandisers",
)


@merchandisers_bp.route("/")
@login_required
def index():

    merchandisers = (
        Merchandiser.query
        .order_by(Merchandiser.name)
        .all()
    )

    return render_template(
        "merchandisers/index.html",
        merchandisers=merchandisers,
    )


@merchandisers_bp.route("/new", methods=["GET", "POST"])
@login_required
def new():

    if not current_user.is_admin:
        abort(403)

    if request.method == "POST":

        name = request.form["name"].strip()

        existing = Merchandiser.query.filter_by(
            name=name
        ).first()

        if existing:

            flash(
                "A merchandiser with that name already exists.",
                "warning",
            )

            return render_template(
                "merchandisers/form.html",
                merchandiser=request.form,
            )

        merchandiser = Merchandiser(
            name=name,
            is_active=request.form.get("is_active") == "1",
        )

        db.session.add(merchandiser)
        db.session.commit()

        flash(
            "Merchandiser created successfully.",
            "success",
        )

        return redirect(
            url_for("merchandisers.index")
        )

    return render_template(
    "merchandisers/form.html",
    merchandiser=None,
)
@merchandisers_bp.route("/<int:id>/edit", methods=["GET", "POST"])
@login_required
def edit(id):

    if not current_user.is_admin:
        abort(403)

    merchandiser = Merchandiser.query.get_or_404(id)

    if request.method == "POST":

        name = request.form["name"].strip()

        existing = (
            Merchandiser.query
            .filter(
                Merchandiser.name == name,
                Merchandiser.id != merchandiser.id,
            )
            .first()
        )

        if existing:

            flash(
                "A merchandiser with that name already exists.",
                "warning",
            )

            return render_template(
                "merchandisers/form.html",
                merchandiser=merchandiser,
            )

        merchandiser.name = name

        merchandiser.is_active = (
            request.form.get("is_active") == "1"
        )

        db.session.commit()

        flash(
            "Merchandiser updated successfully.",
            "success",
        )

        return redirect(
            url_for("merchandisers.index")
        )

    return render_template(
        "merchandisers/form.html",
        merchandiser=merchandiser,
    )
@merchandisers_bp.route("/<int:id>/toggle")
@login_required
def toggle(id):

    if not current_user.is_admin:
        abort(403)

    merchandiser = Merchandiser.query.get_or_404(id)

    merchandiser.is_active = not merchandiser.is_active

    db.session.commit()

    if merchandiser.is_active:
        flash(
            "Merchandiser activated successfully.",
            "success",
        )
    else:
        flash(
            "Merchandiser deactivated successfully.",
            "success",
        )

    return redirect(
        url_for("merchandisers.index")
    )      
