import json

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, ListView, DetailView
from apps.user.mixin import LoginRequiredMixin
from .models import Device, DeviceSKU, DeviceSPU, Manufacturer
from django.core.paginator import Paginator
from .forms import SKUForm, SPUForm, ManufacturerForm


# 备件列表
class DeviceView(LoginRequiredMixin, ListView):
    model = Device
    template_name = 'device/device_list.html'
    context_object_name = 'devices'
    search_value = ""
    order_filed = "-id"

    def get_queryset(self):
        search = self.request.GET.get('search')
        order_by = self.request.GET.get('orderby')
        # 排序
        if order_by:
            all_devices = Device.objects.all().order_by(order_by)
            self.order_filed = order_by
        else:
            all_devices = Device.objects.all().order_by(self.order_filed)
        # 搜索
        if search:
            all_devices = Device.objects.filter(Q(sn__icontains=search) | Q(stock_out__name__icontains=search))
            self.search_value = search

        self.count_total = all_devices.count()
        paginator = Paginator(all_devices, 10)
        page = self.request.GET.get('page', 1)
        devices = paginator.get_page(page)
        return devices

    def get_context_data(self, *args, **kwargs):
        context = super(DeviceView, self).get_context_data(*args, **kwargs)
        context['count_total'] = self.count_total
        context['search'] = self.search_value
        context['orderby'] = self.order_filed
        context['objects'] = self.get_queryset()
        return context


# 新建备件
class NewDevice(LoginRequiredMixin, View):
    def get(self, request, sku_pk):
        return render(request, 'device/new_device.html')

    def post(self, request, sku_pk):
        current_user_id = request.user.id
        sku_id = sku_pk
        if request.POST.get('sn'):
            sn = request.POST.get('sn')
        else:
            sn = None

        info = {
            'sn': sn,
            'sku_id': sku_id,
            'stock_in_id': current_user_id
        }
        Device.objects.create(**info)
        return redirect('/device/sku/%s' % sku_pk)


# 备件型号列表
class DeviceSKUListView(LoginRequiredMixin, ListView):
    model = DeviceSKU
    template_name = 'device/sku_list.html'
    context_object_name = 'skus'
    search_value = ""
    order_filed = "-id"

    def get_queryset(self):
        search = self.request.GET.get('search')
        order_by = self.request.GET.get('orderby')
        # 排序
        if order_by:
            all_skus = DeviceSKU.objects.all().order_by(order_by)
            self.order_filed = order_by
        else:
            all_skus = DeviceSKU.objects.all().order_by(self.order_filed)
        # 搜索
        if search:
            all_skus = DeviceSKU.objects.filter(Q(pn__icontains=search) | Q(spec__icontains=search))
            self.search_value = search

        self.count_total = all_skus.count()
        paginator = Paginator(all_skus, 10)
        page = self.request.GET.get('page', 1)
        skus = paginator.get_page(page)
        return skus

    def get_context_data(self, *args, **kwargs):
        context = super(DeviceSKUListView, self).get_context_data(*args, **kwargs)
        context['count_total'] = self.count_total
        context['search'] = self.search_value
        context['orderby'] = self.order_filed
        context['objects'] = self.get_queryset()
        return context


# 备件型号详情和备件列表
class DeviceSKUDetailView(LoginRequiredMixin, View):
    def get(self, request, sku_pk):
        # 获取sku
        sku = get_object_or_404(DeviceSKU, pk=sku_pk)
        # 获取关联该 SPU 的备件列表
        devices = Device.objects.filter(sku_id=sku.id)
        # 库存量
        inventory_count = devices.filter(status=1).count()
        # 使用量
        used_count = devices.filter(status=2).count()
        sku.device_inventory = inventory_count
        sku.device_used = used_count
        sku.save()
        context = {
            'sku': sku,
            'devices': devices
        }
        return render(request, 'device/devices_detail.html', context)


# 新建备件型号
class NewDeviceSKUView(LoginRequiredMixin, View):
    def get(self, request):
        form = SKUForm()
        context = {
            'form': form
        }

        return render(request, 'device/new_sku.html', context)

    def post(self, request):
        form = SKUForm(request.POST)
        if form.is_valid():
            form.save()
            print('success')
        else:
            print(form.errors)
        return redirect('device:sku_list')


# 新建SPU
@login_required
def add_spu_popup(request):
    form = SPUForm(request.POST)
    if request.method == 'GET':
        return render(request, 'device/add_spu.html', {'form': form})

    if request.method == 'POST':
        if form.is_valid():
            instance = form.save()
            return HttpResponse(
                '<script>opener.closePopup(window, "%s", "%s", "#id_spu");</script>' % (instance.pk, instance)
            )
        else:
            print(form.errors)
            return render(request, 'device/add_spu.html', {'form': form})


@csrf_exempt
def get_spu_id(request):
    if request.is_ajax():
        spu_name = request.GET['spu_name']
        spu_id = DeviceSPU.objects.get(name=spu_name).id
        data = {'spu_id': spu_id, }
        return HttpResponse(json.dumps(data), content_type='application/json')
    return HttpResponse("/")


# 新建厂家
@login_required
def add_manufacturer_popup(request):
    form = ManufacturerForm(request.POST)
    if request.method == 'GET':
        return render(request, 'device/add_manufacturer.html', {'form': form})

    if request.method == 'POST':
        if form.is_valid():
            instance = form.save()
            return HttpResponse(
                '<script>opener.closePopup(window, "%s", "%s", "#id_manufacturer");</script>' % (instance.pk, instance)
            )
        else:
            print(form.errors)
            return render(request, 'device/add_manufacturer.html', {'form': form})


@csrf_exempt
def get_manufacturer_id(request):
    if request.is_ajax():
        manufacturer_name = request.GET['manufacturer_name']
        manufacturer_id = Manufacturer.objects.get(name=manufacturer_name).id
        data = {'manufacturer_id': manufacturer_id, }
        return HttpResponse(json.dumps(data), content_type='application/json')
    return HttpResponse("/")
