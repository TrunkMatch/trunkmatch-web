from django.db import models

from tm_main.models import Profile
from tm_trunk.models import Trunk


class Picture(models.Model):
    """Model for uploaded picture"""
    owner = models.ForeignKey(Profile, blank=False, null=False, related_name='picture_owner')
    trunk = models.ForeignKey(Trunk, blank=True, null=True, related_name='picture_trunk')

    url = models.URLField(blank=False, null=False)
    description = models.CharField(max_length=512, default="")

    def __str__(self):
        return self.trunk.description


class InlineTag(models.Model):
    """Model for a user tagged within a picture"""
    picture = models.ForeignKey('Picture', blank=False, null=False, related_name='inline_tag')

    x_percent = models.FloatField(blank=True, null=True, default=0.0)
    y_percent = models.FloatField(blank=True, null=True, default=0.0)

    tagged_user = models.ForeignKey(Profile, blank=False, null=False, related_name='tagged_user')

    def __str__(self):
        return self.picture.description
