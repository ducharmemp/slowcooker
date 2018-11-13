from flask.views import MethodView
from marshmallow import Schema, fields
from sqlalchemy.orm import Session

from source.models import connection


class RecipeStepSchema(Schema):
    id = fields.Integer()
    number = fields.Integer()
    description = fields.String()
    comment = fields.String()


class RecipeSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    steps = fields.Nested(RecipeStepSchema, many=True)


class RecipeResource(MethodView):
    @staticmethod
    def get():
        with connection() as session:  # type: Session
            return session.query()

    @staticmethod
    def post():
        with connection() as session:  # type Session
            return session.query()
