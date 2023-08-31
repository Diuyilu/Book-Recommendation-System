from flask import Blueprint
from flask_restful import Api

from test.views import GetBookTestInfo

test_bp = Blueprint('test', __name__)

api = Api(test_bp)

api.add_resource(GetBookTestInfo, '/api/get_book_test_info')