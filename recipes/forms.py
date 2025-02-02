# forms.py
from django import forms
from .models import Recipe, Comment

# Form for creating/updating recipes
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'instructions']

# Form for adding comments to recipes
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
