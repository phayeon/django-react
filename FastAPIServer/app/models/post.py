from datetime import datetime

from ..database import Base
from sqlalchemy import Column, String, Integer, DATETIME


class Post(Base):
    __tablename__ = "posts"

    post_id = Column(Integer, primary_key=True)
    title = Column(String(20), nullable=False)
    content = Column(String(20), nullable=False)
    create_at = Column(DATETIME, nullable=False)
    updated_at = Column(DATETIME, nullable=False)

    class Config:
        arbitrary_types_allowed = True
