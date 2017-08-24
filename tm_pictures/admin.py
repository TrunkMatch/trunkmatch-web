from django.contrib import admin

from tm_pictures.models import InlineTag, Picture

admin.site.register(InlineTag)
admin.site.register(Picture)
