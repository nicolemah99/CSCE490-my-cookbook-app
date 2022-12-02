from django.conf import settings
from django.contrib import admin
from django.urls import path
from . import views, forms
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

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
    path("password_change", auth_views.PasswordChangeView.as_view(), name="password_change"),
    path("password_change/done", auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
