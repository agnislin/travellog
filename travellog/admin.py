from django.contrib import admin
from .models import Account, Personal, Package, Album, Picture

# Register your models here.

# We need to tell the admin that Question objects have an admin interface.
admin.site.register(Account)
admin.site.register(Personal)
admin.site.register(Package)
admin.site.register(Album)
admin.site.register(Picture)
