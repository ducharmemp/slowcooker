from source.models import User, Recipe
from source.utils.marshalling import CustomSchema


class UserSchema(CustomSchema):
    class Meta:
        model = User

class UserRecipeSchema(CustomSchema):
    class Meta:
        model = Recipe
