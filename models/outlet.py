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

    is_active = db.Column(
        db.Boolean,
        nullable=False,
        default=True,
    )

    def __repr__(self):
        return f"<Outlet {self.outlet_name}>"
