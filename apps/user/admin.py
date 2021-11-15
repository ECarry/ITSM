from django.contrib import admin
from .models import User, Structure


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'name', 'last_login', 'is_superuser', 'is_staff', 'is_active')


@admin.register(Structure)
class StructureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
