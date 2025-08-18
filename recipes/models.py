# recipes/models.py
from django.conf import settings
from django.db import models
from django.utils.text import slugify

User = settings.AUTH_USER_MODEL

STATUS = ((0, "Draft"), (1, "Published"))

CATEGORY_CHOICES = [
    ("cake", "Cake"),
    ("pastry", "Pastry"),
    ("bread", "Bread"),
]


class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=220, unique=True, blank=True, db_index=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")

    # Content fields
    content = models.TextField(default="No content provided")  # optional long body
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()

    # Media & meta
    image = models.ImageField(upload_to="recipes/", null=True, blank=True)
    excerpt = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, db_index=True)
    status = models.IntegerField(choices=STATUS, default=0, db_index=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["status", "created_at"]),
            models.Index(fields=["category", "created_at"]),
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        Generate a unique slug from the title on first save.
        If the slug exists, append '-2', '-3', ... until unique.
        """
        if not self.slug:
            base = slugify(self.title) or "recipe"
            candidate = base
            i = 1
            while Recipe.objects.filter(slug=candidate).exclude(pk=self.pk).exists():
                i += 1
                candidate = f"{base}-{i}"
            self.slug = candidate
        super().save(*args, **kwargs)

    @property
    def like_count(self) -> int:
        return self.likes.count()


class Comment(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="comments"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    is_approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        short = (self.body[:40] + "…") if len(self.body) > 40 else self.body
        return f"{self.user} on {self.recipe}: {short}"


class Like(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="likes"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("recipe", "user")
        indexes = [
            models.Index(fields=["recipe", "user"]),
            models.Index(fields=["created_at"]),
        ]

    def __str__(self):
        return f"{self.user} → {self.recipe}"
