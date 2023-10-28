from flask_restful import Resource
from flask_restful import request
from sqlalchemy.sql.expression import func

from book.models import Book
from book.serializers import book_serializer


class GetBookInfo(Resource):
    def get(self):
        book = Book.query.order_by(func.random()).limit(10)
        return book_serializer(book)
