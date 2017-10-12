from django.db import models
from taggit.managers import TaggableManager

from tm_main.models import Profile
from tm_pictures.enums import SEASON, GENDER, PIECE


class Trunk(models.Model):
    """Model for Trunks that are for sale"""
    owner = models.ForeignKey(Profile, blank=False, null=False, related_name='owning_user')
    description = models.CharField(max_length=512, default="")

    def __str__(self):
        return self.description


class PurchaseOrder(models.Model):
    """Model for Trunks purchase events"""
    buyer = models.ForeignKey(Profile, blank=False, null=False, related_name='trunk_buyer')
    trunk = models.ForeignKey(Trunk, blank=False, null=False, related_name='purchased_trunk')

    initiation_date = models.DateTimeField(default=None, null=True, blank=True)
    purchase_date = models.DateTimeField(default=None, null=True, blank=True)
    ship_date = models.DateTimeField(default=None, null=True, blank=True)
    delivery_date = models.DateTimeField(default=None, null=True, blank=True)

    shipping_image = models.URLField(blank=False, null=False)
    return_image = models.URLField(blank=False, null=False)

    description = models.CharField(max_length=512, default="")

    def __str__(self):
        return self.description


class Item(models.Model):
    """Model for items in a trunk"""
    trunk = models.ForeignKey(Trunk, blank=False, null=False, related_name='parent_trunk')

    description = models.CharField(max_length=512, default="")
    season = models.IntegerField(choices=SEASON.SEASON, default=4)
    piece = models.IntegerField(choices=PIECE.PIECE, default=6)
    gender = models.IntegerField(choices=GENDER.GENDER, default=6)

    quantity = models.IntegerField(blank=False, null=False, default=0)

    sku = models.CharField(max_length=128, blank=True, null=True, default="")

    brands = TaggableManager()

    def __str__(self):
        return self.description
