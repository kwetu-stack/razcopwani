"""Create outlet visits

Revision ID: c1e2b7d48a90
Revises: 9c3d66c8c54f
Create Date: 2026-07-13 18:10:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c1e2b7d48a90"
down_revision = "9c3d66c8c54f"
branch_labels = None
depends_on = None


def upgrade():
    bind = op.get_bind()
    inspector = sa.inspect(bind)

    if "outlet_visits" in inspector.get_table_names():
        return

    op.create_table(
        "outlet_visits",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("visit_date", sa.Date(), nullable=False),
        sa.Column("merchandiser_id", sa.Integer(), nullable=False),
        sa.Column("outlet_id", sa.Integer(), nullable=False),
        sa.Column("icecream_stock", sa.String(length=20), nullable=False),
        sa.Column("sauces_stock", sa.String(length=20), nullable=False),
        sa.Column("bakery_stock", sa.String(length=20), nullable=False),
        sa.Column("private_label_stock", sa.String(length=20), nullable=False),
        sa.Column("freezer_condition", sa.String(length=30), nullable=False),
        sa.Column("order_placed", sa.Boolean(), nullable=False),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.Column("created_by", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(["created_by"], ["users.id"]),
        sa.ForeignKeyConstraint(["merchandiser_id"], ["merchandisers.id"]),
        sa.ForeignKeyConstraint(["outlet_id"], ["outlets.id"]),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    bind = op.get_bind()
    inspector = sa.inspect(bind)

    if "outlet_visits" in inspector.get_table_names():
        op.drop_table("outlet_visits")
