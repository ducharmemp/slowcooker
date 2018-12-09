import inspect
from functools import wraps, partial

import jwt
from flask import request, abort

def restrict_access(jwt_salt, func=None):
    if func is None:
        return lambda f: restrict_access(jwt_salt, f)


    @wraps(func)
    def wrapper(*args, **kwargs):
        if not request.headers.get('Authorization'):
            abort(401)

        _, token = request.headers['Authorization'].split()
        try:
            jwt.decode(token, jwt_salt)
        except jwt.InvalidTokenError as error:
            abort(401)
        return func(*args, **kwargs)

    return wrapper
