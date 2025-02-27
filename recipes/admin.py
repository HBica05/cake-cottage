from django.contrib import admin
from .models import Recipe, Comment  # ✅ Ensure Comment is imported

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at')  # ✅ Ensure slug is a valid field
    search_fields = ('title', 'ingredients', 'instructions')  
    prepopulated_fields = {'slug': ('title',)}  # ✅ Ensure slug is defined in models.py
    list_filter = ('created_at',)  
    ordering = ('-created_at',)  

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe', 'created_at', 'text')  
    list_filter = ('created_at', 'user')
    search_fields = ('text', 'user__username', 'recipe__title')  
    ordering = ('-created_at',)
