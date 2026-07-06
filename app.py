import os

from flask import Flask, render_template
from flask_login import LoginManager, login_required
from flask_wtf import CSRFProtect
from sqlalchemy import inspect, text

from config import Config
from models import User, db

from blueprints.daily_sales.routes import daily_sales_bp
from blueprints.orders.routes import orders_bp

login_manager = LoginManager()
login_manager.login_view = "auth.login"

csrf = CSRFProtect()


def ensure_order_items_schema(app):
    with app.app_context():
        inspector = inspect(db.engine)
        if "order_items" not in inspector.get_table_names():
            db.create_all()
            return

        columns = {column["name"] for column in inspector.get_columns("order_items")}
        if "price" not in columns:
            dialect_name = db.engine.dialect.name
            if dialect_name == "sqlite":
                statement = text(
                    "ALTER TABLE order_items ADD COLUMN price NUMERIC(10, 0) NOT NULL DEFAULT 0"
                )
            else:
                statement = text(
                    "ALTER TABLE order_items ADD COLUMN IF NOT EXISTS price NUMERIC(10, 0) NOT NULL DEFAULT 0"
                )

            with db.engine.begin() as connection:
                connection.execute(statement)
            return

        price_column = next(
            column
            for column in inspector.get_columns("order_items")
            if column["name"] == "price"
        )
        price_type = str(price_column["type"]).upper()

        if (
            "NUMERIC(10, 0)" in price_type
            or "DECIMAL(10, 0)" in price_type
            or "INTEGER" in price_type
        ):
            return

        dialect_name = db.engine.dialect.name
        if dialect_name == "sqlite":
            with db.engine.begin() as connection:
                connection.execute(
                    text("ALTER TABLE order_items RENAME TO order_items_old")
                )
                connection.execute(text("""
                        CREATE TABLE order_items (
                            id INTEGER NOT NULL,
                            order_id INTEGER NOT NULL,
                            product_id INTEGER NOT NULL,
                            quantity NUMERIC(10, 2) NOT NULL DEFAULT 0,
                            price NUMERIC(10, 0) NOT NULL DEFAULT 0,
                            PRIMARY KEY (id),
                            FOREIGN KEY(order_id) REFERENCES orders (id),
                            FOREIGN KEY(product_id) REFERENCES products (id)
                        )
                        """))
                connection.execute(text("""
                        INSERT INTO order_items (id, order_id, product_id, quantity, price)
                        SELECT id, order_id, product_id, quantity, CAST(price AS NUMERIC(10, 0))
                        FROM order_items_old
                        """))
                connection.execute(text("DROP TABLE order_items_old"))
        else:
            with db.engine.begin() as connection:
                connection.execute(
                    text(
                        "ALTER TABLE order_items ALTER COLUMN price TYPE NUMERIC(10,0)"
                    )
                )


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.config["UPLOAD_FOLDER"].mkdir(parents=True, exist_ok=True)
    app.config["REPORT_FOLDER"].mkdir(parents=True, exist_ok=True)

    db.init_app(app)
    ensure_order_items_schema(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    from blueprints.action_plans.routes import action_plans_bp
    from blueprints.auth.routes import auth_bp
    from blueprints.channels.routes import channels_bp
    from blueprints.competitors.routes import competitors_bp
    from blueprints.customers.routes import customers_bp
    from blueprints.dashboard.routes import dashboard_bp
    from blueprints.lost_accounts.routes import lost_accounts_bp
    from blueprints.opportunities.routes import opportunities_bp
    from blueprints.products.routes import products_bp
    from blueprints.reports.routes import reports_bp
    from blueprints.routes.routes import routes_bp
    from blueprints.swot.routes import swot_bp
    from blueprints.visits.routes import visits_bp

    # Register Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(swot_bp)
    app.register_blueprint(customers_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(daily_sales_bp)
    app.register_blueprint(channels_bp)
    app.register_blueprint(routes_bp)
    app.register_blueprint(visits_bp)
    app.register_blueprint(opportunities_bp)
    app.register_blueprint(competitors_bp)
    app.register_blueprint(lost_accounts_bp)
    app.register_blueprint(action_plans_bp)
    app.register_blueprint(reports_bp)
    app.register_blueprint(orders_bp)

    @app.errorhandler(403)
    @login_required
    def forbidden(error):
        return render_template("errors/403.html"), 403

    @app.errorhandler(404)
    @login_required
    def not_found(error):
        return render_template("errors/404.html"), 404

    @app.errorhandler(500)
    def server_error(error):
        db.session.rollback()
        return render_template("errors/500.html"), 500

    return app


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


if __name__ == "__main__":
    app = create_app()

    with app.app_context():
        ensure_order_items_schema(app)

    port = int(os.getenv("PORT", "5000"))

    app.run(debug=False, host="0.0.0.0", port=port)
