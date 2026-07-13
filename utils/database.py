from sqlalchemy import inspect, text

from models import db


def ensure_order_items_schema(app):
    with app.app_context():
        inspector = inspect(db.engine)

        if "order_items" not in inspector.get_table_names():
            db.create_all()
            return

        columns = {
            column["name"]
            for column in inspector.get_columns("order_items")
        }

        if "price" not in columns:

            dialect_name = db.engine.dialect.name

            if dialect_name == "sqlite":
                statement = text(
                    "ALTER TABLE order_items "
                    "ADD COLUMN price NUMERIC(10,0) "
                    "NOT NULL DEFAULT 0"
                )
            else:
                statement = text(
                    "ALTER TABLE order_items "
                    "ADD COLUMN IF NOT EXISTS price "
                    "NUMERIC(10,0) NOT NULL DEFAULT 0"
                )

            with db.engine.begin() as connection:
                connection.execute(statement)


def initialize_database(app):
    with app.app_context():

        # Create any missing tables
        db.create_all()

        # Existing schema checks
        ensure_order_items_schema(app)