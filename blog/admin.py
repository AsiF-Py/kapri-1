from django.contrib import admin
from .models import Category,Blog,Comment
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {"slug": ("title",)}