from flask_login import UserMixin
from werkzeug.security import check_password_hash,generate_password_hash
from extension import db, login_manager

USERS = [
    {
        "id":1,
        "username":"admin",
        "password":generate_password_hash('123456')
    },
    {
        "id":2,
        "username":"李四",
        "password":generate_password_hash('123456')
    },
]


def query2dict(model_list):
    if isinstance(model_list, list):  # 如果传入的参数是一个list类型的，说明是使用的all()的方式查询的
        if isinstance(model_list[0], db.Model):  # 这种方式是获得的整个对象  相当于 select * from table
            lst = []
            for model in model_list:
                dic = {}
                for col in model.__table__.columns:
                    dic[col.name] = getattr(model, col.name)
                lst.append(dic)
            return lst
        else:  # 这种方式获得了数据库中的个别字段  相当于select id,name from table
            lst = []
            for result in model_list:  # 当以这种方式返回的时候，result中会有一个keys()的属性
                lst.append([dict(zip(result.keys, r)) for r in result])
            return lst
    else:  # 不是list,说明是用的get() 或者 first()查询的，得到的结果是一个对象
        if isinstance(model_list, db.Model):  # 这种方式是获得的整个对象  相当于 select * from table limit=1
            dic = {}
            for col in model_list.__table__.columns:
                dic[col.name] = getattr(model_list, col.name)
            return dic
        else:  # 这种方式获得了数据库中的个别字段  相当于select id,name from table limit = 1
            return dict(zip(model_list.keys(), model_list))


class Userinfo(UserMixin):
    def __init__(self, user):
        self.username = user.get("username")
        self.password_hash = user.get("password")
        self.id = user.get("id")

    @staticmethod
    def queryUser(username):
        for user in USERS:
            if (user.get('name') == username):
                return Userinfo(user)
        return None

    def verifyPassword(self, password):
        if self.password_hash is None:
            return False
        # return check_password_hash(self.password_hash, password)
        elif self.password_hash == password:
            return True

    def get_id(self):
        return self.id

    def get(user_id):
        if not user_id:
            return None
        for user in USERS:
            if str(user.get('id')) == str(user_id):
                return Userinfo(user)
        print('None')
        return None


