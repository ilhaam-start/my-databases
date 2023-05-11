from lib.recipe_repository import RecipeRepository
from lib.recipe import Recipe

"""
When calling #all on RecipeRepository
We get a list of all recipes
"""
def test_view_all_recipes(db_connection):
    db_connection.seed('seeds/recipe_directory.sql')
    recipe_repo = RecipeRepository(db_connection)

    recipes = recipe_repo.all()

    assert recipes == [
        Recipe('Lasagna', 60, 5),
        Recipe('Trifle', 30, 1),
        Recipe('Jollof Rice', 60, 5),
        Recipe('Chocolate Oreo Cake', 80, 4)
    ]

"""
When calling #find on the RecipeRepository
Retrieves the first entry
"""
def test_find_returns_first_entry(db_connection):
    db_connection.seed('seeds/recipe_directory.sql')
    recipe_repo = RecipeRepository(db_connection)

    assert recipe_repo.find(1) == Recipe('Lasagna', 60, 5)
    assert recipe_repo.find(2) == Recipe('Trifle', 30, 1)