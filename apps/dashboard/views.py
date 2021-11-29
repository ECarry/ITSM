from django.shortcuts import render
from django.views.generic import View
from apps.user.mixin import LoginRequiredMixin
from case.models import Case
import plotly.graph_objects as go
from plotly.offline import plot


class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        # 显示 plotly 图表
        x_data = [0, 1, 2, 3]
        y_data = [0, 1, 2, 3]
        data = go.Scatter(x=x_data, y=y_data, mode='lines', name='test')
        plot_div = plot([data], output_type='div')

        # 今天未处理工单个数
        case_today = Case.objects.all().filter(status='3').count()

        context = {
            'case_today': case_today,
            'plot_div': plot_div
        }

        return render(request, 'dashboard.html', context)
