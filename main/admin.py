from django.contrib import admin
from .models import Cake
from django.db import models
from tinymce.widgets import TinyMCE

# Register your models here.
class CakeAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/date", {'fields': ["cake_title", "cake_id"]}),
        ("Content", {"fields": ["cake_content"]}),
        ("Image", {"fields": ["photo"]}),
        ("amount", {"fields": ["amount"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }

admin.site.register(Cake, CakeAdmin)
