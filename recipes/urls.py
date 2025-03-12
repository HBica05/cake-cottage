from django.urls import path
from . import views  

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),  # ✅ Home route as recipe_list
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),

    # Recipe-related views
    path('<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('create/', views.recipe_create, name='recipe_create'),
    path('<int:recipe_id>/edit/', views.recipe_edit, name='recipe_edit'),
    path('<int:recipe_id>/delete/', views.recipe_delete, name='recipe_delete'),

    # Comments
    path('<int:recipe_id>/comment/add/', views.add_comment, name='add_comment'),
    path('comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),

    # Auth
    path('signup/', views.register, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
