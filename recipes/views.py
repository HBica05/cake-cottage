from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe, Comment
from .forms import RecipeForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout  

def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})

def menu_view(request):
    recipes = Recipe.objects.all()
    return render(request, 'menu.html', {'recipes': recipes})

@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    comments = recipe.comments.all()
    
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.recipe = recipe
            new_comment.author = request.user
            new_comment.save()
            messages.success(request, "Comment added successfully! 🎉")
            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        comment_form = CommentForm()

    return render(request, 'recipes/recipe_detail.html', {
        'recipe': recipe,
        'comments': comments,
        'comment_form': comment_form
    })

@login_required
def recipe_create(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            messages.success(request, "Recipe created successfully! 🍰")
            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        form = RecipeForm()
    
    return render(request, 'recipes/recipe_form.html', {'form': form})

@login_required
def recipe_edit(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.user != recipe.author:
        messages.error(request, "You are not authorized to edit this recipe.")
        return redirect('recipe_detail', recipe_id=recipe.id)
    
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(request, "Recipe updated successfully! ✅")
            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        form = RecipeForm(instance=recipe)
    
    return render(request, 'recipes/recipe_form.html', {'form': form})

@login_required
def recipe_delete(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.user == recipe.author:
        recipe.delete()
        messages.success(request, "Recipe deleted successfully! 🗑️")
    else:
        messages.error(request, "You are not authorized to delete this recipe.")
    return redirect('recipe_list')

@login_required
def add_comment(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.recipe = recipe
            comment.author = request.user
            comment.save()
            messages.success(request, "Comment added successfully! 🎉")
            return redirect('recipe_detail', recipe_id=recipe.id)
    
    else:
        form = CommentForm()

    return render(request, 'comments/add_comment.html', {'form': form, 'recipe': recipe})

@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.author:
        return redirect('recipe_detail', recipe_id=comment.recipe.id)
    
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, "Comment updated successfully! ✅")
            return redirect('recipe_detail', recipe_id=comment.recipe.id)
    else:
        form = CommentForm(instance=comment)
    
    return render(request, 'comments/edit_comment.html', {'form': form})

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.author:
        comment.delete()
        messages.success(request, "Comment deleted successfully! 🗑️")
    return redirect('recipe_detail', recipe_id=comment.recipe.id)

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirmPassword"]

        if password == confirm_password:
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, "Account created successfully! 🎉")
                return redirect("login")
            else:
                messages.error(request, "Username already taken! 🚫")
        else:
            messages.error(request, "Passwords do not match! ❌")

    return render(request, "register.html")

def register_user(request):
    return render(request, 'authenticate/register.html', {})

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully! 🎉")
            return redirect("recipe_list")  
        else:
            messages.error(request, "Invalid username or password. ❌")

    return render(request, "login.html")  

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully! 👋")
    return redirect("login")  
