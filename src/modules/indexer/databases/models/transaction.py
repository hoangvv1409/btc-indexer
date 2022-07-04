from sqlalchemy import BigInteger, Integer, Column, JSON, String
from src.databases.schema_base import DeclarativeBase, Base


class TransactionSchema(DeclarativeBase, Base):
    __tablename__ = 'transactions'

    txid = Column(String, primary_key=True)

    hash = Column(String, nullable=False)
    block_hash = Column(String, nullable=False)
    time = Column(BigInteger, nullable=False)
    confirmations = Column(Integer, nullable=False)
    hex = Column(String, nullable=False)

    vin = Column(JSON, nullable=False)
    vout = Column(JSON, nullable=False)
