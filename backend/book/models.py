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
    fake_rating = db.Column(db.String(255), info='假评分')

class Borrowing(db.Model):
    __tablename__ = 'borrowing_analyse'
    xh = db.Column(db.String(255), info='学号', primary_key=True)
    xb = db.Column(db.String(255), info='性别', primary_key=True)
    nl = db.Column(db.String(255), info='年龄', primary_key=True)
    syd = db.Column(db.String(255), info='生源地', primary_key=True)
    pycc = db.Column(db.String(255), info='培养层次', primary_key=True)
    sznj = db.Column(db.String(255), info='所在年级', primary_key=True)
    xy = db.Column(db.String(255), info='学院', primary_key=True)
    tsbh = db.Column(db.String(255), info='图书编号', primary_key=True)
    tsmc = db.Column(db.String(255), info='图书名称', primary_key=True)
    czrq = db.Column(db.String(255), info='借书日期', primary_key=True)
    jyzt = db.Column(db.String(255), info='借阅状态', primary_key=True)

class Collection(db.Model):
    __tablename__ = 'user_collection'
    xh = db.Column(db.String(255), info='学号', primary_key=True)
    book_id = db.Column(db.String(255), info='书籍ID', primary_key=True)

class Recommend(db.Model):
    __tablename__ = 'user_recommend'
    xh = db.Column(db.String(255), info='学号', primary_key=True)
    book_id = db.Column(db.String(255), info='书籍ID', primary_key=True)
    fake_rating = db.Column(db.String(255), info='推荐评分', primary_key=True)

