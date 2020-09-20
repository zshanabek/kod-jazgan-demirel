from django.contrib import admin
from .models import Set


class SetAdmin(admin.ModelAdmin):
    fields = ('title', 'cover', 'description')


admin.site.register(Set, SetAdmin)
