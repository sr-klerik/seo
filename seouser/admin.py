from django.contrib import admin

from .models import SeoUser, Social_VK, Post, Group

admin.site.register(SeoUser)
admin.site.register(Post)
admin.site.register(Group)
admin.site.register(Social_VK)