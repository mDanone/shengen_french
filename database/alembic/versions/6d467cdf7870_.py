"""empty message

Revision ID: 6d467cdf7870
Revises: 530eb3715c5c
Create Date: 2022-09-03 00:35:08.776173

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d467cdf7870'
down_revision = '530eb3715c5c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cities', sa.Column('value', sa.Integer(), nullable=True))
    op.add_column('sub_categories', sa.Column('value', sa.Integer(), nullable=True))
    op.add_column('task_categories', sa.Column('value', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('task_categories', 'value')
    op.drop_column('sub_categories', 'value')
    op.drop_column('cities', 'value')
    # ### end Alembic commands ###
