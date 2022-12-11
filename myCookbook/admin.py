from django.contrib import admin
from .models import User, Category, Recipe, Review

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Review)

class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name')}