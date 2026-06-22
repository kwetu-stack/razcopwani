from . import db
from .mixins import TimestampMixin


class Customer(TimestampMixin, db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)
    customer_code = db.Column(db.String(40), unique=True, nullable=False)
    customer_name = db.Column(db.String(160), nullable=False)
    contact_person = db.Column(db.String(120))
    phone = db.Column(db.String(60))
    email = db.Column(db.String(120))
    physical_address = db.Column(db.String(255))
    territory = db.Column(db.String(80), nullable=False)
    channel_id = db.Column(db.Integer, db.ForeignKey("channels.id"), nullable=False)
    customer_status = db.Column(db.String(40), default="Active", nullable=False)
    credit_limit = db.Column(db.Float, default=0)
    notes = db.Column(db.Text)

    channel = db.relationship("Channel", back_populates="customers", lazy=True)
    visits = db.relationship("Visit", back_populates="customer", lazy=True)
    opportunities = db.relationship("Opportunity", back_populates="customer", lazy=True)
    competitor_activities = db.relationship(
        "CompetitorActivity", back_populates="customer", lazy=True
    )
    lost_accounts = db.relationship("LostAccount", back_populates="customer", lazy=True)
    action_plans = db.relationship("ActionPlan", back_populates="customer", lazy=True)
