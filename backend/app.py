from flask import Flask
import configs
from extension import db


app = Flask(__name__)
# 加载配置文件
app.config.from_object(configs)
# db绑定app
db.init_app(app)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
