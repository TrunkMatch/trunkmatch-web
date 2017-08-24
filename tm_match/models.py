from django.contrib.auth.models import User
from django.db import models

from tm_main.models import Profile


class MatchList(models.Model):
    """Model keep track of followers in line for purchasing"""
    profile = models.OneToOneField(Profile)

    def __str__(self):
        return self.profile.user.username

    class Meta:
        ordering = ["profile"]


class MatchListEvent(models.Model):
    """Model to store matching list attributes"""
    match_list = models.ForeignKey('MatchList', blank=False, null=False, related_name='match_list')
    subscriber = models.ForeignKey(User, blank=False, null=False, related_name='match_list_subscriber')

    join_timestamp = models.DateTimeField(default=None, null=True, blank=True)

    def __str__(self):
        return self.match_list.profile.user.username

    class Meta:
        ordering = ["match_list__profile__user"]
