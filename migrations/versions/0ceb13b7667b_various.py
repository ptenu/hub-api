"""Various

Revision ID: 0ceb13b7667b
Revises: 58cedb07360b
Create Date: 2020-11-10 02:37:33.837748

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ceb13b7667b'
down_revision = '58cedb07360b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('verify_token',
    sa.Column('token', sa.String(length=300), nullable=False),
    sa.PrimaryKeyConstraint('token')
    )
    op.add_column('address', sa.Column('marketing', sa.Boolean(), nullable=False))
    op.add_column('email', sa.Column('from_person_id', sa.String(length=10), nullable=True))
    op.add_column('email', sa.Column('link', sa.String(), nullable=True))
    op.add_column('email', sa.Column('link_text', sa.String(), nullable=True))
    op.add_column('email', sa.Column('preview_text', sa.Text(), nullable=True))
    op.add_column('email', sa.Column('title', sa.String(), nullable=True))
    op.create_foreign_key(None, 'email', 'person', ['from_person_id'], ['id'])
    op.drop_column('email', 'from_user_id')
    op.add_column('payment', sa.Column('payment_intent_id', sa.String(length=100), nullable=True))
    op.create_unique_constraint(None, 'payment', ['payment_intent_id'])
    op.add_column('person', sa.Column('constituency_id', sa.String(length=10), nullable=True))
    op.add_column('person', sa.Column('district_id', sa.String(length=10), nullable=True))
    op.add_column('person', sa.Column('landlord', sa.Boolean(), nullable=True))
    op.add_column('person', sa.Column('own_house', sa.Boolean(), nullable=True))
    op.add_column('person', sa.Column('password', sa.String(length=300), nullable=True))
    op.add_column('person', sa.Column('pays_rent', sa.Boolean(), nullable=True))
    op.add_column('person', sa.Column('restricted_job', sa.Boolean(), nullable=True))
    op.add_column('person', sa.Column('ward_id', sa.String(length=10), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('person', 'ward_id')
    op.drop_column('person', 'restricted_job')
    op.drop_column('person', 'pays_rent')
    op.drop_column('person', 'password')
    op.drop_column('person', 'own_house')
    op.drop_column('person', 'landlord')
    op.drop_column('person', 'district_id')
    op.drop_column('person', 'constituency_id')
    op.drop_constraint(None, 'payment', type_='unique')
    op.drop_column('payment', 'payment_intent_id')
    op.add_column('email', sa.Column('from_user_id', sa.VARCHAR(length=10), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'email', type_='foreignkey')
    op.drop_column('email', 'title')
    op.drop_column('email', 'preview_text')
    op.drop_column('email', 'link_text')
    op.drop_column('email', 'link')
    op.drop_column('email', 'from_person_id')
    op.drop_column('address', 'marketing')
    op.drop_table('verify_token')
    # ### end Alembic commands ###