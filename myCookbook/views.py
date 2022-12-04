from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import View
from .models import User, Recipe, Ingredient
from .forms import UserForm, RecipeForm
from django.http import QueryDict
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib import messages
from itertools import zip_longest
import random

def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return list(zip_longest(fillvalue=fillvalue, *args))

def index(request):
    allRecipes = list(Recipe.objects.all())
    randomRecipes = random.sample(allRecipes,3)
    return render(request, "myCookbook/index.html", {'recipes':randomRecipes})


class addRecipe(View):
    def get(self, request):
        recipeForm = RecipeForm
        return render(request, "myCookbook/addRecipe.html", {"form": recipeForm})

    def post(self, request):
        form = RecipeForm(request.POST, request.FILES)
        newRecipe = form.save(commit=False)
        newRecipe.author = request.user
        instructions = request.POST.getlist('instructions')
        ingredients = request.POST.getlist('ingredients')
        ingredients = grouper(3,ingredients)
        newRecipe.instructions = instructions
        newRecipe.ingredients = ingredients
        newRecipe.save()
        messages.success(request, f'Recipe posted!')
        return render(request, 'myCookbook/addRecipe.html', {"form":form})

def allRecipes(request):
    return render(request, "myCookbook/allRecipes.html")

class RecipeListView(ListView):
    model = Recipe
    template_name = 'myCookbook/allRecipes.html'
    context_object_name = 'recipes'
    paginate_by = 2

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
                username=username, email=email, password=password, theme=theme, bio=bio)
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
    currentUser = User.objects.get(username = request.user)
    recipes = Recipe.objects.filter(author=currentUser)
    numRecipes = len(recipes)
    User.objects.filter(username=request.user).update(num_recipes_posted=numRecipes)
    return render(request, "myCookbook/profile.html", {'user':currentUser, 'recipes':recipes})
