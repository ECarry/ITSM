from django.db import models


class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    response_time = models.DateTimeField(blank=True, null=True, verbose_name="响应时间")
    complete_time = models.DateTimeField(blank=True, null=True, verbose_name="完成时间")
    close_time = models.DateTimeField(blank=True, null=True, verbose_name="关闭时间")

    class Meta:
        abstract = True
