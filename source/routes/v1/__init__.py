from flask import Blueprint
from .recipes import RecipeResource

v1_api = Blueprint("v1", __name__)

v1_api.add_url_rule('/recipes', view_func=RecipeResource.as_view('recipes'))
