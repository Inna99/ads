from __future__ import unicode_literals
from django.conf import settings

from django.db import models
from django.utils.encoding import smart_text as smart_unicode
from django.utils.translation import ugettext_lazy as _


class Ad(models.Model):

    # user = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE
    # )
    title = models.CharField(_('Title'), max_length=255)
    body = models.CharField(_('Body'), max_length=1000)
    actual = models.BooleanField(_('Actual'), default=False)
    date_created = models.DateTimeField(_('Date Created'), auto_now_add=True)
    last_modified = models.DateField(_('Last Modified'), auto_now=True)

    class Meta:
        verbose_name = _('Ad')
        verbose_name_plural = _('Ads')

    def __unicode__(self):
        return smart_unicode(self.title)

    def __str___(self):
        return self.title
