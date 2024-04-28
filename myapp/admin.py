from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Image)


class ImageAdmin(admin.ModelAdmin):
    list_display = ["id", "photo", "date"]


admin.site.register(RegisterModel)
