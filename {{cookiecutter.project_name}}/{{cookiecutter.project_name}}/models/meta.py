import re

import sqlalchemy as sa
import sqlalchemy.ext.declarative as declarative
import sqlalchemy.schema as schema


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

# PostgreSQL timestamp update function that can be attached
# to any table's date/datetime column. User should use
# alembic revision sources to attach this function.
PSQL_UPDATED_TIMESTAMP_FNC = sa.text(
    'CREATE OR REPLACE FUNCTION set_updated_timestamp()'
    ' RETURNS TRIGGER'
    ' LANGUAGE plpgsql'
    ' AS $$'
    ' BEGIN'
    ' NEW.updated_on := now();'
    ' RETURN NEW;'
    ' END;'
    '$$;'
)


def psql_update_timestamp_trigger(tablename):
    """SQL text creator function.

    Creates SQL command to attach timestamp update trigger
    function to specified table. Only for PostgreSQL backend.

    Params:
        tablename(str): Actual table name.

    Returns:
        SQL text to attache `PSQL_UPDATED_TIMESTAMP_FNC`
        to a specific table by name `tablename`.
    """
    return sa.text(
        'CREATE TRIGGER {0}_update_timestamp'
        ' BEFORE UPDATE ON {0}'
        ' FOR EACH ROW EXECUTE PROCEDURE set_updated_timestamp();'.format(
            tablename
        )
    )


# Create UUID extension in a PostgreSQL database.
# This should be done via command line psql utility.
PSQL_CREATE_UUID_EXT = sa.text(
    'CREATE EXTENSION IF NOT EXISTS "uuid-ossp"'
)


# SQL command to drop the timestamp update function
# from a PostgreSQL database.
PSQL_DROP_UPDATE_TIMESTAMP_FNC = sa.text(
    'DROP FUNCTION set_updated_timestamp()'
)


# SQL command to drop the UUID extension
# from a PostgreSQL database. Should be done
# via psql utility.
PSQL_DROP_UUID_EXT = sa.text(
    'DROP EXTENSION "uuid-ossp"'
)


class ModelBase(object):
    """Base class for ORM tables.

    Any ORM table model should inherit the `model.meta.Base`
    declarative base. This base class provides -
        1. id for any entry
        2. table name in table_name syntax
        3. created_on and updated_on columns
        4. an abstract __json__ method.
    """

    id = sa.Column(sa.Integer, primary_key=True)
    created_on = sa.Column(sa.DateTime, server_default=sa.func.now())
    updated_on = sa.Column(sa.DateTime, server_default=sa.func.now(),
                           onupdate=sa.func.now())

    @declarative.declared_attr
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

    def __json__(self, request):
        raise NotImplementedError("{} didn't implement __json__(request)"
                                  " method for {}".format(
                                      self.__tablename__,
                                      request.url
                                  ))


metadata = schema.MetaData(naming_convention=NAMING_CONVENTION)
Base = declarative.declarative_base(metadata=metadata, cls=ModelBase)
