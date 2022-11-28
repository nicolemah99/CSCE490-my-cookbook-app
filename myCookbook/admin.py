from django.contrib import admin
from .models import User, Ingredient, Recipe, RecipeIngredient

admin.site.register(User)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(RecipeIngredient)
