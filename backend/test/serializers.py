from flask import jsonify


def booktest_serializer(booktestinfo):
    booktest_dict = {}
    booktest_list = []
    for book in booktestinfo:
        booktest_dict = {
            'collection_time': book.collection_time,
            'image_address': book.image_address,
            'book_link': book.book_link,
            'book_title': book.book_title,
            'book_subtitle': book.book_subtitle,
            'author': book.author,
            'press': book.press,
            'original_title': book.original_title,
            'translator': book.translator,
            'translator_introduction': book.translator_introduction,
            'publication_year': book.publication_year,
            'pages': book.pages,
            'price': book.price,
            'binding': book.binding,
            'ISBN': book.ISBN,
            'series': book.series,
            'series_link': book.series_link,
            'rating': book.rating,
            'rating_number': book.rating_number,
            'content_validity': book.content_validity,
            'author_introduction': book.author_introduction,
            'menu': book.menu,
            'label': book.label,
            'db_id': book.db_id
        }
        booktest_list.append(booktest_dict)
    return jsonify({'booktest_list': booktest_list, "status": 1})