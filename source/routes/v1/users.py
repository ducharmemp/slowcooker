from flask import jsonify
from flask.views import MethodView
from marshmallow import Schema, fields
from sqlalchemy.orm import Session

from source.models import connection
from source.models.users import User

class UserSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    recipes = fields.Url(relative=True, many=True)


class UserResource(MethodView):
    __route_name__ = 'users'

    routes = [
        '/users/',
        '/users/<int:id>'
    ]

    def get(_, _id=None):
        with connection() as session:  # type: Session
            users = session.query(User)
            if _id is not None:
                users = users.filter(User.id==_id).one()
            else:
                users = users.all()
            return jsonify(users)

    def post(_):
        with connection() as session:  # type Session
            user = User()
            session.add(User)
            session.commit()
            return user.id
