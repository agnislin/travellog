from django.contrib import admin
from .models import User

# Register your models here.

# We need to tell the admin that Question objects have an admin interface.
admin.site.register(User)
