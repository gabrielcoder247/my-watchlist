"""add bio and pic_path

Revision ID: 02f7f4c4000f
Revises: 93bbd3197885
Create Date: 2018-08-13 01:18:35.813911

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02f7f4c4000f'
down_revision = '93bbd3197885'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profile_pic_path')
    op.drop_column('users', 'bio')
    # ### end Alembic commands ###
