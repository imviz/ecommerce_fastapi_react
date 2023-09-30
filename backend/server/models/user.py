import sqlalchemy as sa
from .base import Base
import datetime


class User(Base):
    __tablename__ = "users"
    id = sa.Column(sa.Integer(), primary_key=True)
    email = sa.Column(sa.String(255), unique=True)
    phone_number = sa.Column(sa.Integer(10), unique=True)
    password = sa.Column(sa.String(255))
    email = sa.Column(sa.String(255))
    created_on = sa.Column(sa.DateTime, default=datetime.utcnow)
    modified_on = sa.Column(
        sa.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    is_active = sa.Column(sa.Boolean(), default=True)
    is_admin = sa.Column(sa.Boolean, default=False)
