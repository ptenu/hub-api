"""Initial (new)

Revision ID: 772925ac8d0f
Revises: 
Create Date: 2020-10-19 19:36:28.814059

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '772925ac8d0f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('band',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=3), nullable=True),
    sa.Column('name', sa.String(length=15), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('multiplier', sa.Numeric(precision=4, scale=3), nullable=True),
    sa.Column('starts_on', sa.Date(), nullable=True),
    sa.Column('ends_on', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('email',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.String(length=1024), nullable=True),
    sa.Column('from_user_id', sa.String(length=10), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('sent_at', sa.DateTime(), nullable=True),
    sa.Column('hold_until', sa.DateTime(), nullable=True),
    sa.Column('status', sa.String(length=10), nullable=True),
    sa.Column('type', sa.String(length=3), nullable=True),
    sa.Column('to_all_members', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('person',
    sa.Column('id', sa.String(length=10), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=False),
    sa.Column('date_of_birth', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rate',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('starts_on', sa.Date(), nullable=True),
    sa.Column('ends_on', sa.Date(), nullable=True),
    sa.Column('amount', sa.Numeric(precision=5, scale=3), nullable=True),
    sa.Column('multiplier', sa.Numeric(precision=4, scale=3), nullable=True),
    sa.Column('charge', sa.Numeric(precision=5, scale=3), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('email_recipients',
    sa.Column('email_id', sa.Integer(), nullable=False),
    sa.Column('person_id', sa.String(length=10), nullable=False),
    sa.ForeignKeyConstraint(['email_id'], ['email.id'], ),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.PrimaryKeyConstraint('email_id', 'person_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('email_recipients')
    op.drop_table('rate')
    op.drop_table('person')
    op.drop_table('email')
    op.drop_table('band')
    # ### end Alembic commands ###
