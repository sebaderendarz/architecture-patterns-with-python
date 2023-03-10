"""Add TradingAssetsCommandsLog

Revision ID: 23149751dcbe
Revises: 56dcda0e1ea6
Create Date: 2023-02-28 06:00:25.106341

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "23149751dcbe"
down_revision = "56dcda0e1ea6"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "trading_assets_commands_logs",
        sa.Column("command_id", sa.String(length=255), nullable=False),
        sa.Column("reason", sa.String(length=255), nullable=True),
        sa.Column("status", sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint(
            "command_id", name=op.f("pk_trading_assets_commands_logs")
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("trading_assets_commands_logs")
    # ### end Alembic commands ###
