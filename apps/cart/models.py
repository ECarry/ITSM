from django.db import models
from db.base_model import BaseModel


# 订单类
class Order(BaseModel):
    TRACK_STATUS_CHOICES = {
        (1, "未发货"),
        (2, "已发货"),
        (3, "已收货")
    }
    order_num = models.CharField(max_length=14, verbose_name="订单编号")
    track_num = models.CharField(max_length=32, null=True, blank=True, verbose_name="物流单号")
    track = models.ForeignKey('TrackCompany', on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name="物流公司")
    track_status = models.SmallIntegerField(choices=TRACK_STATUS_CHOICES, default=1, verbose_name="物流状态")
    device = models.ForeignKey('device.DeviceSKU', on_delete=models.DO_NOTHING, verbose_name="备件规格")
    type = models.ForeignKey('device.Device', on_delete=models.DO_NOTHING, null=True, verbose_name="备件类型")
    order_name = models.ForeignKey('user.User', on_delete=models.DO_NOTHING, verbose_name="采购人")
    project = models.ForeignKey('case.Project', on_delete=models.DO_NOTHING, verbose_name="相关项目")
    address = models.ForeignKey('Address', on_delete=models.DO_NOTHING, verbose_name="收货地址")
    case = models.ForeignKey('case.Case', on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name="工单")

    class Meta:
        verbose_name = "采购订单"
        verbose_name_plural = verbose_name


# 物流公司
class TrackCompany(models.Model):
    name = models.CharField(max_length=32, verbose_name="物流公司")

    class Meta:
        verbose_name = "物流公司"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 收货地址
class Address(models.Model):
    address = models.CharField(max_length=256, verbose_name="收货地址")
    addressee = models.ForeignKey('user.User', null=True, on_delete=models.DO_NOTHING, verbose_name="收件人")

    class Meta:
        verbose_name = "收货地址"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.address
