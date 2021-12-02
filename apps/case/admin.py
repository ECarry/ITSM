from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('num', 'area', 'status', 'type', 'create_time', 'level')


@admin.register(Petitioner)
class PetitionerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'company', 'department')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ('id', 'manufacturer', 'name', 'sn', 'project')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'project_num')
