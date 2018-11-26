from source.models import Recipe, RecipeStep
from source.utils.marshalling import SmartNested, CustomSchema


class RecipeStepSchema(CustomSchema):
    class Meta:
        model = RecipeStep


class RecipeSchema(CustomSchema):
    class Meta:
        model = Recipe

    steps = SmartNested(RecipeStepSchema, many=True)
