from django.contrib import admin
from .models import *


class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Rooms)
admin.site.register(Services)