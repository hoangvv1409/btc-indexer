import os
import concurrent.futures

from sqlalchemy.orm import sessionmaker, scoped_session
from src.databases.connection import db_engine, bind_session
from src.modules.indexer.databases.repositories import (
    BlockRepository, TransactionRepository)
from src.modules.indexer.use_cases import Indexing
from src.external_services.bitcoind import Bitcoind


engine = db_engine(os.getenv('DATABASE_URI'))


btc_client = Bitcoind(
    username=os.getenv('RPC_USERNAME'),
    password=os.getenv('RPC_PASSWORD'),
)


def block_handler(height):
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = bind_session(engine, scoped_session(SessionLocal))()

    block_repo = BlockRepository(session)
    txn_repo = TransactionRepository(session)
    indexing = Indexing(
        client=btc_client,
        block_repository=block_repo,
        transaction_repository=txn_repo,
    )

    try:
        indexing.execute(height)
        session.commit()
    except Exception as e:
        session.rollback()

    session.close()
    print(height)


with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    for height in range(1, 743397):
        executor.submit(block_handler, height)
