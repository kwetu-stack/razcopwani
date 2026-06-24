from datetime import date

from . import db
from .mixins import TimestampMixin


class DailySale(db.Model, TimestampMixin):
    __tablename__ = "daily_sales"

    id = db.Column(db.Integer, primary_key=True)

    sale_date = db.Column(db.Date, nullable=False)

    product_name = db.Column(db.String(100), nullable=False)

    sales_value = db.Column(db.Float, default=0)

    def __repr__(self):
        return f"<DailySale {self.product_name} - {self.sale_date}>"