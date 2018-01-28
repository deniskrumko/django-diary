from django.db import models
from django.utils.translation import ugettext_lazy as _


class Tag(models.Model):
    tag = models.CharField(
        max_length=255,
        null=True,
        blank=False,
        verbose_name=_('tag'),
        unique=True,
    )

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')


class DiaryEntry(models.Model):
    author = models.ForeignKey(
        'auth.User',
        null=True,
        blank=False,
        related_name='diary_entries',
        verbose_name=_('Author'),
    )

    date = models.DateField(
        null=True,
        blank=False,
        verbose_name=_('Date'),
    )

    text = models.TextField(
        null=True,
        blank=False,
        verbose_name=_('Text'),
    )

    tags = models.ManyToManyField(
        to=Tag,
        blank=True,
        related_name='diary_entries',
        verbose_name=_('Tags'),
    )

    class Meta:
        verbose_name = _('Diary entry')
        verbose_name_plural = _('Diary entries')
