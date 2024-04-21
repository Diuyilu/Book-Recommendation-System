from flask_login import UserMixin
from extension import db
from app import login_manager

class User(db.Model):
    __tablename__ = 'user'
    username = db.Column(db.String(255), info='用户名')
    password = db.Column(db.String(255), info='密码')
    id = db.Column(db.String(255), primary_key=True,info='用户id')


