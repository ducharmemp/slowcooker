from flask import Blueprint
from werkzeug.exceptions import NotFound, InternalServerError, BadRequest
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from .recipes import RecipeResource
from .users import UserResource, UserRecipeResource

v1_api = Blueprint("v1", __name__)


for resource in [RecipeResource, UserResource, UserRecipeResource]:
    for route in resource.routes:
        v1_api.add_url_rule(route, view_func=resource.as_view(
            '#'.join([resource.__route_name__, route])), strict_slashes=False)


# @v1_api.errorhandler(Exception)
# def handler(e):
#     print(e)
#     res = InternalServerError()
#     if isinstance(e, NoResultFound):
#         res = NotFound()
#     elif isinstance(e, MultipleResultsFound):
#         res = BadRequest()
#     return res
