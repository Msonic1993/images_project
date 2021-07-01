from django.contrib import admin

from .models import Plans, Sizes, Storage

admin.site.register(Plans)
admin.site.register(Sizes)
admin.site.register(Storage)

