from . import db
from .mixins import TimestampMixin


class Merchandiser(TimestampMixin, db.Model):
    __tablename__ = "merchandisers"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(
        db.String(100),
        nullable=False,
        unique=True,
    )

    status = db.Column(
        db.String(20),
        nullable=False,
        default="Active",
    )

    def __repr__(self):
        return f"<Merchandiser {self.name}>"