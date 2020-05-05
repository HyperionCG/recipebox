from django.shortcuts import render, reverse
from recipe_app.models import Author, Recipe
from recipe_app.forms import recipe_form, author_form
from django.http import HttpResponseRedirect

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
    if request.method == 'POST':
        form = recipe_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data['title'],
                time_required=data['time_required'],
                description=data['description'],
                instructions=data['instructions'],
                author=data['author']
            )
            return HttpResponseRedirect(reverse('home'))
    form = recipe_form()
    return render(request, 'recipe_form.html', {'form': form})

def add_author_form(request):
    if request.method == 'POST':
        form = author_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name=data['name'],
                bio=data['bio']
            )
            return HttpResponseRedirect(reverse('home'))
    form = author_form()
    return render(request, 'author_form.html', {'form': form})