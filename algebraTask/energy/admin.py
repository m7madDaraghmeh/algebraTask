from django.contrib import admin
from .models import Users , Data_returned, Country , Location , Projects ,Devices , projects_location , Projects_device , Projects_user
admin.site.register(Users)
admin.site.register(Data_returned)
admin.site.register(Projects)
admin.site.register(Devices)
admin.site.register(Country)
admin.site.register(Location)
admin.site.register(projects_location)
admin.site.register(Projects_device)
admin.site.register(Projects_user)
