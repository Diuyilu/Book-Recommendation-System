from flask_restful import Resource
from flask_restful import request
from flask import session
from user.models import User
from user.serializers import user_serializer
from extension import db


class GetUserInfo(Resource):
    def get(self):
        userinfo = User.query.all()
        return user_serializer(userinfo)

class UserLogin(Resource):
    def post(self):
        params = request.get_json()
        username = params['username']
        password = params['password']



