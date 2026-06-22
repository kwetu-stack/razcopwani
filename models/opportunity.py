from . import db
from .mixins import TimestampMixin


class Opportunity(TimestampMixin, db.Model):
    __tablename__ = "opportunities"

    id = db.Column(db.Integer, primary_key=True)
    opportunity_code = db.Column(db.String(40), unique=True, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), nullable=False)
    territory = db.Column(db.String(80), nullable=False)
    channel_id = db.Column(db.Integer, db.ForeignKey("channels.id"), nullable=False)
    product_category = db.Column(db.String(80))
    opportunity_type = db.Column(db.String(120))
    title = db.Column(db.String(180), nullable=False)
    description = db.Column(db.Text)
    estimated_value = db.Column(db.Float, nullable=False, default=0)
    probability = db.Column(db.Integer, nullable=False, default=0)
    priority = db.Column(db.String(40), default="Medium", nullable=False)
    status = db.Column(db.String(40), nullable=False)
    owner = db.Column(db.String(120))
    source = db.Column(db.String(120))
    next_action = db.Column(db.Text)
    target_close_date = db.Column(db.Date)
    actual_close_date = db.Column(db.Date)
    notes = db.Column(db.Text)

    customer = db.relationship("Customer", back_populates="opportunities", lazy=True)
    channel = db.relationship("Channel", back_populates="opportunities", lazy=True)
