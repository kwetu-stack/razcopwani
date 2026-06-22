from . import db
from .mixins import TimestampMixin


class Product(TimestampMixin, db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    product_code = db.Column(db.String(40), unique=True, nullable=False)
    product_name = db.Column(db.String(160), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    brand = db.Column(db.String(80))
    unit_size = db.Column(db.String(40))
    selling_price = db.Column(db.Float, default=0)
    status = db.Column(db.String(40), default="Active", nullable=False)
    notes = db.Column(db.Text)
