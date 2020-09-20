from django.db import models
from django.utils.translation import gettext as _
from django_extensions.db.models import TimeStampedModel, TitleSlugDescriptionModel


class Set(TitleSlugDescriptionModel, TimeStampedModel):
    cover = models.ImageField(_("Cover"), upload_to='sets', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Набор'
        verbose_name_plural = 'Наборы'
