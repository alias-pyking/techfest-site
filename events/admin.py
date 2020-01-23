from django.contrib import admin

from .models import Event,Star,RegisterEventUsers
admin.site.register(Event)
admin.site.register(Star)
admin.site.register(RegisterEventUsers)