from django.db import models

class Application(models.Model):
    name = models.CharField(max_length=32, primary_key=True)

    def __unicode__(self):
        return self.name


class Article(models.Model):
    application = models.ForeignKey(Application)
    is_active = models.BooleanField()
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title


class Ad(models.Model):
    is_active = models.BooleanField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.content
