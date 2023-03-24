"""DB-001

Revision ID: 6e567c41d227
Revises: 
Create Date: 2023-03-25 01:09:14.507989

"""
from alembic import op
import sqlalchemy as sa

revision = '6e567c41d227'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('buyer_user',
                    sa.Column('id_buyer_user', sa.Integer(), nullable=False),
                    sa.Column('login', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('phone_number', sa.String(), nullable=False),
                    sa.Column('first_name', sa.String(), nullable=False),
                    sa.Column('second_name', sa.String(), nullable=False),
                    sa.Column('birthday', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id_buyer_user')
                    )
    op.create_table('roles',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('login', sa.String(), nullable=False),
                    sa.Column('permission', sa.JSON(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('salesman_user',
                    sa.Column('id_salesman_user', sa.Integer(), nullable=False),
                    sa.Column('login', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('registered_at', sa.TIMESTAMP(), nullable=True),
                    sa.Column('phone_number', sa.String(), nullable=False),
                    sa.Column('first_name', sa.String(), nullable=False),
                    sa.Column('second_name', sa.String(), nullable=False),
                    sa.Column('birthday', sa.String(), nullable=True),
                    sa.Column('roles', sa.String(), nullable=True),
                    sa.Column('id_shop', sa.Integer(), nullable=True),
                    sa.PrimaryKeyConstraint('id_salesman_user')
                    )


def downgrade() -> None:
    op.drop_table('salesman_user')
    op.drop_table('roles')
    op.drop_table('buyer_user')
