from django.contrib import admin

from tm_main.models import Documentation, Address, Profile

admin.site.register(Profile)
admin.site.register(Address)
admin.site.register(Documentation)
