"""empty message

Revision ID: 4662ba7c0ff3
Revises: c8e97ef7aafb
Create Date: 2022-06-06 22:40:35.227805

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4662ba7c0ff3'
down_revision = 'd5598643eeee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'video_info', type_='foreignkey')
    op.create_foreign_key(None, 'video_info', 'video', ['video_id'], ['video_id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'video_info', type_='foreignkey')
    op.create_foreign_key(None, 'video_info', 'video', ['video_id'], ['video_id'])
    # ### end Alembic commands ###
