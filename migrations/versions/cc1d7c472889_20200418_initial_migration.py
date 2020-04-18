"""20200418 initial migration

Revision ID: cc1d7c472889
Revises: 
Create Date: 2020-04-19 00:22:46.463232

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc1d7c472889'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('card',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('word', sa.String(length=50), nullable=True),
    sa.Column('selected', sa.Boolean(), nullable=True),
    sa.Column('team', sa.String(length=50), nullable=True),
    sa.Column('game_id', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_card_game_id'), 'card', ['game_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_card_game_id'), table_name='card')
    op.drop_table('card')
    # ### end Alembic commands ###