"""empty message

Revision ID: 530eb3715c5c
Revises: a375cd6320c3
Create Date: 2022-09-02 23:44:58.466084

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '530eb3715c5c'
down_revision = 'a375cd6320c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cities',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('task_categories',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sub_categories',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('task_category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['task_category_id'], ['task_categories.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sub_categories')
    op.drop_table('task_categories')
    op.drop_table('cities')
    # ### end Alembic commands ###
