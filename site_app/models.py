# blog/models.py

from tinymce.models import HTMLField  
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = HTMLField() 
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False, default=2)

    def save(self, *args, **kwargs):
        if not self.category_id:
            default_category = Category.objects.get(name="World")
            self.category = default_category
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
