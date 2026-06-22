from . import db
from .mixins import TimestampMixin


class CompetitorActivity(TimestampMixin, db.Model):
    __tablename__ = "competitor_activities"

    id = db.Column(db.Integer, primary_key=True)
    date_observed = db.Column(db.Date, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), nullable=False)
    territory = db.Column(db.String(80), nullable=False)
    channel_id = db.Column(db.Integer, db.ForeignKey("channels.id"), nullable=False)
    competitor_name = db.Column(db.String(120), nullable=False)
    brand_name = db.Column(db.String(120))
    product_name = db.Column(db.String(120))
    activity_type = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    price_observed = db.Column(db.Float)
    promotion_details = db.Column(db.Text)
    photo_path = db.Column(db.String(255))
    impact_level = db.Column(db.String(40), nullable=False)
    recommended_action = db.Column(db.Text)
    status = db.Column(db.String(40), default="Open", nullable=False)
    owner = db.Column(db.String(120))

    customer = db.relationship("Customer", back_populates="competitor_activities", lazy=True)
    channel = db.relationship(
        "Channel", back_populates="competitor_activities", lazy=True
    )
