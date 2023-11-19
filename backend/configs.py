
from urllib import parse
# 打开txt文件并读取内容
with open('key.txt', 'r') as file:
    content = file.read()

# 解析内容并赋值给相关变量
lines = content.split('\n')
variables = {}
for line in lines:
    if '=' in line:
        key, value = line.split('=')
        key = key.strip()
        value = value.strip().strip("'")
        variables[key] = value

# 根据变量名进行赋值
HOST = variables.get('HOST')
PORT = variables.get('PORT')
DATABASE = variables.get('DATABASE')
USERNAME = variables.get('USERNAME')
PASSWORD = parse.quote_plus(variables.get('PASSWORD'))


DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD, host=HOST,port=PORT, db=DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

SECRET_KEY = '123456'