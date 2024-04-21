import jwt
from flask import Flask, g, request, session
from flask_cors import CORS
from flask.sessions import SecureCookieSessionInterface

import configs
from book import book_bp
from extension import db,login_manager
from test import test_bp
from user import user_bp
from user.models import User

# def jwt_authentication():
#     authorization_header = request.headers.get('Authorization')
#     if authorization_header:
#         try:
#             token_type, token = authorization_header.split()
#             if token_type.lower() != 'bearer':
#                 raise ValueError('Invalid token type')
#             payload = jwt.decode(token, configs.SECRET_KEY, algorithms=['HS256'])
#             g.user_id = payload['username']
#         except Exception as e:
#             app.logger.error(f"JWT authentication failed: {e}")
#             return False
#     else:
#         return False

app = Flask(__name__)
# 加载配置文件
app.config.from_object(configs)
# db绑定app
db.init_app(app)
CORS(app, supports_credentials=True)


login_manager.init_app(app)  # 初始化应用


app.register_blueprint(test_bp)
app.register_blueprint(user_bp)
app.register_blueprint(book_bp)

# 注册JWT验证中间件
# app.before_request(jwt_authentication)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
