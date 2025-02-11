from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe, Comment
from .forms import RecipeForm, CommentForm
from django.contrib.auth.decorators import login_required


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
            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        comment_form = CommentForm()

    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe, 'comments': comments, 'comment_form': comment_form})


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.author:
        return redirect('recipe_detail', recipe_id=comment.recipe.id)
    
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', recipe_id=comment.recipe.id)
    else:
        form = CommentForm(instance=comment)
    
    return render(request, 'comments/edit_comment.html', {'form': form})


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.author:
        comment.delete()
    return redirect('recipe_detail', recipe_id=comment.recipe.id)