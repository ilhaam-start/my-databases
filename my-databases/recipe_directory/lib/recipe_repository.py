from lib.recipe import Recipe

class RecipeRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM recipes')
        recipes = []
        for row in rows:
            recipe = Recipe(row['name'], row['cooking_time'], row['rating'])
            recipes.append(recipe)
        # recipe = [row for row in rows (Recipe(['name'], ['cooking_time'], ['rating']))]
        return recipes
    
    def find(self, id):
        result = self._connection.execute('SELECT * FROM recipes WHERE id = %s', [id])
        result = result[0]
        return Recipe(result['name'], result['cooking_time'], result['rating'])





