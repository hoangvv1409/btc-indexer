"""add blocks table

Revision ID: fe369024fc73
Revises:
Create Date: 2022-07-03 15:42:56.088951

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe369024fc73'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'blocks',
        sa.Column('hash', sa.String, primary_key=True),
        sa.Column('height', sa.String, nullable=False),
        sa.Column('confirmations', sa.Integer, nullable=False),
        sa.Column('merkle_root', sa.String, nullable=False),

        sa.Column('nonce', sa.Integer, nullable=False),
        sa.Column('difficulty', sa.DECIMAL, nullable=False),

        sa.Column('previous_block_hash', sa.String, nullable=False),
        sa.Column('next_block_hash', sa.String, nullable=False),

        sa.Column('time', sa.BigInteger, nullable=True),
    )

    op.create_index(
        'blocks_height',
        'blocks',
        ['height'],
    )

    op.create_index(
        'blocks_previous_block_hash',
        'blocks',
        ['previous_block_hash'],
    )

    op.create_index(
        'blocks_next_block_hash',
        'blocks',
        ['next_block_hash'],
    )

    op.create_index(
        'blocks_time',
        'blocks',
        ['time'],
        postgresql_ops={'time': 'DESC'},
    )


def downgrade():
    op.drop_table('blocks')
