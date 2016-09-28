"""empty message

Revision ID: 7066b9c0b5d5
Revises: None
Create Date: 2016-09-17 20:45:16.483021

"""

# revision identifiers, used by Alembic.
revision = '7066b9c0b5d5'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('advance_notice',
    sa.Column('an_Id', sa.Integer(), nullable=False),
    sa.Column('an_Year', sa.DateTime(), nullable=True),
    sa.Column('an_Month', sa.DateTime(), nullable=True),
    sa.Column('an_Day', sa.DateTime(), nullable=True),
    sa.Column('an_Post_Time', sa.DateTime(), nullable=True),
    sa.Column('an_Detail', sa.Text(), nullable=True),
    sa.Column('an_Title', sa.String(length=60), nullable=True),
    sa.Column('an_Outline', sa.Text(), nullable=True),
    sa.Column('an_Img_Url', sa.String(length=20), nullable=True),
    sa.Column('an_Edit', sa.Boolean(), nullable=True),
    sa.Column('an_CommentsNum', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('an_Id')
    )
    op.create_table('charm_association',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('charm_Name', sa.String(length=20), nullable=True),
    sa.Column('charm_Img_Url', sa.String(length=20), nullable=True),
    sa.Column('charm_Intro', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('com_Id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('com_Id')
    )
    op.create_table('news',
    sa.Column('news_Id', sa.Integer(), nullable=False),
    sa.Column('news_Category', sa.String(length=30), nullable=True),
    sa.Column('news_Year', sa.DateTime(), nullable=True),
    sa.Column('news_Month', sa.DateTime(), nullable=True),
    sa.Column('news_Day', sa.DateTime(), nullable=True),
    sa.Column('news_Post_Time', sa.DateTime(), nullable=True),
    sa.Column('news_Detail', sa.Text(), nullable=True),
    sa.Column('news_Title', sa.String(length=60), nullable=True),
    sa.Column('news_Outline', sa.Text(), nullable=True),
    sa.Column('news_Img_Url', sa.String(length=20), nullable=True),
    sa.Column('news_Edit', sa.Boolean(), nullable=True),
    sa.Column('news_CommentsNum', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('news_Id')
    )
    op.create_table('notice',
    sa.Column('notice_id', sa.Integer(), nullable=False),
    sa.Column('notice_Year', sa.DateTime(), nullable=True),
    sa.Column('notice_Month', sa.DateTime(), nullable=True),
    sa.Column('notice_Day', sa.DateTime(), nullable=True),
    sa.Column('notice_Post_Time', sa.DateTime(), nullable=True),
    sa.Column('notice_Detail', sa.Text(), nullable=True),
    sa.Column('notice_Title', sa.String(length=60), nullable=True),
    sa.Column('notice_Outline', sa.Text(), nullable=True),
    sa.Column('notice_Img_Url', sa.String(length=20), nullable=True),
    sa.Column('notice_Edit', sa.Boolean(), nullable=True),
    sa.Column('notice_CommentsNum', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('notice_id')
    )
    op.create_table('star_association',
    sa.Column('star_Id', sa.Integer(), nullable=False),
    sa.Column('star_Role', sa.String(length=20), nullable=True),
    sa.Column('star_Name', sa.String(length=25), nullable=True),
    sa.Column('star_Img_Url', sa.String(length=30), nullable=True),
    sa.Column('star_Intro', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('star_Id')
    )
    op.create_table('association_tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tag', sa.String(length=20), nullable=True),
    sa.Column('tag_Id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['tag_Id'], ['charm_association.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('association_tag')
    op.drop_table('star_association')
    op.drop_table('notice')
    op.drop_table('news')
    op.drop_table('comments')
    op.drop_table('charm_association')
    op.drop_table('advance_notice')
    ### end Alembic commands ###
