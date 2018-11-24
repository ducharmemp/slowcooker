from flask import Blueprint
from .recipes import RecipeResource
from .users import UserResource

v1_api = Blueprint("v1", __name__)


for resource in [RecipeResource, UserResource]:
    for route in resource.routes:
        v1_api.add_url_rule(route, view_func=resource.as_view('#'.join([resource.__route_name__, route])), strict_slashes=False)

