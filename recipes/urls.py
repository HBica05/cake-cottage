from django.urls import path, include
from . import views

urlpatterns = [
    # URL for displaying the list of recipes
    path('', views.recipe_list, name='recipe_list'),
    
    # URL for displaying a specific recipe and its comments
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),

     # URL for adding a comment to a recipe
    path('comment/add/<int:recipe_id>/', views.add_comment, name='add_comment'),
    
    # URL for editing a comment
    path('comment/edit/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    
    # URL for deleting a comment
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
