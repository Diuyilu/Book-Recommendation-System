from flask import Blueprint
from flask_restful import Api

from book.views import GetBookInfo

book_bp = Blueprint('book', __name__)

api = Api(book_bp)

api.add_resource(GetBookInfo, '/api/get_book_info')