from sqlalchemy import Integer, Column, JSON
from src.databases.schema_base import DeclarativeBase, Base, DateTimestamp


class TransactionSchema(DeclarativeBase, Base, DateTimestamp):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)

    payload = Column(JSON, nullable=True)
