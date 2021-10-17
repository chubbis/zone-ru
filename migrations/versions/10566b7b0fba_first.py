"""first

Revision ID: 10566b7b0fba
Revises: 
Create Date: 2021-10-17 15:51:46.650645

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '10566b7b0fba'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('email', table_name='users')
    op.drop_index('id', table_name='users')
    op.drop_table('users')
    op.drop_table('flats')
    op.drop_table('floats')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('floats',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('new_hot_water', mysql.FLOAT(), nullable=True),
    sa.Column('new_cold_water', mysql.FLOAT(), nullable=True),
    sa.Column('new_day_electricity', mysql.FLOAT(), nullable=True),
    sa.Column('new_night_electricity', mysql.FLOAT(), nullable=True),
    sa.Column('flat_number', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('current_hot_water', mysql.FLOAT(), nullable=True),
    sa.Column('current_cold_water', mysql.FLOAT(), nullable=True),
    sa.Column('current_day_electricity', mysql.FLOAT(), nullable=True),
    sa.Column('current_night_electricity', mysql.FLOAT(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('flats',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('new_hot_water', mysql.FLOAT(), nullable=True),
    sa.Column('new_cold_water', mysql.FLOAT(), nullable=True),
    sa.Column('new_day_electricity', mysql.FLOAT(), nullable=True),
    sa.Column('new_night_electricity', mysql.FLOAT(), nullable=True),
    sa.Column('flat_number', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('current_hot_water', mysql.FLOAT(), nullable=True),
    sa.Column('current_cold_water', mysql.FLOAT(), nullable=True),
    sa.Column('current_day_electricity', mysql.FLOAT(), nullable=True),
    sa.Column('current_night_electricity', mysql.FLOAT(), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('created_at', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('users',
    sa.Column('id', mysql.BIGINT(unsigned=True), autoincrement=True, nullable=False),
    sa.Column('user_name', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('password_hash', mysql.VARCHAR(length=120), nullable=True),
    sa.Column('email', mysql.VARCHAR(length=120), nullable=True),
    sa.Column('created_at', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('id', 'users', ['id'], unique=False)
    op.create_index('email', 'users', ['email'], unique=False)
    # ### end Alembic commands ###
