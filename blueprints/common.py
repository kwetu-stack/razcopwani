from datetime import date, datetime, time
from io import BytesIO, StringIO

import pandas as pd
from flask import (
    Blueprint,
    Response,
    abort,
    flash,
    redirect,
    render_template,
    request,
    send_file,
    url_for,
)
from flask_login import current_user, login_required
from sqlalchemy import String, cast, func, or_

from data.product_catalog import PRODUCT_CATEGORIES
from models import (
    ActionPlan,
    Channel,
    CompetitorActivity,
    Customer,
    LostAccount,
    Opportunity,
    Product,
    Route,
    Swot,
    Visit,
    db,
)


TERRITORIES = [
    "Nyali",
    "Bamburi",
    "Mtwapa",
    "Kilifi",
    "Malindi",
    "Diani",
    "Ukunda",
    "Likoni",
    "Changamwe",
    "Mariakani",
    "Voi",
    "Taveta",
    "Lamu",
]


def admin_required():
    if not current_user.is_authenticated or not current_user.is_admin:
        abort(403)


def parse_value(value, column):
    if value in (None, ""):
        return None
    python_type = column.type.python_type
    if python_type is date:
        return datetime.strptime(value, "%Y-%m-%d").date()
    if python_type is time:
        return datetime.strptime(value, "%H:%M").time()
    if python_type is datetime:
        return datetime.strptime(value, "%Y-%m-%d").date()
    if python_type is int:
        return int(value)
    if python_type is float:
        return float(value)
    return value.strip() if isinstance(value, str) else value


def serialize_value(value):
    if isinstance(value, (date, datetime)):
        return value.strftime("%Y-%m-%d")
    if value is None:
        return ""
    return value


def choices_from_model(model, value_field, label_field):
    return [
        (str(getattr(row, value_field)), getattr(row, label_field))
        for row in model.query.order_by(getattr(model, label_field)).all()
    ]


def filter_options(config):
    options = {}
    for field, source in config.get("filter_choices", {}).items():
        if source == "distinct":
            column = getattr(config["model"], field)
            rows = db.session.query(column).filter(column.isnot(None)).distinct().order_by(column).all()
            options[field] = [row[0] for row in rows if row[0]]
        else:
            options[field] = source
    return options


