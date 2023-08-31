from flask_restful import Resource
from flask_restful import request

from test.models import BookTest
from test.serializers import booktest_serializer


class GetBookTestInfo(Resource):
    def get(self):
        booktest = BookTest.query.all()
        return booktest_serializer(booktest)
