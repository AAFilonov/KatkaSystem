"""sync

Revision ID: e402cf94f146
Revises: cdf9e48d3272
Create Date: 2021-02-23 16:14:54.877690

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e402cf94f146'
down_revision = 'cdf9e48d3272'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('character', sa.Column('bio', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('character', 'bio')
    # ### end Alembic commands ###
