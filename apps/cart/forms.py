from django import forms
from django.forms import ModelForm
from .models import *


# order form class
class OrderForm(ModelForm):
    class Meta:
        # widgets -- 自定义界面显示
        # error_messages -- 配置表单验证中的错误提示
        # help_texts -- 重写使用帮助
        # labels -- 设置表单输入前的文字提示
        model = Order
        exclude = ['order_num', 'order_name', 'response_time', 'complete_time', 'close_time', 'create_time',
                   'track_status']

        widgets = {
            'count': forms.NumberInput(attrs={'min': '1', 'max': '99'}),
            'project': forms.Select(attrs={'class': 'col-md-6'})
        }




