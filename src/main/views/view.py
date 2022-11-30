import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from api.models.core import LivenessReport
from main.utils import get_all_intervals


def root(request):
    # lines = LivenessReport.objects.order_by('-created_ts').all()
    lines = LivenessReport.objects.order_by('created_ts').all()

    inters = get_all_intervals()
    for line in lines:
        local_time = line.created_ts.astimezone()
        min_index = local_time.hour * 60 + local_time.minute
        day_index = local_time.day - 1
        inters[day_index][min_index] = True
        print(f"day_index={day_index}, min_index={min_index}, time={line.created_ts}")

    context = {
        "intervals": inters,
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