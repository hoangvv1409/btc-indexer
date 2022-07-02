from sqlalchemy import Integer, Column, JSON
from src.databases.schema_base import DeclarativeBase, Base, DateTimestamp


class SampleSchema(DeclarativeBase, Base, DateTimestamp):
    __tablename__ = 'samples'

    id = Column(Integer, primary_key=True)

    payload = Column(JSON, nullable=True)
