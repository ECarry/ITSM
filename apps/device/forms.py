from django.forms import ModelForm
from .models import DeviceSKU


class SKUForm(ModelForm):
    class Meta:
        model = DeviceSKU
        exclude = 'device_inventory', 'device_used'
