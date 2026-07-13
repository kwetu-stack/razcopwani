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

    is_active = db.Column(
        db.Boolean,
        nullable=False,
        default=True,
    )

    def __repr__(self):
        return f"<Merchandiser {self.name}>"