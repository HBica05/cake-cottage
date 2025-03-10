from django.contrib import admin
from .models import Recipe, Comment  


admin.site.register(Recipe)
admin.site.register(Comment)


# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('user', 'recipe', 'created_at', 'text')  
#     list_filter = ('created_at', 'user')
#     search_fields = ('text', 'user__username', 'recipe__title')  
#     ordering = ('-created_at',)
