from django.contrib import admin
from publisher.models import Application, Article, Ad


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("name",)


class ArticleAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ("id", "application", "is_active", "title", "created_at", "modified_at")
    list_filter = ["application"]


class AdAdmin(admin.ModelAdmin):
    list_display = ("id", "is_active", "content", "created_at", "modified_at")


admin.site.register(Application, ApplicationAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Ad, AdAdmin)
