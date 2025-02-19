from django.contrib import admin
from .models import Recipe, Comment  # Import your models

# Customizing the Recipe Admin
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # Columns to display in the list view
    search_fields = ('title', 'ingredients', 'instructions')  # Enable search
    prepopulated_fields = {'slug': ('title',)}  # Auto-generate slug from title
    list_filter = ('created_at',)  # Add filters to the right sidebar
    date_hierarchy = 'created_at'  # Add a date drill-down navigation
    ordering = ('-created_at',)  # Default ordering (newest first)


# Customizing the Comment Admin
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe', 'created_at', 'content')
    list_filter = ('created_at', 'user')
    search_fields = ('content', 'user__username', 'recipe__title')  # Search in user's username and recipe title
    ordering = ('-created_at',)


# Optional: If NOT using the @admin.register decorator, you can register like this:
# admin.site.register(Recipe, RecipeAdmin)
# admin.site.register(Comment, CommentAdmin)

