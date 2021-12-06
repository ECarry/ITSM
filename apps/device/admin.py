from django.contrib import admin
from .models import DeviceSKU, Manufacturer, Device, DeviceSPU


# Register your models here.
@admin.register(DeviceSPU)
class DeviceSPUAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(DeviceSKU)
class DeviceSKUAdmin(admin.ModelAdmin):
    list_display = ('id', 'pn', 'spec', 'manufacturer')


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'sn', 'status', )


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('id', 'manufacturer_name')
