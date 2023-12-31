"""Added approved column to user table

Revision ID: 4b8c72dad4e5
Revises: 51f5ccfba190
Create Date: 2022-02-05 15:29:10.283908

"""

# revision identifiers, used by Alembic.
revision = '4b8c72dad4e5'
down_revision = '51f5ccfba190'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('approved', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'approved')
    # ### end Alembic commands ###
