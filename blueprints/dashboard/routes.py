from datetime import date, timedelta

from flask import Blueprint, render_template
from flask_login import login_required
from sqlalchemy import func

from models import ActionPlan, CompetitorActivity, Customer, LostAccount, Opportunity, Visit, db


dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/")
@login_required
def index():
    planned = Visit.query.filter(Visit.visit_status.in_(["Planned", "Completed", "Missed"])).count()
    completed = Visit.query.filter_by(visit_status="Completed").count()
    total_actions = ActionPlan.query.count()
    completed_actions = ActionPlan.query.filter_by(status="Completed").count()
    pipeline = db.session.query(func.coalesce(func.sum(Opportunity.estimated_value), 0)).filter(
        Opportunity.status.notin_(["Won", "Lost"])
    ).scalar()
    kpis = [
        ("Sales Growth %", "18%", "Target 25%"),
        ("Coverage %", f"{round((completed / planned) * 100) if planned else 0}%", "Completed vs planned visits"),
        ("Open Opportunities", Opportunity.query.filter(Opportunity.status.notin_(["Won", "Lost"])).count(), "Pipeline records"),
        ("Pipeline Value", f"KES {pipeline:,.0f}", "Open estimated value"),
        ("Lost Accounts", LostAccount.query.count(), "Recovery focus"),
        ("Action Completion %", f"{round((completed_actions / total_actions) * 100) if total_actions else 0}%", "Execution rate"),
    ]
    opportunity_stage = db.session.query(Opportunity.status, func.count(Opportunity.id)).group_by(Opportunity.status).all()
    channel_rows = (
        db.session.query(Customer.territory, func.count(Customer.id))
        .group_by(Customer.territory)
        .order_by(func.count(Customer.id).desc())
        .limit(8)
        .all()
    )
    visit_status = db.session.query(Visit.visit_status, func.count(Visit.id)).group_by(Visit.visit_status).all()
    recent = {
        "visits": Visit.query.order_by(Visit.created_at.desc()).limit(5).all(),
        "opportunities": Opportunity.query.order_by(Opportunity.created_at.desc()).limit(5).all(),
        "competitors": CompetitorActivity.query.order_by(CompetitorActivity.created_at.desc()).limit(5).all(),
        "actions": ActionPlan.query.order_by(ActionPlan.created_at.desc()).limit(5).all(),
    }
    alerts = {
        "overdue": ActionPlan.query.filter_by(status="Overdue").limit(5).all(),
        "missed": Visit.query.filter_by(visit_status="Missed").limit(5).all(),
        "aging": Opportunity.query.filter(Opportunity.created_at <= date.today() - timedelta(days=60)).limit(5).all(),
        "recoveries": LostAccount.query.filter(LostAccount.recovery_probability.in_(["High", "Very High"])).limit(5).all(),
    }
    insights = [
        ("Fastest Growing Channel", "HORECA +31%"),
        ("Highest Opportunity Territory", Opportunity.query.with_entities(Opportunity.territory).first()[0] if Opportunity.query.first() else "Nyali"),
        ("Most Active Competitor", CompetitorActivity.query.with_entities(CompetitorActivity.competitor_name).first()[0] if CompetitorActivity.query.first() else "Brookside"),
        ("Largest Lost Account", LostAccount.query.order_by(LostAccount.estimated_monthly_value.desc()).first().customer.customer_name if LostAccount.query.first() else "Whitesands Hotel"),
    ]
    return render_template(
        "dashboard/dashboard.html",
        kpis=kpis,
        opportunity_stage={"labels": [r[0] for r in opportunity_stage], "values": [r[1] for r in opportunity_stage]},
        territory_customers={"labels": [r[0] for r in channel_rows], "values": [r[1] for r in channel_rows]},
        visit_status={"labels": [r[0] for r in visit_status], "values": [r[1] for r in visit_status]},
        recent=recent,
        alerts=alerts,
        insights=insights,
    )
