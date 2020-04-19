"""20200419 added games

Revision ID: 32a9b7b14f24
Revises: 5e9e7211948c
Create Date: 2020-04-19 16:21:36.764277

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32a9b7b14f24'
down_revision = '5e9e7211948c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('card', schema=None) as batch_op:
        batch_op.create_foreign_key(batch_op.f('fk_card_game_id_game'), 'game', ['game_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('card', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_card_game_id_game'), type_='foreignkey')

    # ### end Alembic commands ###
