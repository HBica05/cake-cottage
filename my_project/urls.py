from django.contrib import admin
from django.urls import path, include
from recipes import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipes/', include('recipes.urls')), 

    # Main Pages
    path('', views.index, name='home'), 
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),

    # Authentication (Only include allauth)
    path("accounts/", include("allauth.urls")),

    # Recipe & Comment Management
    path('recipe/create/', views.recipe_create, name='recipe_create'),
    path('<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('comment/add/<int:recipe_id>/', views.add_comment, name='add_comment'),
    path('comment/edit/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
