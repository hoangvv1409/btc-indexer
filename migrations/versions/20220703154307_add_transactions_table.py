"""add transactions table

Revision ID: 53800872213f
Revises: fe369024fc73
Create Date: 2022-07-03 15:43:07.471741

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53800872213f'
down_revision = 'fe369024fc73'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'transactions',
        sa.Column('txid', sa.String, primary_key=True),

        sa.Column('hash', sa.String, nullable=False),
        sa.Column('block_hash', sa.String, nullable=False),
        sa.Column('confirmations', sa.Integer, nullable=False),
        sa.Column('hex', sa.String, nullable=False),

        sa.Column('vin', sa.JSON, nullable=False),
        sa.Column('vout', sa.JSON, nullable=False),

        sa.Column('time', sa.BigInteger, nullable=True),
    )

    op.create_index(
        'transactions_block_hash',
        'transactions',
        ['block_hash'],
    )

    op.create_index(
        'transactions_time',
        'transactions',
        ['time'],
        postgresql_ops={'time': 'DESC'},
    )


def downgrade():
    op.drop_table('transactions')
