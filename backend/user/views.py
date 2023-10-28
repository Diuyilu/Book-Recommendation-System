from flask_restful import Resource
from flask_restful import request
from flask import session, jsonify
from user.models import User
from user.serializers import user_serializer
from extension import db
from user.jwt_token import genToken,verfiyToken
from flask_login import LoginManager,login_user,logout_user,login_required,current_user
from user.userinfo import Userinfo
import json

class GetUserInfo(Resource):
    def get(self):
        userinfo = User.query.all()
        return user_serializer(userinfo)

class UserLogin(Resource):
    def post(self):
        print(request.form)
        username = request.form['username']
        password = request.form['password']
        user = Userinfo.queryUser(username)
        if (user is not None) and (user.verifyPassword(password)):
            login_user(user)
            token = genToken({'username': username, 'password': password})
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
        returndata = {'code': 0, 'msg': 'success', 'data': ' Bye ' + username }
        return json.dumps(returndata),200


def b_to_dict(b_data):
    """将字节数据转化为 dict 类型的数据"""
    json_data = b_data.decode()
    return json.loads(json_data)

