from marshmallow import Schema, fields
from sqlalchemy.orm import Session
from flask import request, jsonify

from source.models import Recipe
from source.utils.session_view import SessionView
from source.utils.marshalling import marshall_with


# class RecipeStepSchema(Schema):
#     id = fields.Integer()
#     number = fields.Integer()
#     description = fields.String()
#     comment = fields.String()


class RecipeSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    # steps = fields.Nested(RecipeStepSchema, many=True)


class RecipeResource(SessionView):
    __route_name__ = 'recipes'

    routes = [
        '/recipes',
        '/recipes/<int:id>'
    ]

    # @marshall_with(RecipeResource)
    def get(_, session, id=None):
        res = session.query(Recipe)
        if id is not None:
            return jsonify(res.filter(Recipe.id == id).first())
        else:
            return jsonify(res.all())

    # @marshall_with(RecipeResource)
    def post(_, session: Session, id=None):
        recipe = Recipe()
        session.add(recipe)
        session.commit()
        return recipe.id

    # @marshall_with(RecipeResource)
    def put(_, session, id=None):
        recipe = session.query(Recipe).filter(Recipe.id == id).first()
        for key, value in request.get_json():
            setattr(recipe, key, value)
        session.commit()

    # @marshall_with(RecipeResource)
    def delete(_, session, id=None):
        session.query(Recipe).filter(Recipe.id == id).delete()
        session.commit()
