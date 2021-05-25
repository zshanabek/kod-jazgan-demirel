from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db import models as e_models
from martor.models import MartorField


class Post(e_models.TimeStampedModel):
    title = models.CharField(_('title'), max_length=255)
    description = MartorField()
    cover = models.ImageField(upload_to='posts/covers', null=True)
    video = models.FileField(upload_to='posts/videos',
                             max_length=100, null=True)
    set = models.ForeignKey(
        "sets.Set", on_delete=models.CASCADE, null=True, related_name='posts')
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.title
