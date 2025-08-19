
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.db import models  # for Q()
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import CommentForm, RecipeForm
from .models import Comment, Recipe, Like


# ---------- Static / Home ----------

def index(request):
    """Redirect '/' to the main recipe list."""
    return redirect("recipe_list")


def about_view(request):
    return render(request, "recipes/about.html")


def contact_view(request):
    """Simple contact handler using settings.DEFAULT_FROM_EMAIL."""
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()

        if not (name and email and message):
            messages.error(request, "Please fill out all fields.")
            return redirect("contact")

        send_mail(
            subject=f"Contact from {name}",
            message=f"From: {name} <{email}>\n\n{message}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
        )
        messages.success(request, "Your message has been sent.")
        return redirect("contact")

    return render(request, "recipes/contact.html")


# ---------- Recipes: List / Detail ----------

def recipe_list(request):
    """
    Show published recipes only.
    Filters:
      - ?category=cake|pastry|bread
      - ?q=search phrase
    """
    qs = Recipe.objects.filter(status=1)

    category = request.GET.get("category")
    if category in {"cake", "pastry", "bread"}:
        qs = qs.filter(category=category)

    q = request.GET.get("q", "").strip()
    if q:
        qs = qs.filter(
            models.Q(title__icontains=q)
            | models.Q(description__icontains=q)
            | models.Q(ingredients__icontains=q)
        )

    context = {"recipes": qs, "current_category": category, "q": q}
    return render(request, "recipes/recipe_list.html", context)


def recipe_detail(request, slug):
    """Recipe page with live comment post support."""
    recipe = get_object_or_404(Recipe, slug=slug, status=1)
    form = CommentForm(request.POST or None)

    if request.method == "POST" and request.user.is_authenticated and form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.recipe = recipe
        comment.save()
        messages.success(request, "Comment posted.")
        return redirect("recipe_detail", slug=slug)

    return render(
        request,
        "recipes/recipe_detail.html",
        {"recipe": recipe, "form": form},
    )


# ---------- Recipes: Create / Edit / Delete ----------

@login_required
def recipe_create(request):
    form = RecipeForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        recipe = form.save(commit=False)
        recipe.author = request.user
        recipe.save()
        messages.success(request, "Recipe created.")
        return redirect("recipe_detail", slug=recipe.slug)
    return render(request, "recipes/recipe_form.html", {"form": form})


@login_required
def recipe_edit(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug, author=request.user)
    form = RecipeForm(request.POST or None, request.FILES or None, instance=recipe)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Recipe updated.")
        return redirect("recipe_detail", slug=recipe.slug)
    return render(request, "recipes/recipe_form.html", {"form": form, "recipe": recipe})


@login_required
def recipe_delete(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug, author=request.user)
    if request.method == "POST":
        recipe.delete()
        messages.info(request, "Recipe deleted.")
        return redirect("recipe_list")
    return render(request, "recipes/recipe_confirm_delete.html", {"recipe": recipe})


# ---------- Likes ----------

@login_required
@require_POST
def toggle_like(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug, status=1)
    like, created = Like.objects.get_or_create(recipe=recipe, user=request.user)
    if created:
        messages.success(request, "Liked!")
    else:
        like.delete()
        messages.info(request, "Like removed.")
    return redirect("recipe_detail", slug=slug)


# ---------- Comments (separate endpoints) ----------

@login_required
@require_POST
def add_comment(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug, status=1)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.recipe = recipe
        comment.save()
        messages.success(request, "Comment added.")
    else:
        messages.error(request, "Please fix the errors in your comment.")
    return redirect("recipe_detail", slug=recipe.slug)


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.user:
        messages.error(request, "You are not allowed to edit this comment.")
        return redirect("recipe_detail", slug=comment.recipe.slug)

    form = CommentForm(request.POST or None, instance=comment)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Comment updated.")
        return redirect("recipe_detail", slug=comment.recipe.slug)
    return render(request, "comments/edit_comment.html", {"form": form, "comment": comment})


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.user:
        comment.delete()
        messages.success(request, "Comment deleted.")
    else:
        messages.error(request, "You are not allowed to delete this comment.")
    return redirect("recipe_detail", slug=comment.recipe.slug)


# ---------- Minimal custom auth (optional if using allauth) ----------

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created.")
            return redirect("recipe_list")
    else:
        form = UserCreationForm()
    return render(request, "recipes/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Logged in.")
            return redirect("recipe_list")
        messages.error(request, "Invalid username or password.")
    return render(request, "recipes/login.html")


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out.")
    return redirect("login")
