from django.forms import ModelForm
from .models import DeviceSKU, DeviceSPU, Manufacturer


class SKUForm(ModelForm):
    class Meta:
        model = DeviceSKU
        exclude = 'device_inventory', 'device_used'


class SPUForm(ModelForm):
    class Meta:
        model = DeviceSPU
        fields = '__all__'


class ManufacturerForm(ModelForm):
    class Meta:
        model = Manufacturer
        fields = '__all__'
