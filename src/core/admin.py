from django.contrib import admin

from core.models import Item

admin.site.register(Item, admin.ModelAdmin)
