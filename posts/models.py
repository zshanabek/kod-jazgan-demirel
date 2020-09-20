from django_extensions.db import models as e_models
from django.db import models


class Post(e_models.TimeStampedModel):
    set = models.ForeignKey(
        "sets.Set", on_delete=models.CASCADE, null=True, related_name='posts')
    content = models.TextField()
    title = models.CharField(max_length=255)
    link = models.URLField(max_length=200)
    cover = models.ImageField(upload_to='posts', null=True)

    def __str__(self):
        return self.title
