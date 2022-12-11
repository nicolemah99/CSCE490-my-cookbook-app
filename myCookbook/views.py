from django.db import IntegrityError
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views import View
from .models import Review, User, Recipe, Category
from .forms import EditUserForm, UserForm, RecipeForm, ReviewForm
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
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


class addRecipe(LoginRequiredMixin,View):
    login_url = 'login'

    def get(self, request):
        recipeForm = RecipeForm
        return render(request, "myCookbook/addRecipe.html", {"form": recipeForm})

    def post(self, request):
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            newRecipe = form.save(commit=False)
            newRecipe.author = request.user
            instructions = request.POST.getlist('instructions')
            instructions = ':'.join(str(x) for x in instructions).replace(',',';')
            ingredients = request.POST.getlist('ingredients')
            ingredients = grouper(3,ingredients)
            newRecipe.instructions = instructions
            newRecipe.ingredients = ingredients
            newRecipe.save()
            form.save_m2m()
        
        messages.success(request, f'Recipe posted!')
        return render(request, 'myCookbook/index.html', {"form":form})

class FilteredListView(ListView):
    filterset_class = None
    
class CategoryView(ListView):
    model = Recipe
    template_name = 'myCookbook/allRecipes.html'
    context_object_name = 'recipes'
    paginate_by = 9

    def get_queryset(self, *args, **kwargs):
        return Recipe.objects.filter(categories__name__icontains = self.kwargs.get('category'))

class RecipeListView(ListView):
    model = Recipe
    template_name = 'myCookbook/allRecipes.html'
    context_object_name = 'recipes'
    paginate_by = 9
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(name__icontains=query)
        else:
            object_list = self.model.objects.all().order_by('date_posted')
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all().order_by('name')
        return context

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'myCookbook/recipeDetail.html'
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        newIngredients = []
        context = super(RecipeDetailView,self).get_context_data(**kwargs)
        newIngredients = self.object.ingredients.split(":")
        newIngredients = grouper(3,newIngredients)
        context['newIngredients'] = newIngredients
        context['newInstructions'] = self.object.instructions.replace(';',',').split(':')
        context['reviews'] = Review.objects.filter(recipe=self.object.id)
        context['form'] = ReviewForm
        
        return context
        
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
                username=username, email=email, password=password, bio=bio)
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
    saved = request.user.saved_recipes.all().order_by('name')
    myRecipes = Recipe.objects.filter(author=request.user).order_by('date_posted')
    allRecipes = saved | myRecipes
    allRecipes = allRecipes.all().order_by('name')
    
    return render(request,'myCookbook/myCookbook.html',{
        'savedRecipes':saved,'myRecipes': myRecipes, 'allRecipes':allRecipes
    })

class Profile(DetailView):
    model = User
    template_name = 'myCookbook/profile.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipes'] = Recipe.objects.filter(author=self.object.id)
        context['num_recipes_posted'] = len(context['recipes'])
        context['recipes_saved'] = self.object.saved_recipes.all()
        context['num_recipes_saved'] = len(self.object.saved_recipes.all())
        return context
    

class deleteRecipe(DeleteView):
    model = Recipe
    success_url = reverse_lazy('myCookbook')

class editRecipe(UpdateView):
    model = Recipe
    fields = ["name",'description','categories','num_servings','min','image']
    success_url = 'myCookbook/profile.html'

def api_toggle(request):
    if not request.user.is_authenticated:
        return JsonResponse({})
    recipe_id = request.GET['recipe_id']
    recipe = Recipe.objects.get(id=recipe_id)
    in_cookbook = recipe.savers.filter(id=request.user.id).exists()
    if in_cookbook:
        recipe.savers.remove(request.user)
    else:
        recipe.savers.add(request.user)
    in_cookbook = not in_cookbook
    status = {
        'user': request.user.username,
        'in_cookbook': in_cookbook,
        'my_saves': request.user.saved_recipes.all().count()
    }
    return JsonResponse(status)

def api_saved(request):
    # should check of user is_authenticated and recipe_id is valid
    if not request.user.is_authenticated:
        return JsonResponse({})
    recipe_id = request.GET['recipe_id']
    recipe = Recipe.objects.get(id=recipe_id)
    status = {
        'in_cookbook': recipe.savers.filter(id=request.user.id).exists()
    }
    return JsonResponse(status)

def api_counters(request):
    user = request.user
    counts = {}
    if user.is_authenticated:
        counts['my_recipes'] = Recipe.objects.filter(author=user).count()
        counts['my_saves'] = user.saved_recipes.all().count()
    return JsonResponse(counts)

def leaveReview(request, recipeID):
    recipe = Recipe.objects.get(id=recipeID)
    
    if request.POST:
        form = ReviewForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.recipe = recipe
            obj.reviewer = request.user
            obj.save()
            messages.success(request,f'Review of {obj.recipe.name} posted')
        return redirect(f"index")

class EditUser(UpdateView):
    model = User
    form_class = EditUserForm

    def get_success_url(self):
          slug=self.kwargs['slug']
          return reverse_lazy('profile', kwargs={'slug': slug})
