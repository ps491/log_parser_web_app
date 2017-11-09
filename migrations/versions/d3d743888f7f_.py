"""empty message

Revision ID: d3d743888f7f
Revises: 
Create Date: 2017-11-09 06:41:56.554401

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3d743888f7f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('country',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('ip_address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ip', sa.String(length=32), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('ip')
    )
    op.create_table('entry',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ip_address_id', sa.Integer(), nullable=False),
    sa.Column('raw_log', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['ip_address_id'], ['ip_address.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('entry')
    op.drop_table('ip_address')
    op.drop_table('country')
    # ### end Alembic commands ###