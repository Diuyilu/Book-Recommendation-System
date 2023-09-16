from flask import jsonify


def user_serializer(userinfo):
    user_dict = {}
    user_list = []
    for user in userinfo:
        user_dict = {
            'username': user.username,
            'password': user.password,
        }
        user_list.append(user_dict)
    return jsonify({'user_list': user_list, "status": 1})

