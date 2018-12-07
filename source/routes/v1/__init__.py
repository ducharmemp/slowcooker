from datetime import datetime, timedelta

import jwt
from flask import Blueprint, request, abort, jsonify
from werkzeug.exceptions import NotFound, InternalServerError, BadRequest
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from source.config import CONFIG
from source.models import connection
from source.models.users import User
from .recipes import RecipeResource
from .users import UserResource, UserRecipeResource
from .schemas.users import UserSchema

v1_api = Blueprint("v1", __name__)


for resource in [RecipeResource, UserResource, UserRecipeResource]:
    for route in resource.routes:
        v1_api.add_url_rule(route, view_func=resource.as_view(
            '#'.join([resource.__route_name__, route])), strict_slashes=False)

def encode_jwt(user):
    return {'token': jwt.encode(
        UserSchema(exclude=('id', 'recipes')).dump(user).data,
        CONFIG["auth"]["jwt_salt"],
        headers={
            'exp': (datetime.utcnow() + timedelta(minutes=30)).ctime(),
            'iat': datetime.utcnow().ctime()
        }
    ).decode('ascii')}

def decode_jwt(tok):
    return jwt.decode(
        tok,
        CONFIG["auth"]["jwt_salt"],
        verify=True
    )


@v1_api.route('/users/login', methods=['POST'], strict_slashes=False)
def auth():
    with connection() as session:
        user = request.get_json()
        db_user = session.query(User).filter(User.name == user["name"]).one()
        if not db_user.validate_password(user["password"]):
            abort(401)
        return jsonify(encode_jwt(db_user))


@v1_api.route('/users/login/test', methods=['POST'], strict_slashes=False)
def test():
    pass


@v1_api.route('/users/setup', methods=['POST'], strict_slashes=False)
def setup_user():
    with connection() as session:
        user = UserSchema(session=session).load(request.get_json()).data
        session.add(User(**user))
        session.commit()
        return jsonify(encode_jwt(user))


# @v1_api.before_request
# def before_request():
#     print(request.path)
#     if '/login' in request.path or '/setup' in request.path:
#         return

#     res = (
#         request.headers.get('Authorization') is not None
#         or not request.headers['Authorization']
#     )

#     if not res:
#         abort(401)

#     _, token = request.headers['Authorization'].split()
#     try:
#         decode_jwt(token)
#     except jwt.InvalidTokenError as e:
#         abort(401)


# @v1_api.errorhandler(Exception)
# def handler(e):
#     print(e)
#     res = InternalServerError()
#     if isinstance(e, NoResultFound):
#         res = NotFound()
#     elif isinstance(e, MultipleResultsFound):
#         res = BadRequest()
#     return res
