from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    blog_markdown = models.CharField(max_length=10000)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
