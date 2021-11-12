from django.contrib import admin
from .models import DeviceSKU, Manufacturer, Device


# Register your models here.
@admin.register(DeviceSKU)
class DeviceSKUAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sn', 'pn', )


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('id', 'manufacturer_name')


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
