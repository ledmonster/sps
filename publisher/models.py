from django.db import models

class Application(models.Model):
    name = models.CharField(max_length=32, primary_key=True)


class Article(models.Model):
    application = models.ForeignKey(Application)
    is_active = models.BooleanField()
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Ad(models.Model):
    is_active = models.BooleanField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
