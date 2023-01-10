from ..database import Base
from sqlalchemy import Column, String


class User(Base):
    __tablename__ = "users"

    user_id = Column(String(20), primary_key=True)
    email = Column(String(20), nullable=False)
    password = Column(String(20), nullable=False)
    user_name = Column(String(20))
    token = Column(String(20))

    class Config:
        arbitrary_types_allowed = True
