from flask import jsonify


def user_serializer(userinfo):
    user_dict = {}
    user_list = []
    for user in userinfo:
        user_dict = {
            'username': user.username,
            'password': user.password,
            'id': user.id,
        }
        user_list.append(user_dict)
    return jsonify({'user_list': user_list, "status": 1})

def now_user_serializer(data):
    user_dict = {}
    user_list = []
    user_dict = {
        'username':data
    }
    user_list.append(user_dict)
    print(user_list)
    return  jsonify({'user_list': user_list, "status": 1})


