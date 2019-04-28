"""11.1

Revision ID: 4331abb202c0
Revises: cce53f228f65
Create Date: 2019-04-28 12:57:54.435828

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4331abb202c0'
down_revision = 'cce53f228f65'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'test')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('test', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    # ### end Alembic commands ###