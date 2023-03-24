import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, JSON, TIMESTAMP
from datetime import datetime
metadata = MetaData()

roles = Table(
    'roles',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('login', String, nullable=False),
    Column('permission', JSON),
)

salesman = Table(
    'salesman_user',
    metadata,
    Column('id_salesman_user', Integer, primary_key=True),
    Column('login', String, nullable=False),
    Column('password', String, nullable=False),
    Column('email', String, nullable=False),
    Column('registered_at', TIMESTAMP, default=datetime.utcnow),
    Column('phone_number', String, nullable=False),
    Column('first_name', String, nullable=False),
    Column('second_name', String, nullable=False),
    Column('birthday', String),
    Column('roles', String),
    Column('id_shop', Integer),
)

buyer = Table(
    'buyer_user',
    metadata,
    Column('id_buyer_user', Integer, primary_key=True),
    Column('login', String, nullable=False),
    Column('password', String, nullable=False),
    Column('email', String, nullable=False),
    Column('phone_number', String, nullable=False),
    Column('first_name', String, nullable=False),
    Column('second_name', String, nullable=False),
    Column('birthday', String),
)
