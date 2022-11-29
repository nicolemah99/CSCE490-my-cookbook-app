from django.contrib import admin
from .models import User, Ingredient, Recipe

admin.site.register(User)
admin.site.register(Ingredient)
admin.site.register(Recipe)
