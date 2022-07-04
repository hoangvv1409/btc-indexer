from sqlalchemy import BigInteger, Integer, Column, String, DECIMAL
from src.databases.schema_base import DeclarativeBase, Base


class BlockSchema(DeclarativeBase, Base):
    __tablename__ = 'blocks'

    hash = Column(String, primary_key=True)
    height = Column(Integer, nullable=False)
    confirmations = Column(Integer, nullable=False)
    merkle_root = Column(String, nullable=False)
    time = Column(BigInteger, nullable=False)

    nonce = Column(BigInteger, nullable=False)
    difficulty = Column(DECIMAL, nullable=False)

    previous_block_hash = Column(String, nullable=False)
    next_block_hash = Column(String, nullable=False)
