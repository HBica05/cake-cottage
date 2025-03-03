from django.urls import path
from . import views  

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),  # Display all recipes
    path('<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),  # Display a specific recipe
    path('menu/', views.menu_view, name='menu_view'),

    path('create/', views.recipe_create, name='recipe_create'),  # Create a recipe
    path('<int:recipe_id>/edit/', views.recipe_edit, name='recipe_edit'),  # Edit a recipe
    path('<int:recipe_id>/delete/', views.recipe_delete, name='recipe_delete'),  # Delete a recipe
    
    path('<int:recipe_id>/comment/add/', views.add_comment, name='add_comment'),  # Add a comment
    path('comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),  # Edit a comment
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),  # Delete a comment

    # ✅ Add missing views
    path('about/', views.about_view, name='about'),  # About Us Page
    path('contact/', views.contact_view, name='contact'),  # Contact Page
]
