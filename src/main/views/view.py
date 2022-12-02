import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from api.models.core import LivenessReport
from main.utils import get_all_intervals

class IntervalViewItem():
    minutes: int = 0
    hint: str = ""

# @login_required
def liveness_report(request):
    # report_lines = LivenessReport.objects.order_by('-created_ts').all()
    report_lines = LivenessReport.objects.order_by('created_ts').all()

    report_intervals = get_all_intervals()

    for i in range(0,len(report_intervals)):
        for j in range(0,len(report_intervals[i])):
            report_intervals[i][j] = IntervalViewItem()

    for line in report_lines:
        local_time = line.created_ts.astimezone()
        interval_index = (local_time.hour * 60 + local_time.minute) // 10
        day_index = local_time.day - 1
        report_intervals[day_index][interval_index].minutes += 1
        report_intervals[day_index][interval_index].hint += f"{local_time.strftime('%d.%m - %H:%M:%S')};\n"

    context = {
        "intervals": report_intervals,
        "last": local_time
    }
    return render(request, 'main/simple.html', context)

# @login_required
def index(request):
    return HttpResponseRedirect(reverse('main:home'))


# @login_required
def home(request, area_id=None, target_date=None):
    context = {
        'user': "request.user.extuser",
        'area': "xuser.def_area",
        'seats': "seats",
        'rooms': "rooms",
        'target_date': target_date
    }
    return render(request, 'main/home.html', context)