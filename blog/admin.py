from django.contrib import admin

# Register your models here.
from .models import Category, Post, Like, Comment, Donat  


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    ...
    
    @admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    ...
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    ...
    
@admin.register(Donat)
class DonatAdmin(admin.ModelAdmin):
    ...

