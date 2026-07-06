import os
import tempfile
import unittest

from flask import Flask
from sqlalchemy import inspect, text

from models import db
from app import ensure_order_items_schema


class OrderItemSchemaMigrationTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.temp_dir, "test_razco.db")
        self.app = Flask(__name__)
        self.app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{self.db_path}"
        self.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        self.app.config["TESTING"] = True
        db.init_app(self.app)

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.engine.dispose()
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def test_adds_missing_price_column_to_order_items(self):
        with self.app.app_context():
            db.session.execute(
                text(
                    "CREATE TABLE order_items (id INTEGER PRIMARY KEY, order_id INTEGER NOT NULL, product_id INTEGER NOT NULL, quantity NUMERIC(10, 2) NOT NULL)"
                )
            )
            db.session.commit()

            ensure_order_items_schema(self.app)

            inspector = inspect(db.engine)
            columns = [
                column["name"] for column in inspector.get_columns("order_items")
            ]

            self.assertIn("price", columns)
            self.assertEqual(columns.count("price"), 1)


if __name__ == "__main__":
    unittest.main()
