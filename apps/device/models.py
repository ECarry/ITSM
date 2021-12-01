from django.db import models


# 类目：类目是一个树状结构的系统，大体上可以分成4-5级。如手机->智能手机->苹果手机类目，
# 在这里面，手机是一级类目，苹果手机是三级类目，也是叶子类目。
# SPU：苹果6（商品聚合信息的最小单位），如手机->苹果手机->苹果6，苹果6就是SPU。
# SKU：土豪金 16G 苹果6 （商品的不可再分的最小单元）。从广义上讲，类目>SPU>SKU。


# 备件 SPU：代表一类
class Device(models.Model):
    name = models.CharField(max_length=32, verbose_name="备件名称")

    class Meta:
        verbose_name = "备件SPU"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 备件 SKU：代表具体型号
class DeviceSKU(models.Model):
    STATUS_CHOICES = {
        (1, "入库"),
        (2, "使用"),
        (3, "损坏"),
        (4, "退货")
    }
    name = models.ForeignKey('Device', on_delete=models.DO_NOTHING, verbose_name="备件名称")
    sn = models.CharField(max_length=32, null=True, blank=True, unique=True, verbose_name="序列号")
    pn = models.CharField(max_length=32, verbose_name="型号")
    spec = models.CharField(max_length=32, null=True, verbose_name="规格")
    unit = models.SmallIntegerField(default=1, verbose_name="备件数")
    device_inventory = models.IntegerField(default=0, verbose_name="备件库存")
    device_used = models.IntegerField(default=0, verbose_name="备件累计使用")
    # auto_now_add=True 时间不变
    # auto_now=True 跟随当前时间
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="入库时间")
    last_time = models.DateTimeField(null=True, blank=True, verbose_name="出库时间")
    return_time = models.DateTimeField(null=True, blank=True, verbose_name="退货时间")
    # on_delete=models.DO_NOTHING 删除备件不影响所关联的类型
    # on_delete=models.CASCADE
    status = models.SmallIntegerField(choices=STATUS_CHOICES, verbose_name="备件状态")
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.DO_NOTHING, verbose_name="厂家")
    stock_in = models.ForeignKey('user.User', related_name="stock_in", null=True, on_delete=models.DO_NOTHING,
                                 verbose_name="入库人")
    stock_out = models.ForeignKey('user.User', related_name="stock_out", null=True, blank=True,
                                  on_delete=models.DO_NOTHING, verbose_name="出库人")

    class Meta:
        # admin 页面显示名称
        verbose_name = '备件'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.pn


# 制造商
class Manufacturer(models.Model):
    manufacturer_name = models.CharField(max_length=32, verbose_name="厂家")

    def __str__(self):
        return self.manufacturer_name

    class Meta:
        verbose_name = '厂家'
        verbose_name_plural = verbose_name
