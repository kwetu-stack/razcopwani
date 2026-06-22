from . import db
from .mixins import TimestampMixin


class Swot(TimestampMixin, db.Model):
    __tablename__ = "swot"

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(40), nullable=False)
    title = db.Column(db.String(180), nullable=False)
    description = db.Column(db.Text)
    territory = db.Column(db.String(80))
    channel = db.Column(db.String(80))
    priority = db.Column(db.String(40), default="Medium", nullable=False)
    status = db.Column(db.String(40), default="Open", nullable=False)
    owner = db.Column(db.String(120))
