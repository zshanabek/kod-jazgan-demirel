from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from .models import Post


class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'set', 'link', 'cover', 'video', 'content')
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }


admin.site.register(Post, PostAdmin)
