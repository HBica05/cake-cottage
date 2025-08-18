from django.urls import path
from . import views

urlpatterns = [
    path("", views.recipe_list, name="recipe_list"),     
    path("about/", views.about_view, name="about"),
    path("contact/", views.contact_view, name="contact"),

    path("signup/", views.register, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    path("create/", views.recipe_create, name="recipe_create"),
    path("<slug:slug>/", views.recipe_detail, name="recipe_detail"),
    path("<slug:slug>/edit/", views.recipe_edit, name="recipe_edit"),
    path("<slug:slug>/delete/", views.recipe_delete, name="recipe_delete"),
    path("<slug:slug>/like/", views.toggle_like, name="toggle_like"),

    path("<slug:slug>/comment/add/", views.add_comment, name="add_comment"),
    path("comment/<int:comment_id>/edit/", views.edit_comment, name="edit_comment"),
    path("comment/<int:comment_id>/delete/", views.delete_comment, name="delete_comment"),
]
