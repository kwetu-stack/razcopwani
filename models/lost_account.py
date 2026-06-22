from . import db
from .mixins import TimestampMixin


class LostAccount(TimestampMixin, db.Model):
    __tablename__ = "lost_accounts"

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), nullable=False)
    territory = db.Column(db.String(80), nullable=False)
    channel_id = db.Column(db.Integer, db.ForeignKey("channels.id"), nullable=False)
    date_lost = db.Column(db.Date)
    last_order_date = db.Column(db.Date)
    estimated_monthly_value = db.Column(db.Float, default=0)
    reason_category = db.Column(db.String(120), nullable=False)
    reason_description = db.Column(db.Text)
    competitor_name = db.Column(db.String(120))
    recovery_probability = db.Column(db.String(40), nullable=False)
    status = db.Column(db.String(80), nullable=False)
    assigned_to = db.Column(db.String(120))
    recovery_action = db.Column(db.Text)
    target_recovery_date = db.Column(db.Date)
    actual_recovery_date = db.Column(db.Date)
    notes = db.Column(db.Text)

    customer = db.relationship("Customer", back_populates="lost_accounts", lazy=True)
    channel = db.relationship("Channel", back_populates="lost_accounts", lazy=True)
