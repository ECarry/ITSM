from django.db import models
from django.contrib.auth.models import AbstractUser


class Structure(models.Model):
    TYPE_CHOICES = (
        ('unit', "单位"),
        ('department', "部门")
    )
    name = models.CharField(max_length=32, verbose_name="部门")
    type = models.CharField(choices=TYPE_CHOICES, max_length=32, default="department", verbose_name="类型")
    # 如果创建同表之间的递归关联关系，可以使用models.ForeignKey('self')
    patent = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name="父类")

    class Meta:
        verbose_name = '部门'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=32, blank=True, null=True, verbose_name="姓名")
    gender = models.CharField(max_length=10, choices=(("male", "男"), ("female", "女")), default="male",
                              verbose_name="性别")
    image = models.ImageField(upload_to="image/%Y/%m", default="static/img/profile-img.jpg", max_length=100, null=True,
                              blank=True)
    mobile = models.CharField(max_length=11, blank=True, null=True, verbose_name="电话")
    post = models.CharField(max_length=32, null=True, blank=True, verbose_name="职位")
    # 如果创建同表之间的递归关联关系，可以使用models.ForeignKey('self')
    superior = models.ForeignKey("self", on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name="上级主管")
    department = models.ForeignKey('Structure', on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name="部门")

    class Meta:
        db_table = 'user'
        verbose_name = '成员'
        verbose_name_plural = verbose_name
