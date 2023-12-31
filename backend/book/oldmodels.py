from extension import db

class Book(db.Model):
    __tablename__ = 'book_data'
    collection_time = db.Column(db.String(255), info='采集时间')
    image_address = db.Column(db.String(255), info='图片地址')
    book_link = db.Column(db.String(255), info='作品链接')
    book_title = db.Column(db.String(255), info='作品名')
    book_subtitle = db.Column(db.String(255), info='副标题')
    author = db.Column(db.String(255), info='作者')
    press = db.Column(db.String(255), info='出版社')
    original_title = db.Column(db.String(255), info='原作名')
    translator = db.Column(db.String(255), info='译者')
    translator_introduction = db.Column(db.String(255), info='译者简介')
    pubdate = db.Column(db.String(255) ,info='出版日')
    pages = db.Column(db.String(255), info='页数')
    price = db.Column(db.String(255), info='定价')
    binding = db.Column(db.String(255), info='装帧')
    ISBN = db.Column(db.String(255), primary_key=True, info='ISBN')
    series = db.Column(db.String(255), info='丛书')
    series_link = db.Column(db.String(255), info='丛书链接')
    rating = db.Column(db.String(255), info='豆瓣评分')
    rating_number = db.Column(db.String(255), info='评价人数')
    content_validity = db.Column(db.String(255), info='内容简介')
    author_introduction = db.Column(db.String(255), info='作者简介')
    menu = db.Column(db.String(255), info='目录')
    label = db.Column(db.String(255), info='标签')
    db_id = db.Column(db.String(255), info='豆瓣ID')