from django.conf import settings
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("addRecipe", views.addRecipe.as_view(), name="addRecipe"),
    path("contactUs", views.contactUs, name="contactUs"),
    path("signUp", views.signUp, name="signUp"),
    path("profile/<slug:slug>", views.Profile.as_view(), name="profile"),
    path("myCookbook", views.myCookbook, name="myCookbook"),
    path("register", views.register, name="register"),
    path("login", auth_views.LoginView.as_view(), name='login'),
    path("logout", auth_views.LogoutView.as_view(), name='logout'),
    path("password_change", auth_views.PasswordChangeView.as_view(), name="password_change"),
    path("password_change/done", auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('allRecipes',views.RecipeListView.as_view(), name='allRecipes'),
    path('c/<str:category>', views.CategoryView.as_view(), name='category'),
    path("<pk>/delete", views.deleteRecipe.as_view(), name='deleteRecipe'),
    path(r'editRecipe/(?P<pk>[0-9]+)/$', views.editRecipe.as_view(), name='editRecipe'),
    path('recipes/<slug:slug>', views.RecipeDetailView.as_view(), name='recipeDetail'),
    path('leaveReview/<str:recipeID>', views.leaveReview, name='leaveReview'),

    path("api/counters", views.api_counters, name="api-counters"),
    path("api/toggle", views.api_toggle, name="api-toggle"),
    path("api/saved", views.api_saved, name="api-saved"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
