from datetime import datetime

from models import db


class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    order_number = db.Column(
        db.String(30),
        unique=True,
        nullable=False
    )

    order_date = db.Column(
        db.Date,
        nullable=False
    )

    customer_id = db.Column(
        db.Integer,
        db.ForeignKey("customers.id"),
        nullable=False
    )

    sales_rep_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    remarks = db.Column(
        db.Text
    )

    status = db.Column(
        db.String(20),
        nullable=False,
        default="Pending"
    )

    # Audit fields

    invoiced_by_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=True
    )

    invoiced_at = db.Column(
        db.DateTime,
        nullable=True
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    customer = db.relationship(
        "Customer",
        backref="orders"
    )

    sales_rep = db.relationship(
        "User",
        foreign_keys=[sales_rep_id],
        backref="sales_orders"
    )

    invoiced_by = db.relationship(
        "User",
        foreign_keys=[invoiced_by_id],
        backref="invoiced_orders"
    )

    items = db.relationship(
        "OrderItem",
        back_populates="order",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Order {self.order_number}>"