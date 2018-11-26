from flask import jsonify
from sqlalchemy.orm import Session, lazyload
from sqlalchemy.orm.exc import NoResultFound

from source.models import connection
from source.models import User, Recipe
from source.utils.session_view import SessionView
from source.utils.marshalling import CustomSchema, marshall_with

from .schemas import UserSchema, UserRecipeSchema


class UserResource(SessionView):
    __route_name__ = 'users'

    routes = [
        '/users/',
        '/users/<int:id>'
    ]

    @marshall_with(UserSchema)
    def get(_, session, id=None):
        users = session.query(User)
        if id is not None:
            users = users.filter(User.id == id).one()
        else:
            users = users.all()
        return users

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

    @marshall_with(UserRecipeSchema)
    def get(_, session, id, recipe_id=None):
        res = session.query(User).filter(User.id == id).one().recipes
        if recipe_id is not None:
            res = [recipe for recipe in res if recipe.id == recipe_id][0]
        return res

    @marshall_with(UserRecipeSchema, allow_none=True)
    def post(_, session, id=None, data=None, **kwargs):
        data.creator_id = id
        session.add(data)
        session.commit()
        return data
