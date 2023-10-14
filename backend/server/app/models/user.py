from datetime import datetime

import sqlalchemy as sa

from app.db.database import Base


class User(Base):
    __tablename__ = "users"
    id = sa.Column(sa.Integer(), primary_key=True)
    name = sa.Column(sa.String(255))
    email = sa.Column(sa.String(255), unique=True)
    phone_number = sa.Column(sa.Integer(), unique=True)
    password = sa.Column(sa.String(255))
    created_on = sa.Column(sa.DateTime, default=datetime.utcnow)
    modified_on = sa.Column(
        sa.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    is_active = sa.Column(sa.Boolean(), default=False)
    is_admin = sa.Column(sa.Boolean, default=False)
