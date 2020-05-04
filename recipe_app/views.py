from django.shortcuts import render
from recipe_app.models import Author, Recipe

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