def module_config():
    return {
        "swot": {
            "title": "SWOT",
            "endpoint": "swot",
            "model": Swot,
            "url": "/swot",
            "search": ["title", "description", "territory", "channel", "owner"],
            "filters": ["category", "territory", "channel", "priority", "status", "owner"],
            "table": ["category", "title", "territory", "channel", "priority", "status", "owner"],
            "fields": [
                ("category", "select", ["Strength", "Weakness", "Opportunity", "Threat"], True),
                ("title", "text", None, True),
                ("description", "textarea", None, False),
                ("territory", "select", TERRITORIES, False),
                ("channel", "select", ["General Trade", "Modern Trade", "HORECA", "Institutions", "Distributors"], False),
                ("priority", "select", ["Critical", "High", "Medium", "Low"], True),
                ("status", "select", ["Open", "Monitoring", "Action Taken", "Closed"], True),
                ("owner", "text", None, False),
            ],
            "kpis": [("Total SWOT", "count"), ("Open", ("status", "Open")), ("Critical", ("priority", "Critical")), ("Threats", ("category", "Threat"))],
            "chart_field": "category",
            "special": "matrix",
        },
        "customers": {
            "title": "Customers",
            "endpoint": "customers",
            "model": Customer,
            "url": "/customers",
            "search": ["customer_name", "customer_code", "phone", "contact_person"],
            "filters": ["territory", "channel_id", "customer_status"],
            "table": ["customer_code", "customer_name", "contact_person", "territory", "channel_id", "customer_status", "credit_limit"],
            "fields": [
                ("customer_code", "text", None, True),
                ("customer_name", "text", None, True),
                ("contact_person", "text", None, False),
                ("phone", "text", None, False),
                ("email", "email", None, False),
                ("physical_address", "text", None, False),
                ("territory", "select", TERRITORIES, True),
                ("channel_id", "fk_channel", None, True),
                ("customer_status", "select", ["Active", "Inactive", "Dormant", "Lost", "Prospect"], True),
                ("credit_limit", "number", None, False),
                ("notes", "textarea", None, False),
            ],
            "kpis": [("Total Customers", "count"), ("Active", ("customer_status", "Active")), ("Dormant", ("customer_status", "Dormant")), ("Lost", ("customer_status", "Lost"))],
            "chart_field": "customer_status",
            "detail": True,
        },
        "products": {
            "title": "Products",
            "endpoint": "products",
            "model": Product,
            "url": "/products",
            "search": ["product_name", "product_code", "category", "brand"],
            "filters": ["category", "brand", "status"],
            "filter_choices": {
                "category": PRODUCT_CATEGORIES,
                "brand": "distinct",
                "status": ["Active", "Inactive", "Discontinued", "Development"],
            },
            "table": ["product_code", "product_name", "category", "brand", "unit_size", "selling_price", "status"],
            "fields": [
                ("product_code", "text", None, True),
                ("product_name", "text", None, True),
                ("category", "select", PRODUCT_CATEGORIES, True),
                ("brand", "text", None, False),
                ("unit_size", "text", None, False),
                ("selling_price", "number", None, False),
                ("status", "select", ["Active", "Inactive", "Discontinued", "Development"], True),
                ("notes", "textarea", None, False),
            ],
            "kpis": [("Total Products", "count"), ("Active", ("status", "Active")), ("Discontinued", ("status", "Discontinued")), ("Development", ("status", "Development"))],
            "chart_field": "category",
            "detail": True,
        },
        "channels": {
            "title": "Channels",
            "endpoint": "channels",
            "model": Channel,
            "url": "/channels",
            "search": ["channel_name", "manager", "description"],
            "filters": ["status"],
            "table": ["channel_name", "growth_target", "manager", "status", "notes"],
            "fields": [
                ("channel_name", "text", None, True),
                ("description", "textarea", None, False),
                ("growth_target", "number", None, False),
                ("manager", "text", None, False),
                ("status", "select", ["Active", "Inactive", "Development", "Closed"], True),
                ("notes", "textarea", None, False),
            ],
            "kpis": [("Total Channels", "count"), ("Active", ("status", "Active")), ("Development", ("status", "Development")), ("Closed", ("status", "Closed"))],
            "chart_field": "status",
            "detail": True,
        },
        "routes": {
            "title": "Routes",
            "endpoint": "routes",
            "model": Route,
            "url": "/routes",
            "search": ["route_name", "route_code", "territory", "assigned_person"],
            "filters": ["territory", "county", "channel_id", "status", "route_day", "assigned_person"],
            "table": ["route_code", "route_name", "territory", "county", "route_day", "channel_id", "assigned_person", "status"],
            "fields": [
                ("route_code", "text", None, True),
                ("route_name", "text", None, True),
                ("territory", "select", TERRITORIES, True),
                ("county", "text", None, False),
                ("route_day", "select", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], False),
                ("channel_id", "fk_channel", None, True),
                ("assigned_person", "text", None, False),
                ("description", "textarea", None, False),
                ("status", "select", ["Active", "Inactive", "Under Review", "Suspended"], True),
            ],
            "kpis": [("Total Routes", "count"), ("Active", ("status", "Active")), ("Under Review", ("status", "Under Review")), ("Suspended", ("status", "Suspended"))],
            "chart_field": "territory",
            "detail": True,
        },
        "visits": {
            "title": "Visits",
            "endpoint": "visits",
            "model": Visit,
            "url": "/visits",
            "search": ["visit_number", "territory", "contact_person", "visit_outcome"],
            "filters": ["territory", "route_id", "customer_id", "visit_status", "visit_outcome", "purpose"],
            "table": ["visit_number", "visit_date", "customer_id", "route_id", "territory", "purpose", "visit_status", "visit_outcome"],
            "fields": [
                ("visit_number", "text", None, True),
                ("visit_date", "date", None, True),
                ("visit_time", "time", None, False),
                ("customer_id", "fk_customer", None, True),
                ("route_id", "fk_route", None, True),
                ("territory", "select", TERRITORIES, True),
                ("purpose", "select", ["Routine Visit", "New Customer Prospecting", "Order Follow-Up", "Relationship Management", "Product Listing", "Complaint Resolution", "Competitor Monitoring", "Opportunity Assessment", "Account Recovery"], False),
                ("contact_person", "text", None, False),
                ("phone", "text", None, False),
                ("arrival_time", "time", None, False),
                ("departure_time", "time", None, False),
                ("visit_status", "select", ["Planned", "Completed", "Missed", "Cancelled", "Rescheduled"], True),
                ("visit_outcome", "select", ["Successful", "Partially Successful", "No Contact", "Customer Closed", "Follow-Up Required", "Opportunity Identified", "Competitor Activity Observed"], False),
                ("next_action", "textarea", None, False),
                ("next_visit_date", "date", None, False),
                ("notes", "textarea", None, False),
            ],
            "kpis": [("Planned Visits", ("visit_status", "Planned")), ("Completed", ("visit_status", "Completed")), ("Missed", ("visit_status", "Missed")), ("Coverage %", "coverage")],
            "chart_field": "visit_status",
            "detail": True,
        },
        "opportunities": {
            "title": "Opportunities",
            "endpoint": "opportunities",
            "model": Opportunity,
            "url": "/opportunities",
            "search": ["opportunity_code", "title", "territory", "owner"],
            "filters": ["status", "priority", "channel_id", "territory", "opportunity_type", "probability", "owner"],
            "table": ["opportunity_code", "customer_id", "territory", "product_category", "estimated_value", "probability", "priority", "status", "owner"],
            "fields": [
                ("opportunity_code", "text", None, True),
                ("customer_id", "fk_customer", None, True),
                ("territory", "select", TERRITORIES, True),
                ("channel_id", "fk_channel", None, True),
                ("product_category", "text", None, False),
                ("opportunity_type", "select", ["New Customer", "New Product Listing", "Range Expansion", "Distributor Expansion", "Contract Opportunity", "Institution Tender", "Hotel Listing", "Shelf Space Expansion", "Market Expansion", "Account Recovery"], False),
                ("title", "text", None, True),
                ("description", "textarea", None, False),
                ("estimated_value", "number", None, True),
                ("probability", "select", ["0", "25", "50", "75", "100"], True),
                ("priority", "select", ["Critical", "High", "Medium", "Low"], True),
                ("status", "select", ["Open", "Qualified", "In Progress", "Negotiation", "Won", "Lost", "On Hold"], True),
                ("owner", "text", None, False),
                ("source", "select", ["Visit", "Competitor Activity", "Lost Account", "SWOT", "Direct Prospecting", "Referral", "Management Initiative"], False),
                ("next_action", "textarea", None, False),
                ("target_close_date", "date", None, False),
                ("actual_close_date", "date", None, False),
                ("notes", "textarea", None, False),
            ],
            "kpis": [("Total Opportunities", "count"), ("Open", ("status", "Open")), ("Won", ("status", "Won")), ("Pipeline Value", "pipeline")],
            "chart_field": "status",
            "detail": True,
        },
        "competitors": {
            "title": "Competitors",
            "endpoint": "competitors",
            "model": CompetitorActivity,
            "url": "/competitors",
            "search": ["competitor_name", "brand_name", "product_name", "territory"],
            "filters": ["competitor_name", "activity_type", "impact_level", "territory", "channel_id", "status"],
            "table": ["date_observed", "competitor_name", "brand_name", "activity_type", "territory", "impact_level", "status", "owner"],
            "fields": [
                ("date_observed", "date", None, True),
                ("customer_id", "fk_customer", None, True),
                ("territory", "select", TERRITORIES, True),
                ("channel_id", "fk_channel", None, True),
                ("competitor_name", "select", ["Brookside", "KCC", "Bidco", "Kevian", "Trufoods", "Delamere", "Bio Foods", "Other"], True),
                ("brand_name", "text", None, False),
                ("product_name", "text", None, False),
                ("activity_type", "select", ["Promotion", "Price Reduction", "Price Increase", "New Product Launch", "Shelf Expansion", "Sampling", "Merchandising", "Freezer Placement", "Distributor Appointment", "Brand Activation", "Competitor Visit", "Other"], True),
                ("description", "textarea", None, False),
                ("price_observed", "number", None, False),
                ("promotion_details", "textarea", None, False),
                ("photo_path", "text", None, False),
                ("impact_level", "select", ["Critical", "High", "Medium", "Low"], True),
                ("recommended_action", "textarea", None, False),
                ("status", "select", ["Open", "Monitoring", "Action Required", "Closed"], True),
                ("owner", "text", None, False),
            ],
            "kpis": [("Total Activities", "count"), ("Active Threats", ("status", "Open")), ("Critical", ("impact_level", "Critical")), ("Action Required", ("status", "Action Required"))],
            "chart_field": "competitor_name",
            "detail": True,
        },
        "lost_accounts": {
            "title": "Lost Accounts",
            "endpoint": "lost_accounts",
            "model": LostAccount,
            "url": "/lost-accounts",
            "search": ["territory", "competitor_name", "assigned_to", "reason_category"],
            "filters": ["status", "recovery_probability", "reason_category", "competitor_name", "territory", "channel_id", "assigned_to"],
            "table": ["customer_id", "territory", "estimated_monthly_value", "reason_category", "competitor_name", "recovery_probability", "status", "assigned_to"],
            "fields": [
                ("customer_id", "fk_customer", None, True),
                ("territory", "select", TERRITORIES, True),
                ("channel_id", "fk_channel", None, True),
                ("date_lost", "date", None, False),
                ("last_order_date", "date", None, False),
                ("estimated_monthly_value", "number", None, False),
                ("reason_category", "select", ["Price", "Competitor Activity", "Poor Service", "Stock Availability", "Relationship Breakdown", "Credit Issues", "Product Quality", "Distribution Issues", "Management Decision", "Other"], True),
                ("reason_description", "textarea", None, False),
                ("competitor_name", "text", None, False),
                ("recovery_probability", "select", ["Very High", "High", "Medium", "Low", "Very Low"], True),
                ("status", "select", ["Open", "Under Investigation", "Recovery Plan Active", "Recovered", "Permanently Lost", "Closed"], True),
                ("assigned_to", "text", None, False),
                ("recovery_action", "textarea", None, False),
                ("target_recovery_date", "date", None, False),
                ("actual_recovery_date", "date", None, False),
                ("notes", "textarea", None, False),
            ],
            "kpis": [("Total Lost", "count"), ("Recovery Pipeline", ("status", "Recovery Plan Active")), ("Recovered", ("status", "Recovered")), ("Revenue at Risk", "recovery_value")],
            "chart_field": "reason_category",
            "detail": True,
        },
        "action_plans": {
            "title": "Action Plans",
            "endpoint": "action_plans",
            "model": ActionPlan,
            "url": "/action-plans",
            "search": ["action_code", "title", "owner", "territory", "source_module"],
            "filters": ["priority", "status", "owner", "territory", "channel_id", "source_module"],
            "table": ["action_code", "title", "source_module", "territory", "priority", "status", "owner", "target_date", "progress_percentage"],
            "fields": [
                ("action_code", "text", None, True),
                ("title", "text", None, True),
                ("description", "textarea", None, False),
                ("source_module", "select", ["SWOT", "Visit", "Opportunity", "Competitor Activity", "Lost Account", "Management Initiative", "Direct Assignment"], False),
                ("source_record_id", "number", None, False),
                ("territory", "select", TERRITORIES, False),
                ("channel_id", "fk_channel", None, False),
                ("customer_id", "fk_customer", None, False),
                ("priority", "select", ["Critical", "High", "Medium", "Low"], True),
                ("status", "select", ["Open", "In Progress", "Pending", "Completed", "Cancelled", "Overdue"], True),
                ("owner", "text", None, True),
                ("start_date", "date", None, False),
                ("target_date", "date", None, False),
                ("completion_date", "date", None, False),
                ("progress_percentage", "number", None, False),
                ("expected_impact", "textarea", None, False),
                ("actual_impact", "textarea", None, False),
                ("notes", "textarea", None, False),
            ],
            "kpis": [("Total Actions", "count"), ("Open", ("status", "Open")), ("Completed", ("status", "Completed")), ("Completion %", "completion")],
            "chart_field": "status",
            "detail": True,
        },
    }


