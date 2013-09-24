from django.contrib import admin
from forum.models import Forum, Topic, Post

class ForumAdmin(admin.ModelAdmin):
    pass

class TopicAdmin(admin.ModelAdmin):
    list_display = ["title", "forum", "creator", "created"]
    list_filter = ["forum", "creator"]

class PostAdmin(admin.ModelAdmin):
    search_fields = ["title", "creator"]
    list_display = ["title", "topic", "creator", "created"]

admin.site.register(Forum, ForumAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Post, PostAdmin)
