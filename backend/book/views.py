import json

from flask_restful import Resource
from flask_restful import request
from sqlalchemy.sql.expression import func
from sqlalchemy import or_

from book.models import Book
from book.serializers import book_serializer


class GetBookInfo(Resource):
    def get(self):
        book = Book.query.order_by(func.random()).limit(10)
        return book_serializer(book)

class SearchBookInfo(Resource):
    def post(self):
        data = b_to_dict(request.data)
        value = data['value']
        print(value)
        book = Book.query.filter(or_(Book.book_title == value,Book.author == value)).order_by(func.random()).limit(10)
        return book_serializer(book)

def b_to_dict(b_data):
    """将字节数据转化为 dict 类型的数据"""
    json_data = b_data.decode()
    return json.loads(json_data)