from flask_restful import Resource
from flask_restful import request

from book.models import Book
from book.serializers import book_serializer


class GetBookInfo(Resource):
    def get(self):
        book = Book.query.limit(10)
        return book_serializer(book)
