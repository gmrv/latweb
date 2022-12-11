from datetime import datetime, timedelta
from dataclasses import dataclass

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from api.models.core import LivenessReport
from app import settings
from main.utils import get_all_intervals



@login_required
def liveness_report(request, device_name=None, min_per_interval=None, report_days_count=1):

    if not report_days_count:
        report_days_count = 1
    if not min_per_interval:
        min_per_interval = settings.MINUTES_PER_INTERVAL_DEFAULT

    start = datetime.today() - timedelta(days=report_days_count-1)
    start = start.replace(hour=0, minute=0, second=0)
    query = LivenessReport.objects.filter(created_ts__gte=start)
    device_names = query.values("name").distinct()
    if not device_name:
        device_name = query.values().distinct().first()["name"]

    report_lines = query.filter(name=device_name).order_by('created_ts')

    report_intervals = get_all_intervals(start, min_per_interval, report_days_count)

    for line in report_lines:
        local_time = line.created_ts.astimezone()
        days_from_start = (local_time - start.astimezone()).days
        minutes_from_start = (days_from_start * 24 * 60) + (local_time.hour * 60) + local_time.minute
        interval_index = minutes_from_start // min_per_interval
        report_intervals[interval_index].inc()
        report_intervals[interval_index].hint += f"{local_time.strftime('%d.%m - %H:%M:%S')}\n"

    context = {
        "intervals": report_intervals,
        "last": local_time,
        "min_per_interval": min_per_interval,
        "device_names": device_names,
        "device_name": device_name,
        "report_days_count": report_days_count,
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