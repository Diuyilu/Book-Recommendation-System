from flask import jsonify


def book_serializer(bookinfo):
    book_list = []
    for book in bookinfo:
        if book.rating:
            booktest_dict = {
                'collection_time': book.collection_time,
                'image_address': 'https://images.weserv.nl/?url=' + book.image_address[7:],
                'book_link': book.book_link,
                'book_title': book.book_title,
                'book_subtitle': book.book_subtitle,
                'author': book.author,
                'press': book.press,
                'original_title': book.original_title,
                'translator': book.translator,
                'translator_introduction': book.translator_introduction,
                'pubdate': book.pubdate,
                'pages': book.pages,
                'price': book.price,
                'binding': book.binding,
                'ISBN': book.ISBN,
                'series': book.series,
                'series_link': book.series_link,
                'rating': book.rating,
                'half_rating': str(round(float(book.rating)/2,1)),
                'rating_number': book.rating_number,
                'content_validity': book.content_validity,
                'author_introduction': book.author_introduction,
                'menu': book.menu,
                'label': book.label,
                'db_id': book.db_id
            }
            book_list.append(booktest_dict)
        else:
            booktest_dict = {
                'collection_time': book.collection_time,
                'image_address': 'https://images.weserv.nl/?url=' + book.image_address[7:],
                'book_link': book.book_link,
                'book_title': book.book_title,
                'book_subtitle': book.book_subtitle,
                'author': book.author,
                'press': book.press,
                'original_title': book.original_title,
                'translator': book.translator,
                'translator_introduction': book.translator_introduction,
                'pubdate': book.pubdate,
                'pages': book.pages,
                'price': book.price,
                'binding': book.binding,
                'ISBN': book.ISBN,
                'series': book.series,
                'series_link': book.series_link,
                'rating': 0,
                'half_rating': 0,
                'rating_number': book.rating_number,
                'content_validity': book.content_validity,
                'author_introduction': book.author_introduction,
                'menu': book.menu,
                'label': book.label,
                'db_id': book.db_id
            }
            book_list.append(booktest_dict)
    return jsonify({'book_list': book_list, "status": 1})