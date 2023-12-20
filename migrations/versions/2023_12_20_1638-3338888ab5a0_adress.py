"""Adress

Revision ID: 3338888ab5a0
Revises: 3ee95d911e16
Create Date: 2023-12-20 16:38:22.174415

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3338888ab5a0'
down_revision: Union[str, None] = '3ee95d911e16'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Adress',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Country', sa.String(), nullable=False),
    sa.Column('Area', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Adress')
    # ### end Alembic commands ###
