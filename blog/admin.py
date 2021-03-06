from django.contrib import admin
from .models import *


class PostCommentInline(admin.TabularInline):
    model = PostComment


@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'date_pub', 'author', 'category')
    inlines = [PostCommentInline]


@admin.register(PostComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'date_pub', 'author', 'post')


@admin.register(PostCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
