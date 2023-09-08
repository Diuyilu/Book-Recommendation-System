from flask_restful import Resource
from flask_restful import request

from user.models import User
from user.serializers import user_serializer


class GetUserInfo(Resource):
    def get(self):
        userinfo = User.query.all()
        return user_serializer(userinfo)
