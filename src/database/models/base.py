from sqlalchemy import schema
from sqlalchemy.orm import declarative_base

# Recommended naming convention used by Alembic.
NAMING_CONVENTION = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)rs",
    "pk": "pk_%(table_name)s",
}

metadata = schema.MetaData(naming_convention=NAMING_CONVENTION)
Base = declarative_base(metadata=metadata)
