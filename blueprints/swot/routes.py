from flask import Blueprint, render_template
from flask_login import login_required

swot_bp = Blueprint(
    "swot",
    __name__,
    url_prefix="/swot"
)


@swot_bp.route("/")
@login_required
def index():
    return render_template("swot/index.html")