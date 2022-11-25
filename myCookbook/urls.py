from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("addRecipe", views.addRecipe, name="addRecipe"),
    path("allRecipes", views.allRecipes, name="allRecipes"),
    path("contactUs", views.contactUs, name="contactUs"),
    path("login", views.login, name="login"),
    path("signUp", views.signUp, name="signUp"),
    path("profile", views.profile, name="profile"),
    path("myCookbook", views.myCookbook, name="myCookbook"),


]