def apply_search_and_filters(query, config):
    search = request.args.get("q", "").strip()
    if search:
        clauses = [
            cast(getattr(config["model"], field), String).ilike(f"%{search}%")
            for field in config["search"]
            if hasattr(config["model"], field)
        ]
        if clauses:
            query = query.filter(or_(*clauses))
    for field in config["filters"]:
        value = request.args.get(field)
        if value:
            query = query.filter(getattr(config["model"], field) == value)
    return query


def kpi_value(config, spec):
    model = config["model"]
    if spec == "count":
        return model.query.count()
    if spec == "coverage":
        planned = Visit.query.filter(Visit.visit_status.in_(["Planned", "Completed", "Missed"])).count()
        completed = Visit.query.filter_by(visit_status="Completed").count()
        return f"{round((completed / planned) * 100) if planned else 0}%"
    if spec == "completion":
        total = ActionPlan.query.count()
        completed = ActionPlan.query.filter_by(status="Completed").count()
        return f"{round((completed / total) * 100) if total else 0}%"
    if spec == "pipeline":
        value = db.session.query(func.coalesce(func.sum(Opportunity.estimated_value), 0)).filter(
            Opportunity.status.notin_(["Won", "Lost"])
        ).scalar()
        return f"KES {value:,.0f}"
    if spec == "recovery_value":
        value = db.session.query(func.coalesce(func.sum(LostAccount.estimated_monthly_value), 0)).filter(
            LostAccount.recovery_probability.in_(["High", "Very High"])
        ).scalar()
        return f"KES {value:,.0f}"
    field, value = spec
    return model.query.filter(getattr(model, field) == value).count()


