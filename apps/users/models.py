from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields import JSONField


class User(AbstractUser):
    email = models.EmailField(
        _('email address'),
        blank=False,
        unique=True
    )
    settings = JSONField(
        default={
            'theme': 'light',
            'font': 'Caveat',
            'language': 'en',
        },
        blank=True,
        null=True,
        verbose_name=_('settings')
    )

    def __str__(self):
        return self.username or self.email

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        ordering = ('email',)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def theme(self):
        theme = self.settings.get('theme')
        return theme or 'light'
