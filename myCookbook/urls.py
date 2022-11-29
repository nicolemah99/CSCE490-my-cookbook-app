from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="index"),
    path("addRecipe", views.addRecipe.as_view(), name="addRecipe"),
    path("allRecipes", views.allRecipes, name="allRecipes"),
    path("contactUs", views.contactUs, name="contactUs"),
    path("signUp", views.signUp, name="signUp"),
    path("profile", views.profile, name="profile"),
    path("myCookbook", views.myCookbook, name="myCookbook"),
    path("register", views.register, name="register"),
    path("login", auth_views.LoginView.as_view(), name='login'),
    path("logout", auth_views.LogoutView.as_view(), name='logout'),

]