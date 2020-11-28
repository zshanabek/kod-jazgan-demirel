from django_extensions.db import models as e_models
from django.db import models


class Post(e_models.TimeStampedModel, e_models.TitleSlugDescriptionModel):
    cover = models.ImageField(upload_to='posts/covers', null=True)
    video = models.FileField(upload_to='posts/videos',
                             max_length=100, null=True)
    set = models.ForeignKey(
        "sets.Set", on_delete=models.CASCADE, null=True, related_name='posts')

    def __str__(self):
        return self.title
