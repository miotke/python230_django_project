from django.contrib import admin
from blogging.models import Post, Category


admin.site.register(Post)



class PostCategory(admin.ModelAdmin):
    admin.site.register(Category)