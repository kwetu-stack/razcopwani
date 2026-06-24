from flask import Blueprint, render_template
from flask_login import login_required

daily_sales_bp = Blueprint(
    "daily_sales",
    __name__,
    url_prefix="/daily-sales"
)

@daily_sales_bp.route("/")
@login_required
def index():
    return render_template("daily_sales/index.html")