from flask import Flask
from flask-cors import
import configs
from extension import db
from test import test_bp
from user import user_bp

app = Flask(__name__)
# 加载配置文件
app.config.from_object(configs)
# db绑定app
db.init_app(app)

app.register_blueprint(test_bp)
app.register_blueprint(user_bp)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
