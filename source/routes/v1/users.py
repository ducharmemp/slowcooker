import uuid

import jwt
from flask import jsonify, request, make_response, abort
from sqlalchemy.orm import Session, lazyload
from sqlalchemy.orm.exc import NoResultFound

from source.config import CONFIG
from source.models import connection
from source.models import User, Recipe
from source.utils.session_view import SessionView
from source.utils.marshalling import CustomSchema, marshall_with, request_kwargs

from . import restrict_access
from .schemas import UserSchema, UserRecipeSchema


class UserResource(SessionView):
    __route_name__ = 'users'

    routes = [
        '/users/',
        '/users/<int:id>'
    ]

    @marshall_with(UserSchema)
    @request_kwargs('page', 'limit')
    def get(_, session, id=None, page=0, limit=25):
        users = session.query(User)
        if id is not None:
            users = users.filter(User.id == id).one()
        else:
            users = users.all()
        return users

    @restrict_access
    @marshall_with(UserSchema, allow_none=True)
    def post(_, session, data=None, **kwargs):
        session.add(data)
        session.commit()
        return data


class UserRecipeResource(SessionView):
    __route_name__ = 'users_recipes'

    routes = [
        '/users/<int:id>/recipes',
        '/users/<int:id>/recipes/<int:recipe_id>'
    ]

    @restrict_access
    @marshall_with(UserRecipeSchema)
    def get(_, session, id, recipe_id=None):
        res = session.query(User).filter(User.id == id).one().recipes
        if recipe_id is not None:
            res = [recipe for recipe in res if recipe.id == recipe_id][0]
        return res

    @restrict_access
    @marshall_with(UserRecipeSchema, allow_none=True)
    def post(_, session, id, data=None):
        files = request.files
