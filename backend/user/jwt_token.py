import jwt
from jwt import PyJWTError
from datetime import datetime,timedelta

SECRECT_KEY = b'\x92R!\x8e\xc6\x9c\xb3\x89#\xa6\x0c\xcb\xf6\xcb\xd7\xbc'


def genToken(data):
  expInt = datetime.utcnow() + timedelta(seconds=3)
  payload = {
    'exp': expInt,
    'data': data
    }
  token = jwt.encode(payload,key= SECRECT_KEY,algorithm= 'HS256')
  print(token)
  return token
  # return bytes.decode(token)

def verfiyToken(tokenStr):
  try:
    tokenBytes =  tokenStr.encode('utf-8')
    payload = jwt.decode(tokenBytes,key= SECRECT_KEY,algorithm= 'HS256')
    return payload
  except PyJWTError as e:
    print("jwt验证失败: %s" % e)
    return None