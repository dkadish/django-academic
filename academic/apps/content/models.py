from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

from academic.settings import *

class Download(models.Model):
    class Meta:
        ordering = [
            'title', ]
    
    title = models.CharField(
        max_length=256)
    description = models.TextField(
        blank=True,
        null=True)
    file = models.FileField(
        _('File'),
	upload_to=DOWNLOADS_DEFAULT_DIRECTORY,
        max_length=256,
        blank=True,
        null=True)

    def _is_valid(self):
        return not isinstance(self.file.filesize, str) \
            and self.picture.filesize > 0 \
            and self.picture.filetype_checked == 'Document'
    is_valid = property(_is_valid)

    def __unicode__(self):
        return u'%s%s' % (self.title, self.file)
