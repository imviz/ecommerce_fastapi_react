import sqlalchemy as sa
from .base import Base
import datetime


class Otp(Base):
    __tabledname__ = "otp"
    id = sa.Column(sa.Integer(), primary_key=True)
    email = sa.Column(sa.Integer(), sa.ForeignKey("users.id"))
    otp = sa.Column(sa.Integer(6))
    modified_on = sa.Column(
        sa.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
