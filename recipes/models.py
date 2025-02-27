from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, null=True)  # ✅ Added slug field
    image = models.ImageField(upload_to='recipes/')  
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    category = models.CharField(max_length=50, choices=[
        ('cake', 'Cake'),
        ('pastry', 'Pastry'),
        ('bread', 'Bread')
    ])    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # ✅ Auto-generate slug from title
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):  # ✅ Ensure Comment model is correctly defined
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.recipe.title}"
