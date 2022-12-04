from django.contrib import admin
from .models import User, Category, Recipe

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Recipe)
