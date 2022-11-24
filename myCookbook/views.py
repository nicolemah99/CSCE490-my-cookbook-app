from django.shortcuts import render

def index(request):
    return render(request, "myCookbook/index.html")

def addRecipe(request):
    return render(request, "myCookbook/addRecipe.html")

def allRecipes(request):
    return render(request, "myCookbook/allRecipes.html")

def contactUs(request):
    return render(request, "myCookbook/contactUs.html")