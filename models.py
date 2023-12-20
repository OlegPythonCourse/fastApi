from typing import Optional

from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))
    age: Mapped[Optional[int]]
    login: Mapped[str] = mapped_column(default= "login", unique=True, index=True)
    password: Mapped[str]

    def __repr__(self) -> str:
        return f'User {self.name} -> #{self.id}'
class Adress(Base):
    __tablename__ = "Adress"
    id: Mapped[int] = mapped_column(primary_key=True)
    Country: Mapped[str]
    Area: Mapped[str]
    Index: Mapped[Optional[str]] = mapped_column(String(5))
    Street: Mapped[Optional[str]] = mapped_column(default='вулиця І.Франка')