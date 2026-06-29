from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

from .action_plan import ActionPlan
from .order import Order
from .order_item import OrderItem
from .channel import Channel
from .competitor import CompetitorActivity
from .customer import Customer
from .daily_sale import DailySale
from .lost_account import LostAccount
from .opportunity import Opportunity
from .product import Product
from .route import Route
from .swot import Swot
from .user import User
from .visit import Visit


__all__ = [
    "db",
    "ActionPlan",
    "Channel",
    "CompetitorActivity",
    "Customer",
    "DailySale",
    "LostAccount",
    "Opportunity",
    "Product",
    "Route",
    "Swot",
    "User",
    "Visit",
    "Order",
    "OrderItem",
]