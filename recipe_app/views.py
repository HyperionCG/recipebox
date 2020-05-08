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