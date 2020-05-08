from django.shortcuts import render, reverse, HttpResponseRedirect
from recipe_app.models import Author, Recipe
from recipe_app.forms import recipe_form, author_form, login_form
from django.contrib.auth import login, logout, authenticate

# This page handles the POST data being sent by
# the standard_form

def handle_author(request):
    if request.method == "POST":
        form = author_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name=data['name'],
                bio=data['bio']
            )
            return HttpResponseRedirect(reverse('home'))

def handle_recipe(request):
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

def handle_login(request):
    if request.method == "POST":
        form = login_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
                )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('home'))
                )
