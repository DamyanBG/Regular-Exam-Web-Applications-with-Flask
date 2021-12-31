"""Add products table

Revision ID: 84b1773e9078
Revises: 6d5520fc3d08
Create Date: 2021-12-31 11:44:01.381961

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84b1773e9078'
down_revision = '6d5520fc3d08'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('pk', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('create_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('photo_url', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('pk')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    # ### end Alembic commands ###