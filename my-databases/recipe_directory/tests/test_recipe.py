from lib.recipe import Recipe

"""
When constructing a recipe
Can access the recipe attributes
"""
def test_recipe_constructs():
    recipe = Recipe('Lasagna', 60, 5)
    assert recipe.name == 'Lasagna' 
    assert recipe.cooking_time == 60
    assert recipe.rating == 5

