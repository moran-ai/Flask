"""sencod

Revision ID: 919869a05c61
Revises: 5cf23569b12b
Create Date: 2021-06-23 17:09:59.642439

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '919869a05c61'
down_revision = '5cf23569b12b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('t_user_1', sa.Column('address', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('t_user_1', 'address')
    # ### end Alembic commands ###