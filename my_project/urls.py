from django.contrib import admin
from django.urls import path, include
from recipes import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),

    path('', views.index, name='home'),  # ✅ Correctly points to index.html
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('menu/', views.menu_view, name='menu'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.register, name='signup'),

    path('recipe/create/', views.recipe_create, name='recipe_create'),
    path('recipes/', include('recipes.urls')),

    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('comment/add/<int:recipe_id>/', views.add_comment, name='add_comment'),
    path('comment/edit/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
from django.contrib import admin
from django.urls import path, include
from recipes import views  

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),  # Home Page
    path('menu/', views.menu_view, name='menu'), 
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.register, name='signup'),
    path('recipe/create/', views.recipe_create, name='recipe_create'),
    path('recipes/', include('recipes.urls')),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('comment/add/<int:recipe_id>/', views.add_comment, name='add_comment'),
    path('comment/edit/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
