#from django.contrib import admin
from django.urls import path
from recipe_app import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('author/<int:id>/', views.author_page, name='author'),
    path('recipe/<int:id>/', views.recipe_page, name='recipe'),
    path('recipe_form/', views.add_recipe_form, name='recipe_form'),
    path('author_form/', views.add_author_form, name='author_form')
]
