from . import db
from .mixins import TimestampMixin


class Channel(TimestampMixin, db.Model):
    __tablename__ = "channels"

    id = db.Column(db.Integer, primary_key=True)
    channel_name = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.Text)
    growth_target = db.Column(db.Float, default=25)
    manager = db.Column(db.String(120))
    status = db.Column(db.String(40), default="Active", nullable=False)
    notes = db.Column(db.Text)

    customers = db.relationship("Customer", back_populates="channel", lazy=True)
    routes = db.relationship("Route", back_populates="channel", lazy=True)
    opportunities = db.relationship("Opportunity", back_populates="channel", lazy=True)
    competitor_activities = db.relationship(
        "CompetitorActivity", back_populates="channel", lazy=True
    )
    lost_accounts = db.relationship("LostAccount", back_populates="channel", lazy=True)
    action_plans = db.relationship("ActionPlan", back_populates="channel", lazy=True)
