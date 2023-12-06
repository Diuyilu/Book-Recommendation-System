from flask import jsonify


def book_serializer(bookinfo):
    book_list = []
    for book in bookinfo:
        booktest_dict = {
            'book_title': book.book_title,
            'content_validity': book.content_validity,
            'author': book.author,
            'author_introduction': book.author_introduction,
            'press': book.press,
            'pubyear': book.pubyear,
            'pages': book.pages,
            'label': book.label,
            'ISBN': book.ISBN,
            'TSBH': book.TSBH,
            'db_id': book.db_id,
            'set_id': book.set_id,
            'book_id': book.book_id,
            'menu': book.menu
        }
        if book.rating:
            booktest_dict['rating'] = book.rating
            booktest_dict['half_rating'] = str(round(float(book.rating)/2,1))
        else:
            booktest_dict['rating'] = 0
            booktest_dict['half_rating'] = 0
        if book.image_address:
            booktest_dict['image_address'] = 'https://images.weserv.nl/?url=' + book.image_address[7:]
        else:
            # 赋值为空
            booktest_dict['image_address'] = book.image_address
        book_list.append(booktest_dict)
    return jsonify({'book_list': book_list, "status": 1})

def label_serializer(bookinfo):
    label_list = []
    for book in bookinfo:
        label_dict = {
            'label': book.label,
        }
        label_list.append(label_dict)
    return jsonify({'label_list': label_list, "status": 1})