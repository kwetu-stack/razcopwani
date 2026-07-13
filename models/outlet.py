from . import db
from .mixins import TimestampMixin


class Outlet(TimestampMixin, db.Model):
    __tablename__ = "outlets"

    id = db.Column(db.Integer, primary_key=True)

    outlet_name = db.Column(
        db.String(150),
        nullable=False,
        unique=True,
    )

    status = db.Column(
        db.String(20),
        nullable=False,
        default="Active",
    )

    def __repr__(self):
        return f"<Outlet {self.outlet_name}>"