from django.contrib import admin
from . import models



class GroomingAdminSite(admin.AdminSite):
    site_header = "Gise Grooms admin"
    site_title = "Gise Grooms"
    index_title = "Gise Grooms"

groom_site = GroomingAdminSite(name='GroomingAdmin')

groom_site.register(models.User)
groom_site.register(models.Service)
groom_site.register(models.Appointment)

admin.site.register(models.User)
admin.site.register(models.Service)
admin.site.register(models.Appointment)

# Register your models here.
