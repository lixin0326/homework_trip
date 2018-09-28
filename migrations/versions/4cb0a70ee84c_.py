"""empty message

Revision ID: 4cb0a70ee84c
Revises: 2d7ac078110c
Create Date: 2018-09-28 15:44:58.235273

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4cb0a70ee84c'
down_revision = '2d7ac078110c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('destination', sa.Column('create_date', sa.DateTime(), nullable=True))
    op.add_column('destination', sa.Column('is_delete', sa.Boolean(), nullable=True))
    op.add_column('destination', sa.Column('price', sa.Numeric(precision=9, scale=2), nullable=False))
    op.create_index(op.f('ix_destination_des_name'), 'destination', ['des_name'], unique=True)
    op.drop_index('des_name', table_name='destination')
    op.add_column('photo', sa.Column('type', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('photo', 'type')
    op.create_index('des_name', 'destination', ['des_name'], unique=True)
    op.drop_index(op.f('ix_destination_des_name'), table_name='destination')
    op.drop_column('destination', 'price')
    op.drop_column('destination', 'is_delete')
    op.drop_column('destination', 'create_date')
    # ### end Alembic commands ###