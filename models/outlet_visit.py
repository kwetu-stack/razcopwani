from . import db
from .mixins import TimestampMixin


class OutletVisit(TimestampMixin, db.Model):
    __tablename__ = "outlet_visits"

    id = db.Column(db.Integer, primary_key=True)

    visit_date = db.Column(
        db.Date,
        nullable=False,
    )

    merchandiser_id = db.Column(
        db.Integer,
        db.ForeignKey("merchandisers.id"),
        nullable=False,
    )

    outlet_id = db.Column(
        db.Integer,
        db.ForeignKey("outlets.id"),
        nullable=False,
    )

    icecream_stock = db.Column(
        db.String(20),
        nullable=False,
    )

    sauces_stock = db.Column(
        db.String(20),
        nullable=False,
    )

    bakery_stock = db.Column(
        db.String(20),
        nullable=False,
    )

    private_label_stock = db.Column(
        db.String(20),
        nullable=False,
    )

    freezer_condition = db.Column(
        db.String(30),
        nullable=False,
    )

    order_placed = db.Column(
        db.Boolean,
        nullable=False,
        default=False,
    )

    notes = db.Column(db.Text)

    created_by = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False,
    )

    merchandiser = db.relationship("Merchandiser")

    outlet = db.relationship("Outlet")

    creator = db.relationship("User")

    def __repr__(self):
        return (
            f"<OutletVisit {self.visit_date} - "
            f"{self.outlet_id}>"
        )