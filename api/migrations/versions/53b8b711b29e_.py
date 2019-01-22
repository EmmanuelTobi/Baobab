"""empty message

Revision ID: 53b8b711b29e
Revises: 351c26992f23
Create Date: 2019-01-22 18:39:30.903190

"""

# revision identifiers, used by Alembic.
revision = '53b8b711b29e'
down_revision = '351c26992f23'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('country',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('group', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_disability',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_ethnicity',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_gender',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_title',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column(u'app_user', sa.Column('affiliation', sa.String(length=255), nullable=False))
    op.add_column(u'app_user', sa.Column('deleted_datetime_utc', sa.DateTime(), nullable=True))
    op.add_column(u'app_user', sa.Column('department', sa.String(length=255), nullable=False))
    op.add_column(u'app_user', sa.Column('firstname', sa.String(length=100), nullable=False))
    op.add_column(u'app_user', sa.Column('is_deleted', sa.Boolean(), nullable=False))
    op.add_column(u'app_user', sa.Column('lastname', sa.String(length=100), nullable=False))
    op.add_column(u'app_user', sa.Column('nationality_country_id', sa.Integer(), nullable=False))
    op.add_column(u'app_user', sa.Column('residence_country_id', sa.Integer(), nullable=False))
    op.add_column(u'app_user', sa.Column('user_category_id', sa.Integer(), nullable=False))
    op.add_column(u'app_user', sa.Column('user_disability_id', sa.Integer(), nullable=False))
    op.add_column(u'app_user', sa.Column('user_ethnicity_id', sa.Integer(), nullable=False))
    op.add_column(u'app_user', sa.Column('user_gender_id', sa.Integer(), nullable=False))
    op.add_column(u'app_user', sa.Column('user_title_id', sa.Integer(), nullable=False))
    op.alter_column(u'app_user', 'active',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column(u'app_user', 'email',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column(u'app_user', 'is_admin',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column(u'app_user', 'password',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.create_foreign_key(u'app_user_residence_country_id', 'app_user', 'country', ['residence_country_id'], ['id'])
    op.create_foreign_key(u'app_user_user_title_id', 'app_user', 'user_title', ['user_title_id'], ['id'])
    op.create_foreign_key(u'app_user_nationality_country_id', 'app_user', 'country', ['nationality_country_id'], ['id'])
    op.create_foreign_key(u'app_user_user_gender_id', 'app_user', 'user_gender', ['user_gender_id'], ['id'])
    op.create_foreign_key(u'app_user_user_category_id', 'app_user', 'user_category', ['user_category_id'], ['id'])
    op.create_foreign_key(u'app_user_user_ethnicity_id', 'app_user', 'user_ethnicity', ['user_ethnicity_id'], ['id'])
    op.create_foreign_key(u'app_user_user_disability_id', 'app_user', 'user_disability', ['user_disability_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(u'app_user_residence_country_id', 'app_user', type_='foreignkey')
    op.drop_constraint(u'app_user_user_title_id', 'app_user', type_='foreignkey')
    op.drop_constraint(u'app_user_nationality_country_id', 'app_user', type_='foreignkey')
    op.drop_constraint(u'app_user_user_gender_id', 'app_user', type_='foreignkey')
    op.drop_constraint(u'app_user_user_category_id', 'app_user', type_='foreignkey')
    op.drop_constraint(u'app_user_user_ethnicity_id', 'app_user', type_='foreignkey')
    op.drop_constraint(u'app_user_user_disability_id', 'app_user', type_='foreignkey')
    op.alter_column(u'app_user', 'password',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column(u'app_user', 'is_admin',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column(u'app_user', 'email',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column(u'app_user', 'active',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.drop_column(u'app_user', 'user_title_id')
    op.drop_column(u'app_user', 'user_gender_id')
    op.drop_column(u'app_user', 'user_ethnicity_id')
    op.drop_column(u'app_user', 'user_disability_id')
    op.drop_column(u'app_user', 'user_category_id')
    op.drop_column(u'app_user', 'residence_country_id')
    op.drop_column(u'app_user', 'nationality_country_id')
    op.drop_column(u'app_user', 'lastname')
    op.drop_column(u'app_user', 'is_deleted')
    op.drop_column(u'app_user', 'firstname')
    op.drop_column(u'app_user', 'department')
    op.drop_column(u'app_user', 'deleted_datetime_utc')
    op.drop_column(u'app_user', 'affiliation')
    op.drop_table('user_title')
    op.drop_table('user_gender')
    op.drop_table('user_ethnicity')
    op.drop_table('user_disability')
    op.drop_table('user_category')
    op.drop_table('country')
    # ### end Alembic commands ###
