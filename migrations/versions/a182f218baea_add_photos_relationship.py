"""add photos relationship

Revision ID: a182f218baea
Revises: 21b38424d21f
Create Date: 2018-08-16 12:28:17.348523

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a182f218baea'
down_revision = '21b38424d21f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reviews', sa.Column('image_path', sa.String(), nullable=True))
    op.drop_column('reviews', 'movie_path')
    op.add_column('users', sa.Column('password_hash', sa.String(length=255), nullable=True))
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('users', 'password_hash')
    op.add_column('reviews', sa.Column('movie_path', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('reviews', 'image_path')
    # ### end Alembic commands ###
