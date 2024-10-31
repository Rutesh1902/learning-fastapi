from database import Base
from sqlalchemy import Column, Integer, String


class Blog(Base):
    id = Column(Integer, primary_key=True, Index=True)
    title = Column(String)
    body = Column(String)
