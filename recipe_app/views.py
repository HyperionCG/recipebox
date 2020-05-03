from django.shortcuts import render
from recipe_app.models import Author, Recipe

# Create your views here.
def index(request):
    authors = Author.objects.all()
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'authors': authors, 'recipes': recipes})
