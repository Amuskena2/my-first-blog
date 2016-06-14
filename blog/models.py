from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200, verbose_name=_('Nombre'))
    text = models.TextField(verbose_name=_('Texto'))
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
