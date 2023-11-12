from flask import Blueprint
from flask_restful import Api

from book.views import GetBookInfo, SearchBookInfo, GetBookInfoById

book_bp = Blueprint('book', __name__)

api = Api(book_bp)

api.add_resource(GetBookInfo, '/api/get_book_info')
api.add_resource(SearchBookInfo, '/api/search_book_info')
api.add_resource(GetBookInfoById, '/api/get_book_info_by_id')