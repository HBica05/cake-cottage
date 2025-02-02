# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # URL for displaying the list of recipes
    path('', views.recipe_list, name='recipe_list'),
    
    # URL for displaying a specific recipe and its comments
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
]
