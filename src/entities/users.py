from sqlalchemy import Column, String, Integer
from src.config import Base 

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self) -> str:
        return f"users [name={self.name}]"

