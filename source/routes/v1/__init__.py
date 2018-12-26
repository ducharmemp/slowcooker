from functools import partial
from datetime import datetime, timedelta

import jwt
from flask import Blueprint, request, abort, jsonify
from werkzeug.exceptions import NotFound, InternalServerError, BadRequest
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from source.config import CONFIG
from source.models import connection
from source.models.users import User
from source.utils.token import encode_jwt
from source.utils.auth import restrict_access as restriction_factory

jwt_salt = CONFIG['auth']['jwt_salt']
restrict_access = restriction_factory(jwt_salt)

from .recipes import RecipeResource
from .users import UserResource, UserRecipeResource
from .schemas.users import UserSchema

v1_api = Blueprint("v1", __name__)

for resource in [RecipeResource, UserResource, UserRecipeResource]:
    for route in resource.routes:
        v1_api.add_url_rule(route, view_func=resource.as_view(
            '#'.join([resource.__route_name__, route])), strict_slashes=False)


@v1_api.route('/users/login', methods=['POST'], strict_slashes=False)
def auth():
    with connection() as session:
        user = request.get_json()
        db_user = session.query(User).filter(User.name == user["name"]).one()
        if not db_user.validate_password(user["password"]):
            abort(401)
        return jsonify(encode_jwt(UserSchema(session=session).dump(db_user).data, jwt_salt))


@v1_api.route('/users/setup', methods=['POST'], strict_slashes=False)
def setup_user():
    with connection() as session:
        user = UserSchema(session=session).load(request.get_json()).data
        session.add(user)
        session.commit()
        return jsonify(encode_jwt(user, jwt_salt))

