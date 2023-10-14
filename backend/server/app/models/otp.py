from datetime import datetime

import sqlalchemy as sa

from app.db.database import Base


class Otp(Base):
    __tablename__ = "otp"
    id = sa.Column(sa.Integer(), primary_key=True)
    email = sa.Column(sa.Integer(), sa.ForeignKey("users.id"))
    otp = sa.Column(sa.Integer())
    modified_on = sa.Column(
        sa.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
