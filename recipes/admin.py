from django.contrib import admin
from .models import Recipe, Comment, Like


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "category", "created_at")
    list_filter = ("status", "category", "created_at")
    search_fields = ("title", "description", "ingredients", "instructions", "author__username")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("-created_at",)
    date_hierarchy = "created_at"
    raw_id_fields = ("author",)


@admin.action(description="Approve selected comments")
def approve_comments(modeladmin, request, queryset):
    queryset.update(is_approved=True)


@admin.action(description="Unapprove selected comments")
def unapprove_comments(modeladmin, request, queryset):
    queryset.update(is_approved=False)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("short_body", "user", "recipe", "is_approved", "created_at")
    list_filter = ("is_approved", "created_at", "recipe")
    search_fields = ("body", "user__username", "recipe__title")
    ordering = ("-created_at",)
    date_hierarchy = "created_at"
    raw_id_fields = ("user", "recipe")
    actions = (approve_comments, unapprove_comments)

    def short_body(self, obj):
        txt = obj.body or ""
        return (txt[:60] + "…") if len(txt) > 60 else txt
    short_body.short_description = "Comment"


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("user", "recipe", "created_at")
    list_filter = ("created_at",)
    search_fields = ("recipe__title", "user__username")
    raw_id_fields = ("user", "recipe")
    date_hierarchy = "created_at"
