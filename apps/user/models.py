from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=32, blank=True, null=True, verbose_name="姓名")
    phone = models.CharField(max_length=11, blank=True, null=True, verbose_name="电话")
    # department = models.ForeignKey('Role', on_delete=models.DO_NOTHING, default=1, verbose_name="职位")

    class Meta:
        db_table = 'user'
        verbose_name = '成员'
        verbose_name_plural = verbose_name


# class Role(models.Model):
#     name = models.CharField(max_length=32, verbose_name="职位")
#     group = models.ManyToManyField(to=Group, verbose_name="部门")
#
#     class Meta:
#         verbose_name = "职位"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.name

# class Group(AbstractUser):
#     class Meta:
#         db_table = 'group'
#         verbose_name = '部门'
#         verbose_name_plural = verbose_name
