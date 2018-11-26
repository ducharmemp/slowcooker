import inspect
from copy import deepcopy
from operator import getitem

from flask import request, jsonify, abort
from functools import wraps, partial, update_wrapper

from marshmallow import fields, pre_load
from marshmallow_sqlalchemy import ModelSchema


class SmartNested(fields.Nested):
    def serialize(self, attr, obj, accessor=None):
        return super(SmartNested, self).serialize(attr, obj, accessor)


class CustomSchema(ModelSchema):
    @pre_load
    def set_field_session(self, data):
        for value in filter(
                lambda f: hasattr(
                    f,
                    'schema'),
                self.fields.values()):
            value.schema.session = self.session

    @pre_load
    def set_field_partial(self, data):
        for value in filter(
                lambda f: hasattr(
                    f,
                    'schema'),
                self.fields.values()):
            value.schema.partial = self.partial


def marshall_with(schema, allow_none=False):
    def wrap(func):
        @wraps(func)
        def wrapped(_, session, *args, **kwargs):
            inner_func = partial(func, _, session, *args, **kwargs)
            schema_obj = schema(session=session, partial=True)

            if request.method in {'GET', 'DELETE', 'HEAD', 'OPTIONS', 'TRACE'}:
                res = inner_func()
            else:
                data = request.get_json()
                if data is None and allow_none is not True:
                    abort(400)
                elif data is None:
                    data = {}
                unmarshalled = schema_obj.load(
                    data, many=isinstance(data, list))
                if unmarshalled.errors:
                    return jsonify(unmarshalled.errors), 400
                res = inner_func(data=unmarshalled.data)
            marshalled = schema_obj.dump(res, many=isinstance(res, list))
            return jsonify(marshalled.data)
        return wrapped
    return wrap
