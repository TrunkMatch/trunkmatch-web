from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models


class Profile(models.Model):
    """Model to extend the Django User"""
    user = models.OneToOneField(User)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits.")
    phone_number = models.CharField(validators=[phone_regex], max_length=16, blank=True)
    phone_country = models.CharField(max_length=32, blank=True, null=True, default="")

    follows = models.ManyToManyField('self', related_name='profile_followers', symmetrical=False, blank=True,
                                     default=None)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ["user"]


class Country(models.Model):
    """Model for countries"""
    iso_code = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=45, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"
        ordering = ["name", "iso_code"]


class StateProvince(models.Model):
    """Model for states and provinces"""
    iso_code = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=55, blank=False)
    country = models.ForeignKey(Country, to_field="iso_code")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "State or province"


class Address(models.Model):
    """Model to store addresses for accounts"""
    profile = models.OneToOneField(Profile)

    address_line1 = models.CharField("Address line 1", max_length=45)
    address_line2 = models.CharField("Address line 2", max_length=45, blank=True)
    postal_code = models.CharField("Postal Code", max_length=10)
    city = models.CharField(max_length=50, blank=False)
    state_province = models.CharField("State/Province", max_length=40, blank=True)
    country = models.ForeignKey(Country, blank=False)

    def __str__(self):
        return "%s, %s %s" % (self.city, self.state_province, str(self.country))

    class Meta:
        verbose_name_plural = "Addresses"
        unique_together = ("address_line1", "address_line2", "postal_code", "city", "state_province", "country")


class Documentation(models.Model):
    """Model to store documentation for users"""
    profile = models.ForeignKey(Profile, blank=False, null=False, related_name='owning_user_profile')

    url = models.URLField(blank=False, null=False)
    description = models.CharField(max_length=512, default="")

    def __str__(self):
        return self.trunk.description

    class Meta:
        verbose_name_plural = "Documentation"
