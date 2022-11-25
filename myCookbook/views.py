from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "myCookbook/index.html")

def addRecipe(request):
    return render(request, "myCookbook/addRecipe.html")

def allRecipes(request):
    return render(request, "myCookbook/allRecipes.html")

def contactUs(request):
    return render(request, "myCookbook/contactUs.html")

def login(request):
    return render(request, "myCookbook/login.html")

def signUp(request):
    return render(request, "myCookbook/signUp.html")

def myCookbook(request):
    return render(request, "myCookbook/myCookbook.html")

def profile(request):
    return render(request, "myCookbook/profile.html")