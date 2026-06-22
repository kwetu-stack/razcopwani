from . import db
from .mixins import TimestampMixin


class Visit(TimestampMixin, db.Model):
    __tablename__ = "visits"

    id = db.Column(db.Integer, primary_key=True)
    visit_number = db.Column(db.String(40), unique=True, nullable=False)
    visit_date = db.Column(db.Date, nullable=False)
    visit_time = db.Column(db.Time)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), nullable=False)
    route_id = db.Column(db.Integer, db.ForeignKey("routes.id"), nullable=False)
    territory = db.Column(db.String(80), nullable=False)
    purpose = db.Column(db.String(120))
    contact_person = db.Column(db.String(120))
    phone = db.Column(db.String(60))
    arrival_time = db.Column(db.Time)
    departure_time = db.Column(db.Time)
    visit_status = db.Column(db.String(40), nullable=False)
    visit_outcome = db.Column(db.String(80))
    next_action = db.Column(db.Text)
    next_visit_date = db.Column(db.Date)
    notes = db.Column(db.Text)

    customer = db.relationship("Customer", back_populates="visits", lazy=True)
    route = db.relationship("Route", back_populates="visits", lazy=True)
