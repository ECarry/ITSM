import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import View
from apps.user.mixin import LoginRequiredMixin
from case.models import Case


CURRENT_TIME = datetime.datetime.now()
CURRENT_MONTH = CURRENT_TIME.month
CURRENT_YEAR = CURRENT_TIME.year
CURRENT_DAY = CURRENT_TIME.day


@login_required
def case(request):
    if request.method == 'GET':
        all_data = []
        processing_data = []
        solved_data = []
        for i in range(1, 32):
            all_case_count = Case.objects.filter(create_time__month=CURRENT_MONTH).filter(create_time__day=i).count()
            processing_case_count = Case.objects.filter(create_time__month=CURRENT_MONTH).filter(create_time__day=i)\
                .filter(status=2).count()
            solved_case_count = Case.objects.filter(create_time__month=CURRENT_MONTH).filter(create_time__day=i)\
                .filter(status=3).count()
            all_data.append(all_case_count)
            processing_data.append(processing_case_count)
            solved_data.append(solved_case_count)
        context = {
            'all_data': all_data,
            'processing_data': processing_data,
            'solved_data': solved_data
        }
        print(context)
        return render(request, 'dashboard.html', context)
