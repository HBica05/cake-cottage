# my_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    # Allauth (login/signup/password)
    path("accounts/", include("allauth.urls")),

    # Recipes app handles: home (/), about, contact, CRUD, comments, likes
    path("recipes/", include("recipes.urls")),
    path("", include("recipes.urls")),  # home page and other top-level routes live in recipes.urls
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
