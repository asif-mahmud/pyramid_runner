from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import MetaData
from sqlalchemy import (
    Column,
    Integer,
    DateTime,
)
from sqlalchemy import func
from sqlalchemy.ext.declarative import declared_attr
import re


# Recommended naming convention used by Alembic, as various different database
# providers will autogenerate vastly different names making migrations more
# difficult. See: http://alembic.zzzcomputing.com/en/latest/naming.html
NAMING_CONVENTION = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}


class ModelBase(object):

    id = Column(Integer, primary_key=True)
    created_on = Column(DateTime, server_default=func.now())
    updated_on = Column(DateTime, server_default=func.now(), server_onupdate=func.now())

    @declared_attr
    def __tablename__(cls):
        name = cls.__name__
        return (
            name[0].lower() +
            re.sub(
                r'([A-Z])',
                lambda m: '_' + m.group(0).lower(),
                name[1:]
            )
        )


metadata = MetaData(naming_convention=NAMING_CONVENTION)
Base = declarative_base(metadata=metadata, cls=ModelBase)
