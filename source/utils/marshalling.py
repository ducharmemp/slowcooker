from flask import request, jsonify
from functools import wraps

def marshall_with(schema):
    def wrap(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            data = request.get_json()
            res = func(*args, **kwargs, data=schema.load(data))
            return jsonify(schema.dumps(res))
        return wrapped
    return wrap
