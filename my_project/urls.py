from django.contrib import admin
from django.urls import path, include
from recipes import views 
from about import views as about_views 

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('about/', about_views.about_me, name='about'),
    path('admin/', admin.site.urls),
    path('recipes/', include('recipes.urls')), 

    # Main Pages
    path('', views.index, name='home'),
    path('menu/', views.menu_view, name='menu'), 
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    # Authentication
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.register, name='signup'),


    # Recipe & Comment Management
    path('recipe/create/', views.recipe_create, name='recipe_create'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('comment/add/<int:recipe_id>/', views.add_comment, name='add_comment'),
    path('comment/edit/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
