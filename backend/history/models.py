from extension import db

class History(db.Model):
    __tablename__ = 'borrowing_analyse'
    xh = db.Column(db.String(255), info='学号')
    xb = db.Column(db.String(255), info='性别')
    nl = db.Column(db.String(255), info='年龄')
    syd = db.Column(db.String(255), info='生源地')
    pycc = db.Column(db.String(255), info='培养层次')
    sznj = db.Column(db.String(255), info='所在年级')
    xy = db.Column(db.String(255), info='学院')
    tsbh = db.Column(db.String(255), info='图书编号')
    tsmc = db.Column(db.String(255), info='图书名称')
    czrq = db.Column(db.String(255), info='借阅日期')
    jyzt = db.Column(db.String(255), info='借阅状态')