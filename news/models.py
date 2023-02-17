from django.db import models


# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=200, blank=True)
    author = models.CharField(max_length=200, blank=True)
    text = models.TextField()
    image = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def imageUrl(self):
        return self.image.url

    def __str__(self):
        return self.title


class TopPost(models.Model):
    title = models.CharField(max_length=100, blank=True)
    text = models.TextField()
    image = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def imageUrl(self):
        return self.image.url

    def __str__(self):
        return self.title
