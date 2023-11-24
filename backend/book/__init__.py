from flask import Blueprint
from flask_restful import Api

from book.views import GetBookInfo, SearchBookInfo, GetBookInfoById, GetNewBookInfo, GetPopBookInfo, GetBookLabel, \
    GetBookByLabel

book_bp = Blueprint('book', __name__)

api = Api(book_bp)

api.add_resource(GetBookInfo, '/api/get_book_info')
api.add_resource(SearchBookInfo, '/api/search_book_info')
api.add_resource(GetBookInfoById, '/api/get_book_info_by_id')
api.add_resource(GetNewBookInfo, '/api/get_new_book_info')
api.add_resource(GetPopBookInfo, '/api/get_pop_book_info')
api.add_resource(GetBookLabel, '/api/get_book_label')
api.add_resource(GetBookByLabel, '/api/get_book_by_label')