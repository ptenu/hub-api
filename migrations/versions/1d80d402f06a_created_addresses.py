"""Created addresses

Revision ID: 1d80d402f06a
Revises: 213244d95cd2
Create Date: 2020-10-22 17:56:21.841548

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d80d402f06a'
down_revision = '213244d95cd2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('address',
    sa.Column('person_id', sa.String(length=10), nullable=False),
    sa.Column('type', sa.String(length=10), nullable=False),
    sa.Column('usage', sa.String(length=10), nullable=False),
    sa.Column('verified', sa.Boolean(), nullable=False),
    sa.Column('line_1', sa.String(length=1024), nullable=True),
    sa.Column('district', sa.String(length=1024), nullable=True),
    sa.Column('city', sa.String(length=1024), nullable=True),
    sa.Column('post_code', sa.String(length=10), nullable=True),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.PrimaryKeyConstraint('person_id', 'type')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('address')
    # ### end Alembic commands ###
