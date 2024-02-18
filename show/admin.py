from django.contrib import admin
from .models import RJProfile,Show
# Register your models here.

@admin.register(RJProfile)
class RJProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    pass