"""migrate pass_secure

Revision ID: 5bb88ea01797
Revises: b18313e722e7
Create Date: 2018-08-10 11:14:12.101603

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5bb88ea01797'
down_revision = 'b18313e722e7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###
