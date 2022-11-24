from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("addRecipe", views.addRecipe, name="addRecipe"),
    path("allRecipes", views.allRecipes, name="allRecipes"),
    path("contactUs", views.contactUs, name="contactUs"),


]