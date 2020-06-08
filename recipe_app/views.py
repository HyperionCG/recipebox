from django.shortcuts import render, reverse, HttpResponseRedirect
from recipe_app.models import Author, Recipe
from recipe_app.forms import recipe_form, author_form, login_form
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from recipe_app.handle_forms import *

def login_view(request):
    form = login_form()
    return render(request, 'standard_form.html', {'form': form})

# Create your views here.
def index(request):
    authors = Author.objects.all()
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'authors': authors, 'recipes': recipes})

def recipe_page(request, id):
    recipe = Recipe.objects.get(id=id)
    return render(request, 'recipe_page.html', {'recipe': recipe})

def author_page(request, id):
    author = Author.objects.get(id=id)
    recipes = Recipe.objects.filter(author=author)
    return render(
        request, 'author_page.html', {'author': author, 'recipes': recipes}
    )

def add_recipe_form(request):
    form = recipe_form()
    return render(request, 'standard_form.html', {'form': form})

def handle_standard_form(request, form_type):
    types = {
        "author_form": handle_author(request),
        "recipe_form": handle_recipe(request),
        "login": handle_login(request)
        }
    return types[form_type]

@login_required
def add_author_form(request):
    form = author_form()
    return render(request, 'standard_form.html', {'form': form})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

@login_required
def edit_view(request, id):
    recipe = Recipe.objects.get(id=id)
    if request.method == "POST":
        form = recipe_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            recipe.title = data['title']
            recipe.description = data['description']
            recipe.time_required = data['time_required']
            recipe.instructions = data['instructions']
            recipe.author = data['author']
            recipe.save()
            return HttpResponseRedirect(reverse('', args=(id)))

        form = recipe_form(initial={
            'title': recipe.title,
            'description': recipe.description
            'time_required': recipe.time_required
            'instructions': recipe.instructions
            'author': recipe.author
        })
        return render(request, "recipe_page.htm", {'form': form})

@login_required
def add_favorite(request, id):
    recipe = Recipe.objects.get(id=id)
    request.user.author.favorites.add(recipe)
    return HttpResponseRedirect(reverse("recipe",args=(id,)))

@login_required
def unadd_favorite(request,id):
    recipe = Recipe.objects.get(id=id)
    request.user.author.favorites.remove(recipe)
    return HttpResponseRedirect(reverse("recipe",args=(id,)))