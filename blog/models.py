from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="image_blog", null=True)
    author = models.CharField(max_length=150, null=True)

    def __str__(self):
        return f'{self.title} - {self.created_at}'
