from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views import View
from .models import User, Recipe, Ingredient
from .forms import UserForm, RecipeForm
from django.http import QueryDict
from django.views.generic.edit import CreateView
from django.contrib import messages

def list_to_string(list):
    
    return (''.join(list))

def index(request):
    return render(request, "myCookbook/index.html")


class addRecipe(View):
    def get(self, request):
        recipeForm = RecipeForm
        return render(request, "myCookbook/addRecipe.html", {"form": recipeForm})

    def post(self, request):
        form = RecipeForm
        name = request.POST['name']
        description = request.POST['description']
        num_servings = request.POST['num_servings']
        min = request.POST['min']
        author = request.user
        instructions = request.POST.getlist('instructions')
        #instructions = list_to_string(instructions)
        
        newRecipe = Recipe(author= author, name=name, instructions=instructions,description=description, num_servings=num_servings,min=min)
        newRecipe.save()
        messages.success(request, f'Recipe posted successfully!')
        return render(request, "myCookbook/addRecipe.html", {"instructions": instructions} )

def allRecipes(request):
    return render(request, "myCookbook/allRecipes.html")


def contactUs(request):
    return render(request, "myCookbook/contactUs.html")

def signUp(request):
    userForm = UserForm
    return render(request, "myCookbook/signUp.html", {"form": userForm})


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        bio = request.POST["bio"]
        theme = request.POST["theme"]
        profile_image = request.POST["profile_image"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "myCookbook/signUp.html", {'form': UserForm,
                                                              "message": "Passwords must match."
                                                              })

        # Attempt to create new user
        try:
            user = User.objects.create_user(
                username=username, email=email, password=password, theme=theme, bio=bio, profile_image=profile_image)
            user.save()
        except IntegrityError:
            return render(request, "myCookbook/signUp.html", {'form': UserForm,
                                                              "message": "Username already taken."
                                                              })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "myCookbook/index.html")


def myCookbook(request):
    return render(request, "myCookbook/myCookbook.html")


def profile(request):
    return render(request, "myCookbook/profile.html")
