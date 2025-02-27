from django.contrib import admin
from django.urls import path, include  #  Ensure 'include' is imported
from recipes import views  #  Import views from the 'recipes' app
from recipes.views import register  #  Import 'register' function correctly

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.recipe_list, name='recipe_list'),  # ✅ Use views from 'recipes'
    path('login/', views.login_view, name='login'),
     path('logout/', views.logout_view, name='logout'),  # ✅ Logout added
    path('signup/', views.register, name='signup'),
    path('recipe/create/', views.recipe_create, name='recipe_create'),

    path('recipes/', include('recipes.urls')),  # ✅ Ensure 'recipes.urls' is included

    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('comment/add/<int:recipe_id>/', views.add_comment, name='add_comment'),
    path('comment/edit/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
