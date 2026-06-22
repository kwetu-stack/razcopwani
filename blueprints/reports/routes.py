from datetime import datetime

from flask import Blueprint, abort, render_template, request
from flask_login import current_user, login_required
from sqlalchemy import func

from blueprints.common import export_rows, module_config
from models import ActionPlan, CompetitorActivity, Customer, LostAccount, Opportunity, Visit, db


reports_bp = Blueprint("reports", __name__, url_prefix="/reports")


@reports_bp.route("/")
@login_required
def index():
    metrics = {
        "Customers": Customer.query.count(),
        "Visits": Visit.query.count(),
        "Coverage %": round((Visit.query.filter_by(visit_status="Completed").count() / max(Visit.query.count(), 1)) * 100),
        "Pipeline Value": db.session.query(func.coalesce(func.sum(Opportunity.estimated_value), 0)).scalar(),
        "Recovery Value": db.session.query(func.coalesce(func.sum(LostAccount.estimated_monthly_value), 0)).scalar(),
        "Critical Threats": CompetitorActivity.query.filter_by(impact_level="Critical").count(),
        "Overdue Actions": ActionPlan.query.filter_by(status="Overdue").count(),
    }
    categories = {
        "Executive Reports": ["Executive Summary", "Monthly Business Review", "Quarterly Review", "Territory Performance Review", "Growth Performance Review"],
        "Customer Reports": ["Customer Master List", "Active Customers", "Dormant Customers", "Lost Customers", "Customer Growth Report", "Customer Coverage Report"],
        "Product Reports": ["Product Master List", "Product Portfolio Report", "Product Category Report", "Growth Products Report", "Declining Products Report"],
        "Channel Reports": ["Channel Performance Report", "Channel Growth Report", "Channel SWOT Report", "Channel Opportunity Report"],
        "Route Reports": ["Route Master Report", "Route Coverage Report", "Weekly Route Report", "Monthly Route Performance Report"],
        "Visit Reports": ["Daily Visit Report", "Weekly Visit Report", "Monthly Visit Report", "Coverage Report", "Missed Visit Report", "Visit Productivity Report"],
        "SWOT Reports": ["SWOT Summary", "SWOT Opportunities Report", "SWOT Threat Report", "Territory SWOT Report", "Strategic Review Report"],
        "Opportunity Reports": ["Opportunity Pipeline Report", "Opportunity Forecast Report", "Won Opportunities Report", "Lost Opportunities Report", "Pipeline Aging Report"],
        "Competitor Reports": ["Competitor Activity Report", "Threat Analysis Report", "Territory Threat Report", "Market Intelligence Report"],
        "Lost Account Reports": ["Lost Accounts Report", "Recovery Pipeline Report", "Revenue Recovery Report", "Competitor Loss Report"],
        "Action Plan Reports": ["Open Actions Report", "Completed Actions Report", "Overdue Actions Report", "Execution Performance Report"],
    }
    return render_template("reports/reports.html", metrics=metrics, categories=categories, generated_at=datetime.now())


@reports_bp.route("/export/<module_key>/<export_format>")
@login_required
def export(module_key, export_format):
    if not current_user.is_admin:
        abort(403)
    configs = module_config()
    if module_key not in configs:
        abort(404)
    rows = configs[module_key]["model"].query.all()
    return export_rows(configs[module_key], rows, export_format)
