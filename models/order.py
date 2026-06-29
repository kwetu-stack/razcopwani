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
        backref="orders"
    )

    items = db.relationship(
        "OrderItem",
        back_populates="order",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Order {self.order_number}>"