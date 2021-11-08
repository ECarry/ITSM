from django.contrib import admin
from .models import DeviceSKU, DeviceType, Manufacturer


# Register your models here.
@admin.register(DeviceSKU)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ("id",)


@admin.register(DeviceType)
class DeviceTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "type_name")


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("id", "manufacturer_name")
