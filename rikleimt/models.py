# encoding=utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

user_role = db.Table(
    'usersToRoles',
    db.column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.column('role_id', db.Integer, db.ForeignKey('role.id'))
)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column('id', db.Integer, primary_key=True)
    name_id = db.Column('nameId', db.String, unique=True)  # TODO: What is the role of this value? [Arlena]
    first_name = db.Column('firstName', db.String)
    last_name = db.Column('lastName', db.String)
    email = db.Column('email', db.String, unique=True)

    roles = db.relationship('Role', secondary=user_role, back_populates='users')


class Role(db.model):
    __tablename__ = 'role'
    id = db.Column('id', db.Integer, primary_key=True)
    slug = db.Column('slug', db.String)
    permissions = db.Column('permissions', db.Text)

    users = db.relationship('User', secondary=user_role, back_populates='roles')

