from django.contrib import admin
from blogging.models import Post, Category


# admin.site.register(Post)



# class PostCategory(admin.ModelAdmin):
#     admin.site.register(Category)

class CategoryInline(admin.TabularInline):
    model = Category.posts.through


# @admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]


# @admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)