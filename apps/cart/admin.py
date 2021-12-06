from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_num', 'device',)


@admin.register(TrackCompany)
class TrackCompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'address')
