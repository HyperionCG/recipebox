#from django.contrib import admin
from django.urls import path
from recipe_app import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index),
    path('author/<int:id>/', views.author_page, name='author'),
    path('recipe/<int:id>/', views.recipe_page, name='recipe')
]
