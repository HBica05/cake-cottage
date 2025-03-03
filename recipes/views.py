from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe, Comment
from .forms import RecipeForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout  
from django.core.mail import send_mail 
from django.conf import settings 


# ✅ Home Page View
def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/index.html', {'recipes': recipes})

# ✅ Menu Page View
def menu_view(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/menu.html', {'recipes': recipes})

# ✅ About Page View
def about_view(request):
    return render(request, 'recipes/about.html')

# ✅ Updated Contact Page View to Handle Form Submission
def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        subject = f"New Contact Form Submission from {name}"
        email_message = f"Message: {message}\n\nFrom: {name} ({email})"

        # Send email (Ensure email settings are configured in settings.py)
        send_mail(
            subject=f"New Contact Message from {name}",
            message=f"Message from {name} ({email}):\n\n{message}",
            from_email=settings.DEFAULT_FROM_EMAIL,  # Ensure this is set in settings.py
            recipient_list=["your-email@example.com"],  # Change this to your email
            fail_silently=False,
        )

        messages.success(request, "Your message has been sent successfully! ✅")
        return redirect("contact")

    return render(request, "recipes/contact.html")

# ✅ Recipe List View
@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

# ✅ Recipe Detail View
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

# ✅ Recipe Creation View
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

# ✅ Recipe Edit View
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

# ✅ Recipe Delete View
@login_required
def recipe_delete(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.user == recipe.author:
        recipe.delete()
        messages.success(request, "Recipe deleted successfully! 🗑️")
    else:
        messages.error(request, "You are not authorized to delete this recipe.")
    return redirect('recipe_list')

# ✅ Add Comment View
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

# ✅ Edit Comment View
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

# ✅ Delete Comment View
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.author:
        comment.delete()
        messages.success(request, "Comment deleted successfully! 🗑️")
    return redirect('recipe_detail', recipe_id=comment.recipe.id)

# ✅ User Registration View (Fixed Redirect)
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after signup
            messages.success(request, "Account created successfully! 🎉")
            return redirect("home")  # ✅ Fixed redirect
    else:
        form = UserCreationForm()
    
    return render(request, "recipes/register.html", {'form': form})

# ✅ User Login View
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

    return render(request, "recipes/login.html")  

# ✅ User Logout View
@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully! 👋")
    return redirect("login")  
