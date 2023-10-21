from flask import Blueprint
from flask_restful import Api

from user.views import GetUserInfo, UserLogin, UserLogout

user_bp = Blueprint('user', __name__)

api = Api(user_bp)

api.add_resource(GetUserInfo, '/api/get_user_info')
api.add_resource(UserLogin,'/api/login')
api.add_resource(UserLogout,'/api/logout')