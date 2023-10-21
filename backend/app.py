from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager

import configs
from extension import db
from test import test_bp
from user import user_bp

app = Flask(__name__)
# 加载配置文件
app.config.from_object(configs)
# db绑定app
db.init_app(app)
CORS(app, supports_credentials=True)
login_manager = LoginManager(app)

app.register_blueprint(test_bp)
app.register_blueprint(user_bp)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
