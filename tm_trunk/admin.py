from django.contrib import admin

from tm_trunk.models import PurchaseOrder, Trunk, Item

admin.site.register(Trunk)
admin.site.register(Item)
admin.site.register(PurchaseOrder)
