from django.db import models
from django.utils.translation import gettext as _
from django_extensions.db.models import TimeStampedModel, TitleSlugDescriptionModel


class Set(TitleSlugDescriptionModel, TimeStampedModel):
    image = models.ImageField(_("Image"), upload_to='sets',
                              height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Набор'
        verbose_name_plural = 'Наборы'
