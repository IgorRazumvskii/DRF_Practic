from django.contrib import admin

from .models import Beauty, Images, Level, Coords, CustomUser

admin.site.register(Beauty)
admin.site.register(Images)
admin.site.register(Level)
admin.site.register(Coords)
admin.site.register(CustomUser)
