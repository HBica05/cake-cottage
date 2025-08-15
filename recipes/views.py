# recipes/views.py
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from django.views import generic

from .forms import CommentForm, RecipeForm
from .models import Comment, Recipe, Like


# ===== Home / Static =====

def index(request):
    """Redirect home to the recipe list."""
    return redirect("recipe_list")


def about_view(request):
    return render(request, "recipes/about.html")


def contact_view(request):
    """Basic contact form handler (uses email backend from settings)."""
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()

        if not (name and email and message):
            messages.error(request, "Please fill out all fields.")
            return redirect("contact")

        send_mail(
            subject=f"New Contact Message from {name}",
            message=f"From: {name} <{email}>\n\n{message}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )
        messages.success(request, "Your message has been sent successfully!")
        return redirect("contact")

    return render(request, "recipes/contact.html")


# ===== Recipes (List / Detail) =====

class RecipeList(generic.ListView):
    """Optional CBV list if you want pagination."""
    queryset = Recipe.objects.filter(status=1)
    template_name = "recipes/recipe_list.html"
    paginate_by = 6


def recipe_list(request):
    """Function-based list (simple)."""
    recipes = Recipe.objects.filter(status=1)
    return render(request, "recipes/recipe_list.html", {"recipes": recipes})


def recipe_detail(request, slug):
    """Show a published recipe and the comment form."""
    recipe = get_object_or_404(Recipe, slug=slug, status=1)
    form = CommentForm(request.POST or None)
    if request.method == "POST" and request.user.is_authenticated and form.is_valid():
        # Post a comment from the detail page
        comment = form.save(commit=False)
        comment.user = request.user
        comment.recipe = recipe
        comment.save()
        messages.success(request, "Comment posted.")
        return redirect("recipe_detail", slug=slug)
    return render(request, "recipes/recipe_detail.html", {"recipe": recipe, "form": form})


# ===== Recipes (Create / Edit / Delete) =====

@login_required
def recipe_create(request):
    form = RecipeForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        recipe = form.save(commit=False)
        recipe.author = request.user
        recipe.save()
        messages.success(request, "Recipe created successfully!")
        return redirect("recipe_detail", slug=recipe.slug)
    return render(request, "recipes/recipe_form.html", {"form": form})


@login_required
def recipe_edit(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug, author=request.user)
    form = RecipeForm(request.POST or None, request.FILES or None, instance=recipe)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Recipe updated successfully!")
        return redirect("recipe_detail", slug=recipe.slug)
    return render(request, "recipes/recipe_form.html", {"form": form, "recipe": recipe})


@login_required
def recipe_delete(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug, author=request.user)
    if request.method == "POST":
        recipe.delete()
        messages.info(request, "Recipe deleted.")
        return redirect("recipe_list")
    # If GET, show a confirm page
    return render(request, "recipes/recipe_confirm_delete.html", {"recipe": recipe})


# ===== Likes =====

@login_required
@require_POST
def toggle_like(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug, status=1)
    like, created = Like.objects.get_or_create(recipe=recipe, user=request.user)
    if not created:
        like.delete()
        messages.info(request, "Like removed.")
    else:
        messages.success(request, "Liked!")
    return redirect("recipe_detail", slug=slug)


# ===== Comments (separate add/edit/delete endpoints) =====

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
        messages.success(request, "Comment added successfully!")
    else:
        messages.error(request, "There was a problem with your comment.")
    return redirect("recipe_detail", slug=recipe.slug)


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.user:
        messages.error(request, "You are not authorized to edit this comment.")
        return redirect("recipe_detail", slug=comment.recipe.slug)

    form = CommentForm(request.POST or None, instance=comment)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Comment updated successfully!")
        return redirect("recipe_detail", slug=comment.recipe.slug)
    return render(request, "comments/edit_comment.html", {"form": form, "comment": comment})


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.user:
        comment.delete()
        messages.success(request, "Comment deleted.")
    else:
        messages.error(request, "You are not authorized to delete this comment.")
    return redirect("recipe_detail", slug=comment.recipe.slug)


# ===== Auth (simple custom handlers) =====

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully!")
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
            messages.success(request, "Logged in successfully!")
            return redirect("recipe_list")
        messages.error(request, "Invalid username or password.")
    return render(request, "recipes/login.html")


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("login")
