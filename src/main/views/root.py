from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# @login_required
def root(request):
    context = {
        'user': "request.user.extuser",
        'area': "xuser.def_area",
        'seats': "seats",
        'rooms': "rooms",
        'target_date': "target_date"
    }
    return render(request, 'main/home.html', context)

# @login_required
def profile(request):
    return HttpResponseRedirect(reverse('root'))


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