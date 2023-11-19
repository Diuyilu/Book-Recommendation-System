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
        book = Book.query.filter(or_(Book.book_title.like('%'+ value +'%'),Book.author.like('%'+ value +'%'))).order_by(func.random()).all()
        return book_serializer(book)

class GetBookInfoById(Resource):
    def post(self):
        data = request.get_json()
        # data = b_to_dict(request.data)
        db_id = data['db_id']
        book = Book.query.filter(Book.db_id == str(db_id)).all()
        return book_serializer(book)

class GetNewBookInfo(Resource):
    def get(self):
        # 查询Book.pubdata前四位大于等于2023的数据
        book = Book.query.filter(Book.pubdate >= 2023).order_by(func.random()).limit(10)
        return book_serializer(book)

def b_to_dict(b_data):
    """将字节数据转化为 dict 类型的数据"""
    json_data = b_data.decode()
    return json.loads(json_data)