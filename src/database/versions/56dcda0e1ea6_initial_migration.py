"""Initial migration

Revision ID: 56dcda0e1ea6
Revises: 
Create Date: 2023-02-19 22:02:32.700002

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "56dcda0e1ea6"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "tags",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_tags")),
    )
    op.create_table(
        "trading_assets",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("full_name", sa.String(length=255), nullable=False),
        sa.Column("iso_code", sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_trading_assets")),
    )
    op.create_table(
        "trading_asset_tags",
        sa.Column("trading_asset_id", sa.Integer(), nullable=False),
        sa.Column("tag_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["tag_id"], ["tags.id"], name=op.f("fk_trading_asset_tags_tag_id_'tags's")
        ),
        sa.ForeignKeyConstraint(
            ["trading_asset_id"],
            ["trading_assets.id"],
            name=op.f("fk_trading_asset_tags_trading_asset_id_'trading_assets's"),
        ),
        sa.PrimaryKeyConstraint(
            "trading_asset_id", "tag_id", name=op.f("pk_trading_asset_tags")
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("trading_asset_tags")
    op.drop_table("trading_assets")
    op.drop_table("tags")
    # ### end Alembic commands ###
