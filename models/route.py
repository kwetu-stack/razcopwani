from . import db
from .mixins import TimestampMixin


class Route(TimestampMixin, db.Model):
    __tablename__ = "routes"

    id = db.Column(db.Integer, primary_key=True)
    route_code = db.Column(db.String(40), unique=True, nullable=False)
    route_name = db.Column(db.String(140), nullable=False)
    territory = db.Column(db.String(80), nullable=False)
    county = db.Column(db.String(80))
    route_day = db.Column(db.String(20))
    channel_id = db.Column(db.Integer, db.ForeignKey("channels.id"), nullable=False)
    assigned_person = db.Column(db.String(120))
    description = db.Column(db.Text)
    status = db.Column(db.String(40), default="Active", nullable=False)

    channel = db.relationship("Channel", back_populates="routes", lazy=True)
    visits = db.relationship("Visit", back_populates="route", lazy=True)
