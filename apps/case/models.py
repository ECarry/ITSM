from django.db import models
from db.base_model import BaseModel


# 工单
class Case(BaseModel):
    STATUS_CHOICES = {
        (1, "审批中"),
        (2, "处理中"),
        (3, "关闭"),
        (4, "超时"),
        (5, "退单")
    }
    LEVEL_CHOICES = {
        (1, "一级"),
        (2, "二级"),
        (3, "三级")
    }
    TYPE_CHOICES = {
        (1, "硬件服务"),
        (2, "技术支撑")
    }
    num = models.CharField(max_length=32, unique=True, verbose_name="工单编号")
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=2, verbose_name="工单状态")
    level = models.SmallIntegerField(choices=LEVEL_CHOICES, default=3, verbose_name="工单等级")
    type = models.SmallIntegerField(choices=TYPE_CHOICES, default=1, verbose_name="服务类型")
    area = models.CharField(max_length=128, null=True, verbose_name="位置")
    context = models.TextField(max_length=256, verbose_name="工单详情")
    register = models.ForeignKey('user.User', related_name="register_name", null=True, on_delete=models.DO_NOTHING,
                                 verbose_name="登记人")
    handler = models.ForeignKey('user.User', related_name="handler_name", null=True, on_delete=models.DO_NOTHING,
                                verbose_name="处理人")
    petitioner = models.ForeignKey('Petitioner', on_delete=models.DO_NOTHING, null=True, verbose_name="客户申请人")
    server = models.ForeignKey('Server', on_delete=models.DO_NOTHING, null=True, verbose_name="设备")

    class Meta:
        verbose_name = "工单"
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.num


# 项目
class Project(models.Model):
    project_name = models.CharField(max_length=256, verbose_name="项目名称")
    project_num = models.CharField(max_length=32, verbose_name="项目编号")
    contract_num = models.CharField(max_length=32, verbose_name="合同编号")
    start_time = models.DateField(null=True, verbose_name="开始时间")
    end_time = models.DateField(null=True, verbose_name="结束时间")
    company = models.CharField(max_length=256, null=True, verbose_name="客户名称")

    class Meta:
        verbose_name = "项目"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.project_name


# 申请单位
class Company(models.Model):
    name = models.CharField(max_length=32, verbose_name="申请单位")

    class Meta:
        verbose_name = "申请单位"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 申请部门
class Department(models.Model):
    name = models.CharField(max_length=32, verbose_name="申请部门")

    class Meta:
        verbose_name = "申请部门"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 申请人
class Petitioner(models.Model):
    name = models.CharField(max_length=32, verbose_name="申请人")
    phone = models.CharField(max_length=11, blank=True, null=True, verbose_name="电话")
    email = models.EmailField(max_length=128, blank=True, null=True, verbose_name="邮箱")
    department = models.ForeignKey('Department', on_delete=models.DO_NOTHING, verbose_name="部门")
    company = models.ForeignKey('Company', on_delete=models.DO_NOTHING, verbose_name="单位")

    class Meta:
        verbose_name = "申请人"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 设备 server
class Server(models.Model):
    name = models.CharField(max_length=32, verbose_name="设备名称")
    sn = models.CharField(max_length=32, unique=True, verbose_name="序列号")
    cpu = models.CharField(max_length=32, null=True, blank=True, verbose_name="cpu")
    mem = models.CharField(max_length=32, null=True, blank=True, verbose_name="mem")
    disk = models.CharField(max_length=32, null=True, blank=True, verbose_name="disk")
    motherboard = models.CharField(max_length=32, null=True, blank=True, verbose_name="motherboard")
    power = models.CharField(max_length=32, null=True, blank=True, verbose_name="power")
    manufacturer = models.ForeignKey('device.Manufacturer', on_delete=models.DO_NOTHING, verbose_name="厂家")
    project = models.ForeignKey('Project', on_delete=models.DO_NOTHING, null=True, verbose_name="所属项目")

    class Meta:
        verbose_name = "服务器"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s SN:%s" % (self.name, self.sn)
