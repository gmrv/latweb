import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from api.models.core import LivenessReport
from app import settings
from main.utils import get_all_intervals


class IntervalViewItem():
    minutes: int = 0
    max_minutes: int = 0
    percent: int = 0

    hint: str = ""

    def inc(self):
        self.minutes +=1
        self.percent = (self.minutes / self.max_minutes * 100)

    def percent_str(self):
        return str(self.percent)

@login_required
def liveness_report(request, device_name=None, min_per_interval=None):

    query = LivenessReport.objects.all()
    device_names = query.values("name").distinct()

    if not device_name:
        device_name = query.values().distinct().first()["name"]
    if not min_per_interval:
        min_per_interval = settings.MINUTES_PER_INTERVAL_DEFAULT

    report_lines = query.filter(name=device_name).order_by('created_ts')

    report_intervals = get_all_intervals(min_per_interval)

    for i in range(0,len(report_intervals)):
        for j in range(0,len(report_intervals[i])):
            report_intervals[i][j] = IntervalViewItem()
            report_intervals[i][j].max_minutes = min_per_interval

    for line in report_lines:
        local_time = line.created_ts.astimezone()
        interval_index = (local_time.hour * 60 + local_time.minute) // min_per_interval
        day_index = local_time.day - 1
        report_intervals[day_index][interval_index].inc()
        report_intervals[day_index][interval_index].hint += f"{local_time.strftime('%d.%m - %H:%M:%S')}\n"

    context = {
        "intervals": report_intervals,
        "last": local_time,
        "min_per_interval": min_per_interval,
        "device_names": device_names,
        "device_name": device_name,
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