def chart_data(config):
    field = getattr(config["model"], config["chart_field"])
    rows = (
        db.session.query(field, func.count(config["model"].id))
        .group_by(field)
        .order_by(func.count(config["model"].id).desc())
        .all()
    )
    return {
        "labels": [str(row[0] or "Unspecified") for row in rows],
        "values": [row[1] for row in rows],
    }


def display_value(row, field):
    value = getattr(row, field)
    if field == "channel_id" and value:
        channel = db.session.get(Channel, value)
        return channel.channel_name if channel else value
    if field == "customer_id" and value:
        customer = db.session.get(Customer, value)
        return customer.customer_name if customer else value
    if field == "route_id" and value:
        route = db.session.get(Route, value)
        return route.route_name if route else value
    return serialize_value(value)


def build_record_from_form(row, config):
    for field, _type, _choices, _required in config["fields"]:
        column = config["model"].__table__.columns[field]
        value = parse_value(request.form.get(field), column)
        if field == "progress_percentage" and value is not None:
            value = max(0, min(100, value))
        setattr(row, field, value)


def export_rows(config, rows, export_format):
    data = [
        {field.replace("_", " ").title(): display_value(row, field) for field in config["table"]}
        for row in rows
    ]
    frame = pd.DataFrame(data)
    filename = config["endpoint"].replace("_", "-")
    if export_format == "csv":
        buffer = StringIO()
        frame.to_csv(buffer, index=False)
        return Response(
            buffer.getvalue(),
            mimetype="text/csv",
            headers={"Content-Disposition": f"attachment; filename={filename}.csv"},
        )
    if export_format == "excel":
        buffer = BytesIO()
        with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
            frame.to_excel(writer, index=False, sheet_name=config["title"][:31])
        buffer.seek(0)
        return send_file(
            buffer,
            as_attachment=True,
            download_name=f"{filename}.xlsx",
            mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
    lines = [config["title"], f"Generated: {datetime.now():%Y-%m-%d %H:%M}", ""]
    lines.extend(frame.to_string(index=False).splitlines() if not frame.empty else ["No data"])
    text = "\\n".join(lines).replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
    pdf = f"%PDF-1.4\n1 0 obj<</Type/Catalog/Pages 2 0 R>>endobj\n2 0 obj<</Type/Pages/Count 1/Kids[3 0 R]>>endobj\n3 0 obj<</Type/Page/Parent 2 0 R/MediaBox[0 0 612 792]/Contents 4 0 R/Resources<</Font<</F1 5 0 R>>>>>>endobj\n4 0 obj<</Length {len(text)+80}>>stream\nBT /F1 9 Tf 36 756 Td 12 TL ({text[:3000]}) Tj ET\nendstream endobj\n5 0 obj<</Type/Font/Subtype/Type1/BaseFont/Helvetica>>endobj\ntrailer<</Root 1 0 R>>\n%%EOF"
    return Response(
        pdf,
        mimetype="application/pdf",
        headers={"Content-Disposition": f"attachment; filename={filename}.pdf"},
    )


def register_crud(module_key):
    configs = module_config()
    config = configs[module_key]
    bp = Blueprint(config["endpoint"], __name__, url_prefix=config["url"])

    @bp.route("/")
    @login_required
    def index():
        query = apply_search_and_filters(config["model"].query, config)
        page = request.args.get("page", 1, type=int)
        pagination = query.order_by(config["model"].id.desc()).paginate(
            page=page, per_page=15, error_out=False
        )
        kpis = [(label, kpi_value(config, spec)) for label, spec in config["kpis"]]
        return render_template(
            "module/index.html",
            config=config,
            rows=pagination.items,
            pagination=pagination,
            kpis=kpis,
            chart=chart_data(config),
            filter_options=filter_options(config),
            channels=choices_from_model(Channel, "id", "channel_name"),
            customers=choices_from_model(Customer, "id", "customer_name"),
            routes=choices_from_model(Route, "id", "route_name"),
            display_value=display_value,
            request_args=request.args,
        )

    @bp.route("/create", methods=["GET", "POST"])
    @login_required
    def create():
        admin_required()
        row = config["model"]()
        if request.method == "POST":
            build_record_from_form(row, config)
            db.session.add(row)
            db.session.commit()
            flash(f"{config['title']} record created.", "success")
            return redirect(url_for(f"{config['endpoint']}.index"))
        return render_template(
            "module/form.html",
            config=config,
            row=row,
            channels=choices_from_model(Channel, "id", "channel_name"),
            customers=choices_from_model(Customer, "id", "customer_name"),
            routes=choices_from_model(Route, "id", "route_name"),
            serialize_value=serialize_value,
        )

    @bp.route("/<int:record_id>")
    @login_required
    def detail(record_id):
        row = db.session.get(config["model"], record_id) or abort(404)
        return render_template(
            "module/detail.html",
            config=config,
            row=row,
            display_value=display_value,
        )

    @bp.route("/<int:record_id>/edit", methods=["GET", "POST"])
    @login_required
    def edit(record_id):
        admin_required()
        row = db.session.get(config["model"], record_id) or abort(404)
        if request.method == "POST":
            build_record_from_form(row, config)
            db.session.commit()
            flash(f"{config['title']} record updated.", "success")
            return redirect(url_for(f"{config['endpoint']}.detail", record_id=record_id))
        return render_template(
            "module/form.html",
            config=config,
            row=row,
            channels=choices_from_model(Channel, "id", "channel_name"),
            customers=choices_from_model(Customer, "id", "customer_name"),
            routes=choices_from_model(Route, "id", "route_name"),
            serialize_value=serialize_value,
        )

    @bp.route("/<int:record_id>/delete", methods=["POST"])
    @login_required
    def delete(record_id):
        admin_required()
        row = db.session.get(config["model"], record_id) or abort(404)
        db.session.delete(row)
        db.session.commit()
        flash(f"{config['title']} record deleted.", "success")
        return redirect(url_for(f"{config['endpoint']}.index"))

    @bp.route("/export/<export_format>")
    @login_required
    def export(export_format):
        admin_required()
        if export_format not in {"csv", "excel", "pdf"}:
            abort(404)
        rows = apply_search_and_filters(config["model"].query, config).all()
        return export_rows(config, rows, export_format)

    @bp.route("/print")
    @login_required
    def print_view():
        rows = apply_search_and_filters(config["model"].query, config).all()
        return render_template(
            "module/print.html",
            config=config,
            rows=rows,
            display_value=display_value,
            generated_at=datetime.now(),
        )

    return bp
