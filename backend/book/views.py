import json
import random

from flask_restful import Resource
from flask_restful import request
from sqlalchemy.sql.expression import func
from sqlalchemy import or_
from datetime import datetime



from book.models import Book, Borrowing, Collection, Recommend
from book.serializers import book_serializer, label_serializer, borrowing_serializer

import pandas as pd

from extension import db

class JudgeCollection(Resource):
    def post(self):
        data = request.get_json()
        xh = data['username']
        book_id = data['book_id']
        collection = Collection.query.filter(Collection.xh == xh, Collection.book_id == book_id).first()
        if collection is None:
            return {'status': 0 , 'message': '未收藏'}
        else:
            return {'status': 1 , 'message': '已收藏'}
class PushBorrowingByRecommend(Resource):
    def post(self):
        data = request.get_json()
        # data = b_to_dict(request.data)
        xh = data['username']
        tsbh = data['book_id']
        tsmc = data['book_name']
        user = Borrowing.query.filter(Borrowing.xh == xh).first()
        # 获取今天的日期
        today = datetime.today()
        # 格式化日期
        date = today.strftime("%Y-%m-%d")
        borrowing = Borrowing(xh=user.xh, xb=user.xb, nl=user.nl, syd=user.syd, pycc=user.pycc, sznj=user.sznj, xy=user.xy, tsbh=tsbh, tsmc=tsmc, czrq=date, jyzt='推荐记录')
        db.session.add(borrowing)
        db.session.commit()
        return {'status': 1 , 'message': '已添加到历史记录'}

class DeleteBookInfoByCollection(Resource):
    def post(self):
        data = request.get_json()
        # data = b_to_dict(request.data)
        xh = data['username']
        book_id = data['book_id']
        collection = Collection.query.filter(Collection.xh == xh, Collection.book_id == book_id).first()
        db.session.delete(collection)
        db.session.commit()
        return {'status': 1 , 'message': '取消收藏成功'}

class DeleteBookInfoByRecommend(Resource):
    def post(self):
        data = request.get_json()
        # data = b_to_dict(request.data)
        xh = data['username']
        book_id = data['book_id']
        recommend = Recommend.query.filter(Recommend.xh == xh, Recommend.book_id == book_id).first()
        db.session.delete(recommend)
        db.session.commit()
        return {'status': 1 , 'message': '反馈成功，将为你优化推荐结果'}

class PushBookInfoByRecommend(Resource):
    def post(self):
        data = request.get_json()
        # data = b_to_dict(request.data)
        xh = data['username']
        book_id = data['book_id']
        collection = Collection(xh=xh, book_id=book_id)
        db.session.add(collection)
        db.session.commit()
        return {'status': 1 , 'message': '收藏成功'}

class GetBookInfoByCollection(Resource):
    def post(self):
        data = request.get_json()
        # data = b_to_dict(request.data)
        xh = data['username']
        collection = Collection.query.filter(Collection.xh == xh).all()
        book_list = []
        for collect in collection:
            book = Book.query.filter(Book.book_id == collect.book_id).first()
            if book is not None:
                book_list.append(book)
        return book_serializer(book_list)

class GetBorrowingInfo(Resource):
    def post(self):
        data = request.get_json()
        # data = b_to_dict(request.data)
        xh = data['xh']
        borrowing = Borrowing.query.filter(Borrowing.xh == xh).all()
        return borrowing_serializer(borrowing)

class GetBookInfoByBorrowing(Resource):
    def post(self):
        data = request.get_json()
        # data = b_to_dict(request.data)
        xh = data['username']
        borrowing = Borrowing.query.filter(Borrowing.xh == xh).all()
        print(borrowing)
        book_set = set()
        for borrow in borrowing:
            book = Book.query.filter(Book.TSBH == borrow.tsbh).first()
            if book is not None:
                book_set.add(book)
        book_list = list(book_set)
        print(book_list)
        return book_serializer(book_list)

class GetUserBookInfo(Resource):
    def post(self):
        data = request.get_json()
        xh = data['username']
        user = Recommend.query.filter(Recommend.xh == xh).all()
        if len(user) < 30:
            books = Book.query.order_by(func.random()).limit(30-len(user))
            book_list = []
            for book in books:
                num = random.uniform(5, 10)
                num = round(num, 1)
                book_list.append(Recommend(xh=xh, book_id=book.book_id, fake_rating=num))
            db.session.add_all(book_list)
            db.session.commit()
            print('插入成功')
            recommend = Recommend.query.filter(Recommend.xh == xh).all()
            user_book_list = []
            for user_book in recommend:
                this_book = Book.query.filter(Book.book_id == user_book.book_id).first()
                if this_book is not None:
                    this_book.rating = user_book.fake_rating  # Update the rating in Book
                    db.session.commit()  # Commit the change
                    user_book_list.append(this_book)
        else:
            recommend = Recommend.query.filter(Recommend.xh == xh).all()
            user_book_list = []
            for user_book in recommend:
                this_book = Book.query.filter(Book.book_id == user_book.book_id).first()
                if this_book is not None:
                    user_book_list.append(this_book)


        return book_serializer(user_book_list)

class GetBookInfo(Resource):
    def get(self):
        # book = Book.query.order_by(func.random()).limit(30)
        book = Book.query.order_by(func.random()).limit(30)
        print('开始查询')
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
        book_id = data['book_id']
        book = Book.query.filter(Book.book_id == str(book_id)).all()
        return book_serializer(book)

class GetNewBookInfo(Resource):
    def get(self):
        # 查询Book.pubdata前四位大于等于2023的数据
        book = Book.query.filter(Book.pubyear >= 2023).order_by(func.random()).limit(10)
        return book_serializer(book)

class GetPopBookInfo(Resource):
    def get(self):
        # 查询Book.rating从大到小排序前250位的数据
        book = Book.query.filter(Book.rating != None).order_by(Book.rating.desc()).limit(250)
        return book_serializer(book)

class GetBookLabel(Resource):
    def get(self):
        # 查询Book.label且去重
        label = Book.query.with_entities(Book.label).distinct().all()
        return label_serializer(label)

class GetBookByLabel(Resource):
    def post(self):
        data = request.get_json()
        label = data['label']
        book = Book.query.filter(Book.label == label).order_by(func.random()).limit(3)
        return book_serializer(book)

class GetBookInfoTest(Resource):
    def get(self):
        df = pd.read_csv('../ceshi/book.csv')
        title_list = list(df['tsmc'])
        book_list = []
        i = 0
        for title in title_list:
            book1 = Book.query.filter(Book.book_title == title).first()
        print('开始查询')
        return book_serializer(book1)


def b_to_dict(b_data):
    """将字节数据转化为 dict 类型的数据"""
    json_data = b_data.decode()
    return json.loads(json_data)