from django.contrib import admin
from django.urls import path, include

from . import views
from .views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.recipe_list, name='recipe_list'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('recipe/create/', views.recipe_create, name='recipe_create'),

    path('recipes/', include('recipes.urls')), 

    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('comment/add/<int:recipe_id>/', views.add_comment, name='add_comment'),
    path('comment/edit/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path("register/", register, name="register"),
]
