from . import db
from .mixins import TimestampMixin


class ActionPlan(TimestampMixin, db.Model):
    __tablename__ = "action_plans"

    id = db.Column(db.Integer, primary_key=True)
    action_code = db.Column(db.String(40), unique=True, nullable=False)
    title = db.Column(db.String(180), nullable=False)
    description = db.Column(db.Text)
    source_module = db.Column(db.String(80))
    source_record_id = db.Column(db.Integer)
    territory = db.Column(db.String(80))
    channel_id = db.Column(db.Integer, db.ForeignKey("channels.id"))
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"))
    priority = db.Column(db.String(40), nullable=False)
    status = db.Column(db.String(40), nullable=False)
    owner = db.Column(db.String(120), nullable=False)
    start_date = db.Column(db.Date)
    target_date = db.Column(db.Date)
    completion_date = db.Column(db.Date)
    progress_percentage = db.Column(db.Integer, default=0, nullable=False)
    expected_impact = db.Column(db.Text)
    actual_impact = db.Column(db.Text)
    notes = db.Column(db.Text)

    customer = db.relationship("Customer", back_populates="action_plans", lazy=True)
    channel = db.relationship("Channel", back_populates="action_plans", lazy=True)
