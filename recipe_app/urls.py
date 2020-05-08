#from django.contrib import admin
from django.urls import path
from recipe_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('author/<int:id>/', views.author_page, name='author'),
    path('recipe/<int:id>/', views.recipe_page, name='recipe'),
    path('<str:form_type>/standard_form/', views.handle_standard_form),
    path('recipe_form/', views.add_recipe_form, name='recipe_form'),
    path('author_form/', views.add_author_form, name='author_form'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_user, name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
