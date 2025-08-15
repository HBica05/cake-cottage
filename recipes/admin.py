from django.contrib import admin
from .models import Recipe, Comment, Like

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "category", "created_at")
    list_filter = ("status", "category", "created_at")
    search_fields = ("title", "description", "ingredients", "instructions", "author__username")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("-created_at",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "recipe", "user", "body", "created_at")
    list_filter = ("is_approved", "created_at", "recipe")
    search_fields = ("body", "user__username", "recipe__title")
    ordering = ("-created_at",)

    def short_body(self, obj):
        txt = obj.body or ""
        return (txt[:50] + "…") if len(txt) > 50 else txt
    short_body.short_description = "body"


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("recipe", "user")
    search_fields = ("recipe__title", "user__username")
