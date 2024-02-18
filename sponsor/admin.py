from django.contrib import admin
from .models import Sponsor,Subscribe
# Register your models here.
@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    pass

@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    pass