from source.models import User, Recipe
from source.utils.marshalling import CustomSchema


class UserSchema(CustomSchema):
    class Meta:
        model = User
        load_only = ("password",)

class UserRecipeSchema(CustomSchema):
    class Meta:
        model = Recipe
