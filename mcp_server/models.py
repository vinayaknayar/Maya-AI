from sqlmodel import SQLModel, Field
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from typing import Optional

#####
# SQLModel ORM definitions:
    # User
    # Task
#####

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str
    hashed_password: str


class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int
    title: str
    description: Optional[str] = None

Base = declarative_base()

class JournalEntry(Base):
    __tablename__ = "journal_entries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    content = Column(String, nullable=False)
