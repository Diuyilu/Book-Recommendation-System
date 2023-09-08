from extension import db

class User(db.Model):
    __tablename__ = 'user'
    username = db.Column(db.String(255), primary_key=True,info='用户名')
    password = db.Column(db.String(255), info='密码')