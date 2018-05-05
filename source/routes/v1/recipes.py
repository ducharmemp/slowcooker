from flask.views import MethodView
from marshmallow import Schema, fields
from sqlalchemy.orm import Session

from source.models import connection


class RecipeSchema(Schema):
    id = fields.Integer()


class RecipeResource(MethodView):
    def get(self):
        with connection() as session:  # type: Session
            return session.query()
