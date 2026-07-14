"""Create outlets master

Revision ID: 9c3d66c8c54f
Revises: 41a58f0b3944
Create Date: 2026-07-13 17:05:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "9c3d66c8c54f"
down_revision = "41a58f0b3944"
branch_labels = None
depends_on = None


def upgrade():
    bind = op.get_bind()
    inspector = sa.inspect(bind)

    if "outlets" not in inspector.get_table_names():
        op.create_table(
            "outlets",
            sa.Column("id", sa.Integer(), nullable=False),
            sa.Column("outlet_name", sa.String(length=150), nullable=False),
            sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.true()),
            sa.Column("created_at", sa.DateTime(), nullable=False),
            sa.Column("updated_at", sa.DateTime(), nullable=False),
            sa.PrimaryKeyConstraint("id"),
            sa.UniqueConstraint("outlet_name"),
        )
        return

    columns = {
        column["name"]
        for column in inspector.get_columns("outlets")
    }

    with op.batch_alter_table("outlets", schema=None) as batch_op:
        if "is_active" not in columns:
            batch_op.add_column(
                sa.Column(
                    "is_active",
                    sa.Boolean(),
                    nullable=False,
                    server_default=sa.true(),
                )
            )

        if "status" in columns:
            batch_op.drop_column("status")


def downgrade():
    bind = op.get_bind()
    inspector = sa.inspect(bind)

    if "outlets" not in inspector.get_table_names():
        return

    columns = {
        column["name"]
        for column in inspector.get_columns("outlets")
    }

    with op.batch_alter_table("outlets", schema=None) as batch_op:
        if "status" not in columns:
            batch_op.add_column(
                sa.Column(
                    "status",
                    sa.String(length=20),
                    nullable=False,
                    server_default="Active",
                )
            )

        if "is_active" in columns:
            batch_op.drop_column("is_active")
