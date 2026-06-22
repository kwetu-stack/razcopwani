from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

from .action_plan import ActionPlan
from .channel import Channel
from .competitor import CompetitorActivity
from .customer import Customer
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
    "LostAccount",
    "Opportunity",
    "Product",
    "Route",
    "Swot",
    "User",
    "Visit",
]
