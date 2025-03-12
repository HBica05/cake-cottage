from django.http import HttpResponse
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
from django.views import generic


# ✅ Recipe List View (Class-Based)
class RecipeList(generic.ListView):
    queryset = Recipe.objects.filter(status=1)
    template_name = "recipes/recipe_list.html"
    paginate_by = 6


# ✅ Recipe List View (Function-Based, if preferred)
def recipe_list(request):
    recipes = Recipe.objects.filter(status=1)
    return render(request, "recipes/recipe_list.html", {"recipes": recipes})


# ✅ Home Page View (Redirecting to Recipe List)
def index(request):
    return redirect("recipe_list")


# ✅ About Page View
def about_view(request):
    return render(request, 'recipes/about.html')


class EventList(generic.ListView):


    model = EventListtemplate_name = "index.html"
    paginated_by = 12



# def event_detail(request, event_id):
    
#     queryset = Event.objects.all()
#     event = get_object_or_404(queryset, event_id=event_id)

#     return render(
#         request,
#         "events/event_detail.html",
#         {"event": event}
#     )

# ✅ Contact Page View (Handles Form Submission)
def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Send email (Ensure email settings are configured in settings.py)
        send_mail(
            subject=f"New Contact Message from {name}",
            message=f"Message from {name} ({email}):\n\n{message}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=["your-email@example.com"],  # Change this to your email
            fail_silently=False,
        )

        messages.success(request, "Your message has been sent successfully! ✅")
        return redirect("contact")

    return render(request, "recipes/contact.html")


# ✅ Recipe Detail View
def recipe_detail(request, slug):
    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    return render(request, "recipes/recipe_detail.html",{"recipe": recipe,},  
    )


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


# ✅ User Registration View
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after signup
            messages.success(request, "Account created successfully! 🎉")
            return redirect("home")
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
