"""add photos relationship

Revision ID: 19625ca387b3
Revises: 3f6b7f6149dd
Create Date: 2018-08-16 13:30:39.149144

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19625ca387b3'
down_revision = '3f6b7f6149dd'
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
