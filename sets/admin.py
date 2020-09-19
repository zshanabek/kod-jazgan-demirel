from django.contrib import admin
from .models import Set


class SetAdmin(admin.ModelAdmin):
    fields = ('title', 'image')


admin.site.register(Set, SetAdmin)
