from sqlalchemy import Integer, Column, JSON
from src.databases.schema_base import DeclarativeBase, Base, DateTimestamp


class BlockSchema(DeclarativeBase, Base, DateTimestamp):
    __tablename__ = 'blocks'

    id = Column(Integer, primary_key=True)

    payload = Column(JSON, nullable=True)
