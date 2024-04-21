from flask_restful import Resource
from flask_restful import request
from flask import session, jsonify, g
from user.models import User
from user.serializers import user_serializer, now_user_serializer
from extension import db, login_manager
from user.jwt_token import genToken,verfiyToken
from flask_login import LoginManager,login_user,logout_user,login_required,current_user
from user.userinfo import Userinfo
import json
from user.userinfo import query2dict


@login_manager.user_loader
def load_user(user_id):
    print('load_user!!!!!')
    print(user_id)
    user = User.query.filter(User.id == user_id).first()
    user = query2dict(user)
    user = Userinfo(user)
    return user

class GetUserInfo(Resource):
    def get(self):
        with open('user_dict.json', 'r') as f:
            user_dict = json.load(f)
        username = user_dict['username']
        print(username)
        return now_user_serializer(username)


class UserLogin(Resource):
    def post(self):
        print(request.form)
        username = request.form['username']
        password = request.form['password']
        print(username)
        user = User.query.filter(User.username == username).first()
        user_dict = query2dict(user)
        user = Userinfo(user_dict)
        print('user')
        print(user.id)
        # user = Userinfo.queryUser(username)
        if (user is not None) and (user.verifyPassword(password)):
        # if (user is not None) and (user.password == password):
            login_user(user)
            token = genToken({'username': username, 'password': password})
            with open('user_dict.json', 'w') as f:
                json.dump(user_dict, f)
            returnData = {"succeed": True, 'code': 200, 'message': '成功', 'data': {'token': token}}

            print(returnData)
            # return json.dumps(returnData), 200
            return jsonify(returnData) # 200
        else:
            # returnData = {'code': 1, 'message': 'success', 'data': 'username or password is not correct'}
            returnData = {'code': 2001, 'message': '用户名或密码错误', "succeed": False}
            # return json.dumps(returnData), 200
            print(returnData)
            return jsonify(returnData) # 200
class UserLogout(Resource):
    def get(self):
        username = current_user.username
        logout_user()
        now_user = ''
        returndata = {'code': 0, 'msg': 'success', 'data': ' Bye ' + username }
        return json.dumps(returndata),200


def b_to_dict(b_data):
    """将字节数据转化为 dict 类型的数据"""
    json_data = b_data.decode()
    return json.loads(json_data)

