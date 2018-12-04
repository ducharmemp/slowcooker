from sqlalchemy.orm import Session
from flask import request, jsonify

from source.models import Recipe, RecipeStep
from source.utils.session_view import SessionView
from source.utils.marshalling import marshall_with, request_kwargs

from source.utils.sql import windowed_query

from .schemas import RecipeSchema


class RecipeResource(SessionView):
    __route_name__ = 'recipes'

    routes = [
        '/recipes',
        '/recipes/<int:id>'
    ]

    @marshall_with(RecipeSchema)
    @request_kwargs('page', 'limit')
    def get(_, session, id=None, page=0, limit=25):
        page = int(page)
        limit = min([int(limit), 25])
        res = session.query(Recipe)
        if id is not None:
            return res.filter(Recipe.id == id).first()
        else:
            return [*windowed_query(res, Recipe.id, limit, page)]

    @marshall_with(RecipeSchema)
    def post(_, session: Session, id=None, data=None):
        session.add(data)
        session.commit()
        return data.id

    @marshall_with(RecipeSchema)
    def patch(_, session, id=None, data=None):
        session.merge(data, load=True)
        session.commit()

    @marshall_with(RecipeSchema)
    def delete(_, session, id=None):
        session.query(Recipe).filter(Recipe.id == id).delete()
        session.commit()
