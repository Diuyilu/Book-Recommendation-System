from extension import db

class Book(db.Model):
    __tablename__ = 'book_merged'
    book_title = db.Column(db.String(255), info='作品名')
    content_validity = db.Column(db.String(255), info='内容简介')
    author = db.Column(db.String(255), info='作者')
    author_introduction = db.Column(db.String(255), info='作者简介')
    press = db.Column(db.String(255), info='出版社')
    pubyear = db.Column(db.String(255) ,info='出版日')
    pages = db.Column(db.String(255), info='页数')
    label = db.Column(db.String(255), info='标签')
    rating = db.Column(db.String(255), info='豆瓣评分')
    ISBN = db.Column(db.String(255), info='ISBN')
    TSBH = db.Column(db.String(255), info='图书编号')
    db_id = db.Column(db.String(255), info='豆瓣ID')
    set_id = db.Column(db.String(255), info='书单ID')
    book_id = db.Column(db.String(255), info='书籍ID',primary_key=True)
    image_address = db.Column(db.String(255), info='图片地址')
    menu = db.Column(db.String(255), info='目录')